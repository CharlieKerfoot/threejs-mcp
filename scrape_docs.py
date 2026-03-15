"""
Scrapes Three.js documentation and creates condensed markdown files.
Run this once to populate the docs/ directory.
"""

import asyncio
import json
import re
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://threejs.org/docs"
DOCS_DIR = Path(__file__).parent / "docs"


async def fetch_index(client: httpx.AsyncClient) -> dict[str, list[str]]:
  """Parse the index.html to get categories and page names."""
  resp = await client.get(f"{BASE_URL}/index.html")
  resp.raise_for_status()
  soup = BeautifulSoup(resp.text, "html.parser")

  content = soup.find("div", id="content")
  categories: dict[str, list[str]] = {}
  current_h2 = ""
  current_h3 = ""

  for el in content.find_all(["h2", "h3", "a"]):
    if el.name == "h2":
      current_h2 = el.get_text(strip=True)
    elif el.name == "h3":
      current_h3 = el.get_text(strip=True)
      key = f"{current_h2}/{current_h3}" if current_h2 else current_h3
    elif el.name == "a":
      href = el.get("href", "")
      if href.endswith(".html"):
        page_name = href.replace(".html", "")
        key = f"{current_h2}/{current_h3}" if current_h2 else current_h3
        categories.setdefault(key, []).append(page_name)

  return categories


def parse_page(html: str, class_name: str) -> str:
  """Parse a doc page HTML into condensed markdown."""
  soup = BeautifulSoup(html, "html.parser")
  lines: list[str] = []

  # Inheritance
  inheritance = soup.find("p", class_="inheritance")
  if inheritance:
    chain = inheritance.get_text(strip=True).replace("→", "→")
    if chain:
      lines.append(f"Extends: {chain}")

  # Title
  h1 = soup.find("h1")
  title = h1.get_text(strip=True) if h1 else class_name
  lines.insert(0, f"# {title}")

  # Description
  desc_div = soup.find("div", class_="class-description")
  if desc_div:
    lines.append("")
    lines.append(desc_div.get_text(" ", strip=True))

  # Constructor
  constructor = soup.find("div", class_="container-overview")
  if constructor:
    h3 = constructor.find("h3")
    if h3:
      sig = h3.get_text(strip=True)
      lines.append("")
      lines.append(f"## Constructor")
      lines.append(f"`{sig}`")
      # Constructor params
      params = constructor.find_all("div", class_="param")
      if params:
        for p in params:
          name_el = p.find("span", class_="param-name")
          type_el = p.find("span", class_="param-type")
          desc_el = p.find("div", class_="param-description")
          name = name_el.get_text(strip=True) if name_el else ""
          typ = type_el.get_text(strip=True) if type_el else ""
          desc = desc_el.get_text(" ", strip=True) if desc_el else ""
          line = f"- **{name}**"
          if typ:
            line += f" : `{typ}`"
          if desc:
            line += f" — {desc}"
          lines.append(line)
      # Constructor description
      desc = constructor.find("div", class_="description")
      if desc:
        text = desc.get_text(" ", strip=True)
        if text and text != sig:
          lines.append(text)

  # Collect properties and methods by iterating all elements in order
  # Methods can be either wrapped in <div class="member"> or appear as
  # bare <h3> + <div class="method"> siblings under <article>
  article = soup.find("article")
  if not article:
    return "\n".join(lines)

  def parse_entry(h3_el, context_el=None):
    """Parse an h3 element into a doc entry line."""
    name_a = h3_el.find("a")
    if not name_a:
      return None, []
    name_text = name_a.get_text(strip=True)
    type_sig = h3_el.find("span", class_="type-signature")
    type_text = type_sig.get_text(strip=True) if type_sig else ""
    sig = h3_el.find("span", class_="signature")
    sig_text = sig.get_text(strip=True) if sig else ""

    entry = f".{name_text}"
    if sig_text:
      entry += sig_text
    if type_text:
      entry += f" {type_text}"

    # Find description and params from context element (member div or method div)
    search_el = context_el or h3_el.parent
    desc_div = search_el.find("div", class_="description") if search_el else None
    desc_text = ""
    if desc_div:
      desc_text = desc_div.get_text(" ", strip=True)
      if len(desc_text) > 200:
        desc_text = desc_text[:197] + "..."

    params = search_el.find_all("div", class_="param") if search_el else []
    param_strs = []
    for p in params:
      pname = p.find("span", class_="param-name")
      ptype = p.find("span", class_="param-type")
      pdesc = p.find("div", class_="param-description")
      ps = pname.get_text(strip=True) if pname else ""
      if ptype:
        ps += f": {ptype.get_text(strip=True)}"
      if pdesc:
        pd = pdesc.get_text(" ", strip=True)
        if len(pd) > 100:
          pd = pd[:97] + "..."
        ps += f" — {pd}"
      if ps:
        param_strs.append(ps)

    line = f"- `{entry}`"
    if desc_text:
      line += f" — {desc_text}"
    return line, param_strs

  # Walk through all direct and nested children of the article
  for el in article.find_all(["h2", "h3", "div"], recursive=True):
    if el.name == "h2" and "subsection-title" in el.get("class", []):
      section_name = el.get_text(strip=True)
      lines.append("")
      lines.append(f"## {section_name}")
    elif el.name == "div" and "member" in el.get("class", []):
      # Property or method wrapped in a member div
      h3 = el.find("h3")
      if not h3:
        continue
      line, param_strs = parse_entry(h3, el)
      if line:
        lines.append(line)
        for ps in param_strs:
          lines.append(f"  - {ps}")
    elif el.name == "h3" and "name-method" in el.get("class", []):
      # Bare method h3 (not inside a member div)
      if el.find_parent("div", class_="member"):
        continue  # Already handled above
      if el.find_parent("div", class_="container-overview"):
        continue  # Constructor, already handled
      # Find the sibling method div
      method_div = el.find_next_sibling("div", class_="method")
      line, param_strs = parse_entry(el, method_div)
      if line:
        lines.append(line)
        for ps in param_strs:
          lines.append(f"  - {ps}")

  return "\n".join(lines)


