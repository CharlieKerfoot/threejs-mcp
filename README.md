# threejs-mcp

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

Clone this repository, then update the path in `run.sh` to point to the cloned directory:

```bash
#!/bin/zsh
source ~/.zshrc
exec uv run --directory /path/to/threejs-mcp threejs-mcp
```

Make the script executable:

```bash
chmod +x run.sh
```

Then follow the instructions for your MCP client below. Replace `/path/to/threejs-mcp/run.sh` with the actual path to the script.

### Claude Code

```bash
claude mcp add threejs -s user -- /path/to/threejs-mcp/run.sh
```

The scope (`-s`) can be `user`, `project`, or `local`.

### Claude Desktop

Open **Settings > Developer > Edit Config** and add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "/path/to/threejs-mcp/run.sh"
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
      "command": "/path/to/threejs-mcp/run.sh"
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
      "command": "/path/to/threejs-mcp/run.sh"
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
        "command": "/path/to/threejs-mcp/run.sh"
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
      "command": "/path/to/threejs-mcp/run.sh"
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
        "path": "/path/to/threejs-mcp/run.sh"
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
      "command": "/path/to/threejs-mcp/run.sh"
    }
  }
}
```

### Continue

Add to your `~/.continue/config.yaml`:

```yaml
mcpServers:
  - name: threejs
    command: /path/to/threejs-mcp/run.sh
```

### Roo Code

Open **Settings > MCP > Edit MCP Settings** and add:

```json
{
  "mcpServers": {
    "threejs": {
      "command": "/path/to/threejs-mcp/run.sh"
    }
  }
}
```

### Any other MCP client

This is a standard stdio MCP server. Run it with:

```bash
/path/to/threejs-mcp/run.sh
```

## Scraping docs

The `docs/` directory contains condensed markdown scraped from the Three.js documentation. To regenerate:

```bash
uv run python scrape_docs.py
```

This requires the `httpx` and `beautifulsoup4` packages (not included in the main dependencies).
