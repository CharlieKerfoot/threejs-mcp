# Threejs-mcp

A Three.js code-generation [MCP server](https://modelcontextprotocol.io/). Each tool encodes Three.js API knowledge directly and returns ready-to-use JavaScript — no manual boilerplate needed.

## Tools

| Category | Tools |
|---|---|
| Scene & Renderer | `scene_setup`, `html_template` |
| Cameras | `perspective_camera`, `orthographic_camera` |
| Geometry | `geometry`, `extrude_geometry`, `lathe_geometry`, `tube_geometry` |
| Materials | `material`, `shader_material` |
| Meshes | `mesh`, `instanced_mesh`, `group` |
| Lighting | `ambient_light`, `directional_light`, `point_light`, `spot_light`, `hemisphere_light`, `rect_area_light` |
| Controls | `orbit_controls`, `fly_controls`, `pointer_lock_controls`, `transform_controls` |
| Loaders | `gltf_loader`, `texture_loader`, `cube_texture_loader`, `hdr_environment`, `fbx_loader` |
| Animation | `animation_loop`, `keyframe_animation`, `tween_animation` |
| Interaction | `raycaster` |
| Helpers | `debug_helpers`, `light_helpers` |
| Post-processing | `postprocessing_setup` |
| Environment | `ground_plane`, `skybox`, `water_surface`, `particles`, `reflective_surface`, `lensflare` |
| UI | `css2d_label` |
| Physics | `rapier_physics` |
| XR | `webxr_setup` |
| Utilities | `math_utils`, `dispose_resources` |

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Installation

Clone this repository, then follow the instructions for your MCP client below. Replace `/path/to/threejs-mcp` with the actual path to the cloned repo.

### Claude Code

```bash
claude mcp add threejs -s user -- uv run --directory /path/to/threejs-mcp server.py
```

The scope (`-s`) can be `user`, `project`, or `local`.

### Claude Desktop

Open **Settings > Developer > Edit Config** and add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
    }
  }
}
```

### Cursor

Open **Settings > MCP > Add new global MCP server** and add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
    }
  }
}
```

Or add to `.cursor/mcp.json` in your project root for project-scoped configuration.

### Windsurf

Open **Settings > MCP > Add Server > Add custom server** and add to your MCP config:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
    }
  }
}
```

### VS Code / GitHub Copilot

Add to your user or workspace `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "threejs": {
        "command": "uv",
        "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
      }
    }
  }
}
```

Or create `.vscode/mcp.json` in your project root:

```json
{
  "servers": {
    "threejs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
    }
  }
}
```

### Zed

Add to your Zed settings (`~/.config/zed/settings.json`):

```json
{
  "context_servers": {
    "threejs": {
      "command": {
        "path": "uv",
        "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
      }
    }
  }
}
```

### Cline

Open **Settings > MCP Servers > Edit MCP Settings** and add to the config:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
    }
  }
}
```

### Continue

Add to your `~/.continue/config.yaml`:

```yaml
mcpServers:
  - name: threejs
    command: uv
    args:
      - run
      - --directory
      - /path/to/threejs-mcp
      - server.py
```

### Roo Code

Open **Settings > MCP > Edit MCP Settings** and add:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/threejs-mcp", "server.py"]
    }
  }
}
```

### Any other MCP client

This is a standard stdio MCP server. Run it with:

```bash
uv run --directory /path/to/threejs-mcp server.py
```

## Scraping docs

The `docs/` directory contains condensed markdown scraped from the Three.js documentation. To regenerate:

```bash
uv run python scrape_docs.py
```

This requires the `httpx` and `beautifulsoup4` packages (not included in the main dependencies).