async def scrape_page(
  client: httpx.AsyncClient, name: str, semaphore: asyncio.Semaphore
) -> tuple[str, str | None]:
  """Fetch and parse a single doc page."""
  async with semaphore:
    try:
      resp = await client.get(f"{BASE_URL}/pages/{name}.html")
      if resp.status_code != 200:
        return name, None
      return name, parse_page(resp.text, name)
    except Exception as e:
      print(f"  Error fetching {name}: {e}")
      return name, None


async def main():
  DOCS_DIR.mkdir(exist_ok=True)

  async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
    print("Fetching index...")
    categories = await fetch_index(client)

    # Save index
    index_data = {}
    for cat, pages in categories.items():
      index_data[cat] = pages
    with open(DOCS_DIR / "index.json", "w") as f:
      json.dump(index_data, f, indent=2)

    # Collect all unique page names
    all_pages = set()
    for pages in categories.values():
      all_pages.update(pages)

    print(f"Found {len(all_pages)} pages across {len(categories)} categories")

    # Scrape all pages with concurrency limit
    semaphore = asyncio.Semaphore(20)
    tasks = [scrape_page(client, name, semaphore) for name in sorted(all_pages)]

    results = {}
    done = 0
    for coro in asyncio.as_completed(tasks):
      name, content = await coro
      done += 1
      if done % 50 == 0:
        print(f"  {done}/{len(all_pages)} pages scraped...")
      if content:
        results[name] = content

    print(f"Successfully scraped {len(results)} pages")

    # Save each page as a markdown file
    for name, content in results.items():
      filepath = DOCS_DIR / f"{name}.md"
      filepath.write_text(content)

    print(f"Saved {len(results)} markdown files to {DOCS_DIR}")

    # Create a compact search index
    search_index = {}
    for name, content in results.items():
      # Extract first non-header line as description
      desc_lines = [
        line for line in content.split("\n")
        if line and not line.startswith("#") and not line.startswith("Extends:")
      ]
      desc = desc_lines[0] if desc_lines else ""
      if len(desc) > 150:
        desc = desc[:147] + "..."
      search_index[name] = desc

    with open(DOCS_DIR / "search_index.json", "w") as f:
      json.dump(search_index, f, indent=2)

    print("Done!")


if __name__ == "__main__":
  asyncio.run(main())
