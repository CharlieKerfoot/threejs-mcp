"""
Three.js MCP Server — native Three.js code-generation tools.
Each tool encodes Three.js API knowledge directly, returning ready-to-use
JavaScript code. Tools are numerous and well-described so Claude Code's
deferred tool search can find them without loading all schemas upfront.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
  "threejs",
  instructions=(
    "Three.js code-generation MCP server. Use these tools when building "
    "Three.js applications. Each tool returns ready-to-use JavaScript code. "
    "Use tool search to find the right tool for your task."
  ),
)


# ---------------------------------------------------------------------------
# Scene & Renderer Setup
# ---------------------------------------------------------------------------

@mcp.tool()
def scene_setup(
  renderer: str = "webgpu",
  antialias: bool = True,
  alpha: bool = False,
  shadow_map: bool = True,
  tone_mapping: str = "ACESFilmic",
  pixel_ratio: bool = True,
  background: str = "#000000",
  fog_type: str = "none",
  fog_color: str = "#cccccc",
  fog_near: float = 1,
  fog_far: float = 1000,
  fog_density: float = 0.00025,
) -> str:
  """Generate complete Three.js scene boilerplate with renderer, resize handling,
  and animation loop. Use this as the starting point for any Three.js project.
  Supports WebGPU and WebGL renderers."""
  renderer_class = "WebGPURenderer" if renderer == "webgpu" else "WebGLRenderer"
  renderer_import = (
    "three/addons/renderers/webgpu/WebGPURenderer.js"
    if renderer == "webgpu"
    else "three"
  )

  tone_map = {
    "none": "THREE.NoToneMapping",
    "linear": "THREE.LinearToneMapping",
    "reinhard": "THREE.ReinhardToneMapping",
    "cineon": "THREE.CineonToneMapping",
    "ACESFilmic": "THREE.ACESFilmicToneMapping",
    "AgX": "THREE.AgXToneMapping",
    "neutral": "THREE.NeutralToneMapping",
  }
  tone = tone_map.get(tone_mapping, "THREE.ACESFilmicToneMapping")

  fog_code = ""
  if fog_type == "linear":
    fog_code = f"\nscene.fog = new THREE.Fog('{fog_color}', {fog_near}, {fog_far});"
  elif fog_type == "exponential":
    fog_code = f"\nscene.fog = new THREE.FogExp2('{fog_color}', {fog_density});"

  imports = [f'import * as THREE from "three";']
  if renderer == "webgpu":
    imports.append(
      f'import {{ {renderer_class} }} from "{renderer_import}";'
    )

  shadow_code = ""
  if shadow_map:
    shadow_code = """
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;"""

  pr_code = (
    "\nrenderer.setPixelRatio(window.devicePixelRatio);"
    if pixel_ratio
    else ""
  )

  return f"""{chr(10).join(imports)}

// Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color('{background}');{fog_code}

// Renderer
const renderer = new {renderer_class}({{ antialias: {str(antialias).lower()}, alpha: {str(alpha).lower()} }});
renderer.setSize(window.innerWidth, window.innerHeight);{pr_code}
renderer.toneMapping = {tone};
renderer.toneMappingExposure = 1.0;{shadow_code}
document.body.appendChild(renderer.domElement);

// Resize handler
window.addEventListener('resize', () => {{
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}});

// Animation loop
function animate() {{
  requestAnimationFrame(animate);
  // Update controls, animations, etc. here
  renderer.render(scene, camera);
}}
animate();"""


@mcp.tool()
def html_template(
  title: str = "Three.js App",
  importmap_version: str = "0.175.0",
  use_addons: bool = True,
) -> str:
  """Generate a complete HTML file with Three.js import map for ES module usage.
  Includes proper meta tags, canvas styling, and import map configuration."""
  addons = ""
  if use_addons:
    addons = f"""
        "three/addons/": "https://cdn.jsdelivr.net/npm/three@{importmap_version}/examples/jsm/","""

  return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    body {{ margin: 0; overflow: hidden; }}
    canvas {{ display: block; }}
  </style>
</head>
<body>
  <script type="importmap">
    {{
      "imports": {{
        "three": "https://cdn.jsdelivr.net/npm/three@{importmap_version}/build/three.module.js",{addons}
      }}
    }}
  </script>
  <script type="module" src="./main.js"></script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Cameras
# ---------------------------------------------------------------------------

@mcp.tool()
def perspective_camera(
  fov: float = 50,
  near: float = 0.1,
  far: float = 2000,
  position_x: float = 0,
  position_y: float = 5,
  position_z: float = 10,
  look_at_x: float = 0,
  look_at_y: float = 0,
  look_at_z: float = 0,
) -> str:
  """Generate a Three.js PerspectiveCamera. Most common camera type, mimics
  human eye perspective. Use for standard 3D scenes."""
  return f"""const camera = new THREE.PerspectiveCamera(
  {fov},
  window.innerWidth / window.innerHeight,
  {near},
  {far}
);
camera.position.set({position_x}, {position_y}, {position_z});
camera.lookAt({look_at_x}, {look_at_y}, {look_at_z});"""


@mcp.tool()
def orthographic_camera(
  size: float = 10,
  near: float = 0.1,
  far: float = 2000,
  position_x: float = 0,
  position_y: float = 10,
  position_z: float = 10,
  look_at_x: float = 0,
  look_at_y: float = 0,
  look_at_z: float = 0,
) -> str:
  """Generate a Three.js OrthographicCamera. No perspective distortion —
  objects remain the same size regardless of distance. Use for 2D games,
  isometric views, UI overlays, or technical/CAD views."""
  return f"""const aspect = window.innerWidth / window.innerHeight;
const camera = new THREE.OrthographicCamera(
  -{size} * aspect, {size} * aspect,
  {size}, -{size},
  {near}, {far}
);
camera.position.set({position_x}, {position_y}, {position_z});
camera.lookAt({look_at_x}, {look_at_y}, {look_at_z});"""


# ---------------------------------------------------------------------------
# Geometries
# ---------------------------------------------------------------------------

GEOMETRIES = {
  "box": {
    "class": "BoxGeometry",
    "params": ["width=1", "height=1", "depth=1", "widthSegments=1", "heightSegments=1", "depthSegments=1"],
    "desc": "Rectangular cuboid centered at origin.",
  },
  "sphere": {
    "class": "SphereGeometry",
    "params": ["radius=1", "widthSegments=32", "heightSegments=16", "phiStart=0", "phiLength=Math.PI*2", "thetaStart=0", "thetaLength=Math.PI"],
    "desc": "Sphere generated by sweeping around axes.",
  },
  "plane": {
    "class": "PlaneGeometry",
    "params": ["width=1", "height=1", "widthSegments=1", "heightSegments=1"],
    "desc": "Flat plane in the X-Y plane.",
  },
  "cylinder": {
    "class": "CylinderGeometry",
    "params": ["radiusTop=1", "radiusBottom=1", "height=1", "radialSegments=32", "heightSegments=1", "openEnded=false", "thetaStart=0", "thetaLength=Math.PI*2"],
    "desc": "Cylinder with separate top/bottom radii. Set radiusTop=0 for a cone.",
  },
  "cone": {
    "class": "ConeGeometry",
    "params": ["radius=1", "height=1", "radialSegments=32", "heightSegments=1", "openEnded=false", "thetaStart=0", "thetaLength=Math.PI*2"],
    "desc": "Cone (cylinder with zero top radius).",
  },
  "torus": {
    "class": "TorusGeometry",
    "params": ["radius=1", "tube=0.4", "radialSegments=12", "tubularSegments=48", "arc=Math.PI*2"],
    "desc": "Donut/ring shape.",
  },
  "torusknot": {
    "class": "TorusKnotGeometry",
    "params": ["radius=1", "tube=0.4", "tubularSegments=64", "radialSegments=8", "p=2", "q=3"],
    "desc": "Torus knot — a knot that winds p times around and q times through the torus.",
  },
  "ring": {
    "class": "RingGeometry",
    "params": ["innerRadius=0.5", "outerRadius=1", "thetaSegments=32", "phiSegments=1", "thetaStart=0", "thetaLength=Math.PI*2"],
    "desc": "Flat 2D ring (annulus).",
  },
  "circle": {
    "class": "CircleGeometry",
    "params": ["radius=1", "segments=32", "thetaStart=0", "thetaLength=Math.PI*2"],
    "desc": "Flat 2D circle/sector.",
  },
  "capsule": {
    "class": "CapsuleGeometry",
    "params": ["radius=1", "length=1", "capSegments=4", "radialSegments=8"],
    "desc": "Capsule (cylinder with hemispherical caps).",
  },
  "dodecahedron": {
    "class": "DodecahedronGeometry",
    "params": ["radius=1", "detail=0"],
    "desc": "12-sided polyhedron.",
  },
  "icosahedron": {
    "class": "IcosahedronGeometry",
    "params": ["radius=1", "detail=0"],
    "desc": "20-sided polyhedron. Good base for sphere subdivision.",
  },
  "octahedron": {
    "class": "OctahedronGeometry",
    "params": ["radius=1", "detail=0"],
    "desc": "8-sided polyhedron.",
  },
  "tetrahedron": {
    "class": "TetrahedronGeometry",
    "params": ["radius=1", "detail=0"],
    "desc": "4-sided polyhedron.",
  },
}


@mcp.tool()
def geometry(
  shape: str,
  variable_name: str = "geometry",
  params: dict | None = None,
) -> str:
  """Generate Three.js geometry code. shape must be one of: box, sphere, plane,
  cylinder, cone, torus, torusknot, ring, circle, capsule, dodecahedron,
  icosahedron, octahedron, tetrahedron. Pass params dict to override defaults."""
  shape_lower = shape.lower()
  if shape_lower not in GEOMETRIES:
    available = ", ".join(sorted(GEOMETRIES.keys()))
    return f"Unknown geometry '{shape}'. Available: {available}"

  info = GEOMETRIES[shape_lower]
  if params:
    args = ", ".join(str(params.get(p.split("=")[0], p.split("=")[1])) for p in info["params"])
  else:
    args = ", ".join(p.split("=")[1] for p in info["params"])

  return f"""// {info['desc']}
const {variable_name} = new THREE.{info['class']}({args});"""


@mcp.tool()
def extrude_geometry(
  shape_code: str = "",
  depth: float = 1,
  bevel_enabled: bool = True,
  bevel_thickness: float = 0.2,
  bevel_size: float = 0.1,
  bevel_segments: int = 3,
  variable_name: str = "geometry",
) -> str:
  """Generate Three.js ExtrudeGeometry from a 2D Shape. Extrudes a 2D path
  into 3D. Provide shape_code as a THREE.Shape definition, or leave empty
  for an example heart shape."""
  if not shape_code:
    shape_code = """// Example: heart shape
const shape = new THREE.Shape();
shape.moveTo(0, 0);
shape.bezierCurveTo(0, -0.5, -1, -1.5, -2, -1.5);
shape.bezierCurveTo(-4, -1.5, -4, 1, -4, 1);
shape.bezierCurveTo(-4, 3, -2, 4.5, 0, 6);
shape.bezierCurveTo(2, 4.5, 4, 3, 4, 1);
shape.bezierCurveTo(4, 1, 4, -1.5, 2, -1.5);
shape.bezierCurveTo(1, -1.5, 0, -0.5, 0, 0);"""

  return f"""{shape_code}

const extrudeSettings = {{
  depth: {depth},
  bevelEnabled: {str(bevel_enabled).lower()},
  bevelThickness: {bevel_thickness},
  bevelSize: {bevel_size},
  bevelSegments: {bevel_segments},
}};

const {variable_name} = new THREE.ExtrudeGeometry(shape, extrudeSettings);"""


@mcp.tool()
def lathe_geometry(
  points_code: str = "",
  segments: int = 32,
  phi_start: float = 0,
  phi_length: float = 6.283185307,
  variable_name: str = "geometry",
) -> str:
  """Generate Three.js LatheGeometry — creates a surface of revolution by
  rotating a set of 2D points around the Y axis. Good for vases, bottles,
  goblets, and other rotationally symmetric shapes."""
  if not points_code:
    points_code = """// Example: vase profile
const points = [
  new THREE.Vector2(0, 0),
  new THREE.Vector2(1, 0.5),
  new THREE.Vector2(0.8, 1),
  new THREE.Vector2(1.2, 2),
  new THREE.Vector2(0.6, 3),
];"""

  return f"""{points_code}

const {variable_name} = new THREE.LatheGeometry(points, {segments}, {phi_start}, {phi_length});"""


@mcp.tool()
def tube_geometry(
  curve_code: str = "",
  tubular_segments: int = 64,
  radius: float = 0.2,
  radial_segments: int = 8,
  closed: bool = False,
  variable_name: str = "geometry",
) -> str:
  """Generate Three.js TubeGeometry — extrudes a tube along a 3D curve.
  Provide curve_code as a THREE.Curve definition, or leave empty for
  an example CatmullRomCurve3."""
  if not curve_code:
    curve_code = """const curve = new THREE.CatmullRomCurve3([
  new THREE.Vector3(-2, 0, 0),
  new THREE.Vector3(-1, 1, 1),
  new THREE.Vector3(1, -1, 1),
  new THREE.Vector3(2, 0, 0),
]);"""

  return f"""{curve_code}

const {variable_name} = new THREE.TubeGeometry(curve, {tubular_segments}, {radius}, {radial_segments}, {str(closed).lower()});"""


# ---------------------------------------------------------------------------
# Materials
# ---------------------------------------------------------------------------

MATERIALS = {
  "standard": {
    "class": "MeshStandardMaterial",
    "desc": "PBR metallic-roughness workflow. Best balance of quality and performance.",
    "key_props": ["color", "metalness", "roughness", "map", "normalMap", "envMap", "emissive", "emissiveIntensity", "aoMap", "displacementMap", "wireframe", "flatShading", "side", "transparent", "opacity"],
  },
  "physical": {
    "class": "MeshPhysicalMaterial",
    "desc": "Extended PBR with clearcoat, transmission, sheen, iridescence. Use for glass, car paint, fabric.",
    "key_props": ["color", "metalness", "roughness", "clearcoat", "clearcoatRoughness", "transmission", "ior", "thickness", "sheen", "sheenRoughness", "sheenColor", "iridescence", "iridescenceIOR", "specularIntensity", "specularColor", "attenuationColor", "attenuationDistance"],
  },
  "basic": {
    "class": "MeshBasicMaterial",
    "desc": "Unlit material — not affected by lights. Use for UI elements, wireframes, or flat-shaded looks.",
    "key_props": ["color", "map", "wireframe", "transparent", "opacity", "side", "envMap", "combine", "reflectivity"],
  },
  "lambert": {
    "class": "MeshLambertMaterial",
    "desc": "Non-shiny diffuse material using Lambertian reflectance. Cheap lighting.",
    "key_props": ["color", "emissive", "map", "transparent", "opacity", "side", "wireframe"],
  },
  "phong": {
    "class": "MeshPhongMaterial",
    "desc": "Blinn-Phong shading with specular highlights. Good for shiny non-PBR surfaces.",
    "key_props": ["color", "emissive", "specular", "shininess", "map", "normalMap", "transparent", "opacity", "side", "wireframe", "flatShading"],
  },
  "toon": {
    "class": "MeshToonMaterial",
    "desc": "Cel-shaded/cartoon look with discrete shading steps.",
    "key_props": ["color", "map", "gradientMap", "emissive", "transparent", "opacity", "side"],
  },
  "normal": {
    "class": "MeshNormalMaterial",
    "desc": "Maps normal vectors to RGB colors. Useful for debugging normals.",
    "key_props": ["wireframe", "flatShading", "side", "transparent", "opacity"],
  },
  "depth": {
    "class": "MeshDepthMaterial",
    "desc": "Draws geometry by depth. Near=white, far=black. Used in shadow maps and effects.",
    "key_props": ["wireframe", "side"],
  },
  "matcap": {
    "class": "MeshMatcapMaterial",
    "desc": "Material capture — uses a matcap texture for lighting. No lights needed.",
    "key_props": ["color", "matcap", "map", "normalMap", "transparent", "opacity", "side", "flatShading"],
  },
  "line_basic": {
    "class": "LineBasicMaterial",
    "desc": "Basic line material with uniform color.",
    "key_props": ["color", "linewidth", "transparent", "opacity"],
  },
  "line_dashed": {
    "class": "LineDashedMaterial",
    "desc": "Dashed line material. Call line.computeLineDistances() after creation.",
    "key_props": ["color", "linewidth", "dashSize", "gapSize", "scale", "transparent", "opacity"],
  },
  "points": {
    "class": "PointsMaterial",
    "desc": "Material for THREE.Points particle systems.",
    "key_props": ["color", "size", "sizeAttenuation", "map", "transparent", "opacity"],
  },
  "sprite": {
    "class": "SpriteMaterial",
    "desc": "Material for THREE.Sprite — always faces camera.",
    "key_props": ["color", "map", "rotation", "transparent", "opacity", "sizeAttenuation"],
  },
  "shadow": {
    "class": "ShadowMaterial",
    "desc": "Receives shadows but is otherwise invisible. Use for ground planes.",
    "key_props": ["color", "transparent", "opacity"],
  },
}


@mcp.tool()
def material(
  type: str,
  variable_name: str = "material",
  props: dict | None = None,
) -> str:
  """Generate Three.js material code. type must be one of: standard, physical,
  basic, lambert, phong, toon, normal, depth, matcap, line_basic, line_dashed,
  points, sprite, shadow. Pass props dict to set material properties."""
  type_lower = type.lower()
  if type_lower not in MATERIALS:
    available = ", ".join(sorted(MATERIALS.keys()))
    return f"Unknown material type '{type}'. Available: {available}"

  info = MATERIALS[type_lower]
  if props:
    prop_lines = []
    for k, v in props.items():
      if isinstance(v, str) and not v.startswith("new ") and not v.startswith("THREE."):
        prop_lines.append(f"  {k}: '{v}',")
      else:
        prop_lines.append(f"  {k}: {v},")
    props_str = "\n".join(prop_lines)
    return f"""// {info['desc']}
// Key properties: {', '.join(info['key_props'])}
const {variable_name} = new THREE.{info['class']}({{
{props_str}
}});"""
  else:
    return f"""// {info['desc']}
// Key properties: {', '.join(info['key_props'])}
const {variable_name} = new THREE.{info['class']}();"""


@mcp.tool()
def shader_material(
  vertex_shader: str = "",
  fragment_shader: str = "",
  uniforms: dict | None = None,
  transparent: bool = False,
  variable_name: str = "material",
) -> str:
  """Generate a Three.js ShaderMaterial with custom GLSL vertex and fragment
  shaders. Use for fully custom rendering effects."""
  if not vertex_shader:
    vertex_shader = """void main() {
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}"""
  if not fragment_shader:
    fragment_shader = """void main() {
  gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}"""

  uniform_lines = ""
  if uniforms:
    entries = []
    for k, v in uniforms.items():
      # v is already a raw value (e.g. 0, "new THREE.Vector2()")
      # Wrap it directly — don't nest {value: ...} inside another {value: ...}
      if isinstance(v, dict) and "value" in v:
        raw = v["value"]
      else:
        raw = v
      entries.append(f"    {k}: {{ value: {raw} }},")
    uniform_lines = "\n".join(entries)
    uniform_lines = f"\n  uniforms: {{\n{uniform_lines}\n  }},"

  return f"""const {variable_name} = new THREE.ShaderMaterial({{
  vertexShader: `{vertex_shader}`,
  fragmentShader: `{fragment_shader}`,{uniform_lines}
  transparent: {str(transparent).lower()},
}});"""


# ---------------------------------------------------------------------------
# Mesh & Object Creation
# ---------------------------------------------------------------------------

@mcp.tool()
def mesh(
  geometry_code: str,
  material_code: str,
  variable_name: str = "mesh",
  position: list[float] | None = None,
  rotation: list[float] | None = None,
  scale: list[float] | None = None,
  cast_shadow: bool = True,
  receive_shadow: bool = True,
) -> str:
  """Generate a Three.js Mesh by combining geometry and material code.
  Optionally set position, rotation (in radians), scale, and shadow properties.
  Adds the mesh to the scene."""
  pos = position or [0, 0, 0]
  rot = rotation or [0, 0, 0]
  scl = scale or [1, 1, 1]

  scale_line = ""
  if scl != [1, 1, 1]:
    scale_line = f"\n{variable_name}.scale.set({scl[0]}, {scl[1]}, {scl[2]});"

  rot_line = ""
  if rot != [0, 0, 0]:
    rot_line = f"\n{variable_name}.rotation.set({rot[0]}, {rot[1]}, {rot[2]});"

  # Extract variable names from the geometry and material code
  # Look for "const <varName> =" pattern
  import re
  geo_match = re.search(r'const\s+(\w+)\s*=', geometry_code)
  mat_match = re.search(r'const\s+(\w+)\s*=', material_code)
  geo_var = geo_match.group(1) if geo_match else "geometry"
  mat_var = mat_match.group(1) if mat_match else "material"

  return f"""{geometry_code}

{material_code}

const {variable_name} = new THREE.Mesh({geo_var}, {mat_var});
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});{rot_line}{scale_line}
{variable_name}.castShadow = {str(cast_shadow).lower()};
{variable_name}.receiveShadow = {str(receive_shadow).lower()};
scene.add({variable_name});"""


@mcp.tool()
def instanced_mesh(
  geometry_var: str = "geometry",
  material_var: str = "material",
  count: int = 1000,
  variable_name: str = "instancedMesh",
  randomize: bool = True,
  spread: float = 50,
) -> str:
  """Generate Three.js InstancedMesh for rendering many copies of the same
  geometry efficiently. Use for forests, particles, crowds, etc."""
  randomize_code = ""
  if randomize:
    randomize_code = f"""
const dummy = new THREE.Object3D();
for (let i = 0; i < {count}; i++) {{
  dummy.position.set(
    (Math.random() - 0.5) * {spread},
    (Math.random() - 0.5) * {spread},
    (Math.random() - 0.5) * {spread}
  );
  dummy.rotation.set(
    Math.random() * Math.PI * 2,
    Math.random() * Math.PI * 2,
    Math.random() * Math.PI * 2
  );
  const s = 0.5 + Math.random() * 0.5;
  dummy.scale.set(s, s, s);
  dummy.updateMatrix();
  {variable_name}.setMatrixAt(i, dummy.matrix);
}}
{variable_name}.instanceMatrix.needsUpdate = true;"""

  return f"""const {variable_name} = new THREE.InstancedMesh({geometry_var}, {material_var}, {count});
{variable_name}.castShadow = true;
{variable_name}.receiveShadow = true;
scene.add({variable_name});{randomize_code}"""


@mcp.tool()
def group(
  variable_name: str = "group",
  children: list[str] | None = None,
  position: list[float] | None = None,
  rotation: list[float] | None = None,
) -> str:
  """Generate a Three.js Group to organize multiple objects together.
  Groups share transformations with their children."""
  pos = position or [0, 0, 0]
  rot = rotation or [0, 0, 0]

  child_lines = ""
  if children:
    child_lines = "\n".join(f"{variable_name}.add({c});" for c in children)
    child_lines = f"\n{child_lines}"

  rot_line = ""
  if rot != [0, 0, 0]:
    rot_line = f"\n{variable_name}.rotation.set({rot[0]}, {rot[1]}, {rot[2]});"

  return f"""const {variable_name} = new THREE.Group();
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});{rot_line}{child_lines}
scene.add({variable_name});"""


# ---------------------------------------------------------------------------
# Lights
# ---------------------------------------------------------------------------

@mcp.tool()
def ambient_light(
  color: str = "#ffffff",
  intensity: float = 0.5,
  variable_name: str = "ambientLight",
) -> str:
  """Generate a Three.js AmbientLight. Illuminates all objects equally from
  all directions. Use as base fill lighting — does not cast shadows."""
  return f"""const {variable_name} = new THREE.AmbientLight('{color}', {intensity});
scene.add({variable_name});"""


@mcp.tool()
def directional_light(
  color: str = "#ffffff",
  intensity: float = 1.0,
  position: list[float] | None = None,
  target: list[float] | None = None,
  cast_shadow: bool = True,
  shadow_map_size: int = 2048,
  shadow_camera_size: float = 10,
  variable_name: str = "directionalLight",
) -> str:
  """Generate a Three.js DirectionalLight. Parallel light rays like the sun.
  Use as primary scene lighting. Casts shadows."""
  pos = position or [5, 10, 5]
  tgt = target or [0, 0, 0]

  shadow_code = ""
  if cast_shadow:
    shadow_code = f"""
{variable_name}.castShadow = true;
{variable_name}.shadow.mapSize.width = {shadow_map_size};
{variable_name}.shadow.mapSize.height = {shadow_map_size};
{variable_name}.shadow.camera.near = 0.1;
{variable_name}.shadow.camera.far = 50;
{variable_name}.shadow.camera.left = -{shadow_camera_size};
{variable_name}.shadow.camera.right = {shadow_camera_size};
{variable_name}.shadow.camera.top = {shadow_camera_size};
{variable_name}.shadow.camera.bottom = -{shadow_camera_size};"""

  return f"""const {variable_name} = new THREE.DirectionalLight('{color}', {intensity});
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});
{variable_name}.target.position.set({tgt[0]}, {tgt[1]}, {tgt[2]});{shadow_code}
scene.add({variable_name});"""


@mcp.tool()
def point_light(
  color: str = "#ffffff",
  intensity: float = 1.0,
  distance: float = 0,
  decay: float = 2,
  position: list[float] | None = None,
  cast_shadow: bool = True,
  variable_name: str = "pointLight",
) -> str:
  """Generate a Three.js PointLight. Emits light in all directions from a
  single point, like a light bulb. Intensity diminishes with distance."""
  pos = position or [0, 5, 0]

  shadow_code = ""
  if cast_shadow:
    shadow_code = f"\n{variable_name}.castShadow = true;"

  return f"""const {variable_name} = new THREE.PointLight('{color}', {intensity}, {distance}, {decay});
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});{shadow_code}
scene.add({variable_name});"""


@mcp.tool()
def spot_light(
  color: str = "#ffffff",
  intensity: float = 1.0,
  distance: float = 0,
  angle: float = 0.5236,
  penumbra: float = 0.5,
  decay: float = 2,
  position: list[float] | None = None,
  target: list[float] | None = None,
  cast_shadow: bool = True,
  shadow_map_size: int = 2048,
  variable_name: str = "spotLight",
) -> str:
  """Generate a Three.js SpotLight. Cone-shaped light like a flashlight or
  stage spotlight. Has angle and penumbra (soft edge) controls."""
  pos = position or [0, 10, 0]
  tgt = target or [0, 0, 0]

  shadow_code = ""
  if cast_shadow:
    shadow_code = f"""
{variable_name}.castShadow = true;
{variable_name}.shadow.mapSize.width = {shadow_map_size};
{variable_name}.shadow.mapSize.height = {shadow_map_size};"""

  return f"""const {variable_name} = new THREE.SpotLight('{color}', {intensity}, {distance}, {angle}, {penumbra}, {decay});
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});
{variable_name}.target.position.set({tgt[0]}, {tgt[1]}, {tgt[2]});{shadow_code}
scene.add({variable_name});"""


@mcp.tool()
def hemisphere_light(
  sky_color: str = "#87ceeb",
  ground_color: str = "#362907",
  intensity: float = 0.6,
  variable_name: str = "hemisphereLight",
) -> str:
  """Generate a Three.js HemisphereLight. Two-tone ambient light — sky color
  from above, ground color from below. Great for outdoor scenes."""
  return f"""const {variable_name} = new THREE.HemisphereLight('{sky_color}', '{ground_color}', {intensity});
scene.add({variable_name});"""


@mcp.tool()
def rect_area_light(
  color: str = "#ffffff",
  intensity: float = 5.0,
  width: float = 4,
  height: float = 4,
  position: list[float] | None = None,
  look_at: list[float] | None = None,
  variable_name: str = "rectLight",
) -> str:
  """Generate a Three.js RectAreaLight (addon). Rectangular area light like a
  window or studio softbox. Requires RectAreaLightUniformsLib. Does NOT cast shadows."""
  pos = position or [0, 5, -5]
  look = look_at or [0, 0, 0]

  return f"""import {{ RectAreaLightHelper }} from 'three/addons/helpers/RectAreaLightHelper.js';
import {{ RectAreaLightUniformsLib }} from 'three/addons/lights/RectAreaLightUniformsLib.js';

RectAreaLightUniformsLib.init();
const {variable_name} = new THREE.RectAreaLight('{color}', {intensity}, {width}, {height});
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});
{variable_name}.lookAt({look[0]}, {look[1]}, {look[2]});
scene.add({variable_name});
scene.add(new RectAreaLightHelper({variable_name}));"""


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------

@mcp.tool()
def orbit_controls(
  camera_var: str = "camera",
  renderer_var: str = "renderer",
  enable_damping: bool = True,
  auto_rotate: bool = False,
  min_distance: float = 1,
  max_distance: float = 100,
  max_polar_angle: float = 3.14159,
  variable_name: str = "controls",
) -> str:
  """Generate Three.js OrbitControls — orbit camera around a target with
  mouse/touch. The most common camera control for 3D viewers. Remember to
  call controls.update() in the animation loop."""
  return f"""import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';

const {variable_name} = new OrbitControls({camera_var}, {renderer_var}.domElement);
{variable_name}.enableDamping = {str(enable_damping).lower()};
{variable_name}.dampingFactor = 0.05;
{variable_name}.autoRotate = {str(auto_rotate).lower()};
{variable_name}.minDistance = {min_distance};
{variable_name}.maxDistance = {max_distance};
{variable_name}.maxPolarAngle = {max_polar_angle};

// Add to animation loop:
// {variable_name}.update();"""


@mcp.tool()
def fly_controls(
  camera_var: str = "camera",
  renderer_var: str = "renderer",
  movement_speed: float = 10,
  roll_speed: float = 0.5,
  variable_name: str = "controls",
) -> str:
  """Generate Three.js FlyControls — free-flight camera movement with
  WASD/arrow keys and mouse. Good for exploration/flight sims."""
  return f"""import {{ FlyControls }} from 'three/addons/controls/FlyControls.js';

const {variable_name} = new FlyControls({camera_var}, {renderer_var}.domElement);
{variable_name}.movementSpeed = {movement_speed};
{variable_name}.rollSpeed = {roll_speed};
{variable_name}.dragToLook = true;

// Add to animation loop (pass delta time):
// {variable_name}.update(delta);"""


@mcp.tool()
def pointer_lock_controls(
  camera_var: str = "camera",
  renderer_var: str = "renderer",
  variable_name: str = "controls",
) -> str:
  """Generate Three.js PointerLockControls — first-person camera with
  pointer lock. Click to capture mouse, ESC to release. Good for FPS games."""
  return f"""import {{ PointerLockControls }} from 'three/addons/controls/PointerLockControls.js';

const {variable_name} = new PointerLockControls({camera_var}, {renderer_var}.domElement);
scene.add({variable_name}.object);

{renderer_var}.domElement.addEventListener('click', () => {{
  {variable_name}.lock();
}});

// Movement (add keyboard handler)
const velocity = new THREE.Vector3();
const direction = new THREE.Vector3();
let moveForward = false, moveBackward = false, moveLeft = false, moveRight = false;

document.addEventListener('keydown', (e) => {{
  switch (e.code) {{
    case 'ArrowUp': case 'KeyW': moveForward = true; break;
    case 'ArrowDown': case 'KeyS': moveBackward = true; break;
    case 'ArrowLeft': case 'KeyA': moveLeft = true; break;
    case 'ArrowRight': case 'KeyD': moveRight = true; break;
  }}
}});
document.addEventListener('keyup', (e) => {{
  switch (e.code) {{
    case 'ArrowUp': case 'KeyW': moveForward = false; break;
    case 'ArrowDown': case 'KeyS': moveBackward = false; break;
    case 'ArrowLeft': case 'KeyA': moveLeft = false; break;
    case 'ArrowRight': case 'KeyD': moveRight = false; break;
  }}
}});

// Add to animation loop:
// if ({variable_name}.isLocked) {{
//   direction.z = Number(moveForward) - Number(moveBackward);
//   direction.x = Number(moveRight) - Number(moveLeft);
//   direction.normalize();
//   {variable_name}.moveRight(direction.x * delta * 10);
//   {variable_name}.moveForward(direction.z * delta * 10);
// }}"""


@mcp.tool()
def transform_controls(
  camera_var: str = "camera",
  renderer_var: str = "renderer",
  target_var: str = "mesh",
  mode: str = "translate",
  variable_name: str = "transformControls",
) -> str:
  """Generate Three.js TransformControls — interactive translate/rotate/scale
  gizmo. mode is 'translate', 'rotate', or 'scale'. Toggle with W/E/R keys."""
  return f"""import {{ TransformControls }} from 'three/addons/controls/TransformControls.js';

const {variable_name} = new TransformControls({camera_var}, {renderer_var}.domElement);
{variable_name}.attach({target_var});
{variable_name}.setMode('{mode}');
scene.add({variable_name}.getHelper());

// Toggle mode with keyboard
window.addEventListener('keydown', (e) => {{
  switch (e.key) {{
    case 'w': {variable_name}.setMode('translate'); break;
    case 'e': {variable_name}.setMode('rotate'); break;
    case 'r': {variable_name}.setMode('scale'); break;
  }}
}});

// Disable OrbitControls while dragging
// {variable_name}.addEventListener('dragging-changed', (e) => {{
//   orbitControls.enabled = !e.value;
// }});"""


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

@mcp.tool()
def gltf_loader(
  url: str = "model.glb",
  variable_name: str = "model",
  draco: bool = False,
  on_progress: bool = False,
) -> str:
  """Generate Three.js GLTFLoader code to load .gltf/.glb models. The most
  common 3D model format. Enable draco for compressed models."""
  draco_import = ""
  draco_setup = ""
  if draco:
    draco_import = "\nimport { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';"
    draco_setup = """
const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.6/');
loader.setDRACOLoader(dracoLoader);"""

  progress_code = ""
  if on_progress:
    progress_code = """
  (progress) => {
    console.log(`Loading: ${(progress.loaded / progress.total * 100).toFixed(1)}%`);
  },"""

  return f"""import {{ GLTFLoader }} from 'three/addons/loaders/GLTFLoader.js';{draco_import}

const loader = new GLTFLoader();{draco_setup}

loader.load(
  '{url}',
  (gltf) => {{
    const {variable_name} = gltf.scene;
    scene.add({variable_name});

    // Optional: play animations
    // const mixer = new THREE.AnimationMixer({variable_name});
    // gltf.animations.forEach((clip) => mixer.clipAction(clip).play());
    // Add to animation loop: mixer.update(delta);
  }},{progress_code}
  undefined,
  (error) => console.error('Error loading model:', error)
);"""


@mcp.tool()
def texture_loader(
  url: str = "texture.jpg",
  variable_name: str = "texture",
  wrap_s: str = "RepeatWrapping",
  wrap_t: str = "RepeatWrapping",
  repeat_x: float = 1,
  repeat_y: float = 1,
  encoding: str = "sRGB",
) -> str:
  """Generate Three.js TextureLoader code. Load image textures for materials
  (diffuse maps, normal maps, etc.)."""
  encoding_code = ""
  if encoding == "sRGB":
    encoding_code = f"\n{variable_name}.colorSpace = THREE.SRGBColorSpace;"

  return f"""const {variable_name} = new THREE.TextureLoader().load('{url}');
{variable_name}.wrapS = THREE.{wrap_s};
{variable_name}.wrapT = THREE.{wrap_t};
{variable_name}.repeat.set({repeat_x}, {repeat_y});{encoding_code}"""


@mcp.tool()
def cube_texture_loader(
  path: str = "textures/cubemap/",
  filenames: list[str] | None = None,
  variable_name: str = "envMap",
) -> str:
  """Generate Three.js CubeTextureLoader code for loading skybox/environment
  cube maps (6 faces: px, nx, py, ny, pz, nz)."""
  files = filenames or ["px.jpg", "nx.jpg", "py.jpg", "ny.jpg", "pz.jpg", "nz.jpg"]
  file_list = ", ".join(f"'{f}'" for f in files)

  return f"""const {variable_name} = new THREE.CubeTextureLoader()
  .setPath('{path}')
  .load([{file_list}]);

// Use as scene background/environment:
// scene.background = {variable_name};
// scene.environment = {variable_name};"""


@mcp.tool()
def hdr_environment(
  url: str = "environment.hdr",
  as_background: bool = True,
  variable_name: str = "envMap",
) -> str:
  """Generate Three.js RGBELoader code to load HDR environment maps for
  physically-based lighting. Sets both scene.environment and optionally
  scene.background."""
  bg_code = ""
  if as_background:
    bg_code = f"\n    scene.background = {variable_name};"

  return f"""import {{ RGBELoader }} from 'three/addons/loaders/RGBELoader.js';

new RGBELoader().load('{url}', ({variable_name}) => {{
  {variable_name}.mapping = THREE.EquirectangularReflectionMapping;
  scene.environment = {variable_name};{bg_code}
}});"""


@mcp.tool()
def fbx_loader(
  url: str = "model.fbx",
  variable_name: str = "model",
) -> str:
  """Generate Three.js FBXLoader code to load .fbx models. Common format
  from Autodesk tools (Maya, 3ds Max, Blender export)."""
  return f"""import {{ FBXLoader }} from 'three/addons/loaders/FBXLoader.js';

const loader = new FBXLoader();
loader.load('{url}', ({variable_name}) => {{
  scene.add({variable_name});

  // Optional: play animations
  // const mixer = new THREE.AnimationMixer({variable_name});
  // {variable_name}.animations.forEach((clip) => mixer.clipAction(clip).play());
}});"""


# ---------------------------------------------------------------------------
# Animation
# ---------------------------------------------------------------------------

@mcp.tool()
def animation_loop(
  use_clock: bool = True,
  updates: list[str] | None = None,
) -> str:
  """Generate a Three.js animation loop with clock-based delta time.
  Provide updates as a list of code strings to run each frame."""
  update_lines = ""
  if updates:
    update_lines = "\n  " + "\n  ".join(updates)

  if use_clock:
    return f"""const clock = new THREE.Clock();

function animate() {{
  requestAnimationFrame(animate);
  const delta = clock.getDelta();
  const elapsed = clock.getElapsedTime();{update_lines}
  renderer.render(scene, camera);
}}
animate();"""
  else:
    return f"""function animate() {{
  requestAnimationFrame(animate);{update_lines}
  renderer.render(scene, camera);
}}
animate();"""


@mcp.tool()
def keyframe_animation(
  target_var: str = "mesh",
  property_path: str = ".position",
  times: list[float] | None = None,
  values: list[float] | None = None,
  loop: str = "LoopRepeat",
  duration: float = 2.0,
  variable_name: str = "mixer",
) -> str:
  """Generate Three.js keyframe animation using AnimationMixer, AnimationClip,
  and KeyframeTrack. Animate any property (position, rotation, scale, etc.)
  over specified keyframe times and values."""
  t = times or [0, 1, 2]
  v = values or [0, 0, 0, 0, 2, 0, 0, 0, 0]
  times_str = ", ".join(str(x) for x in t)
  values_str = ", ".join(str(x) for x in v)

  return f"""const track = new THREE.VectorKeyframeTrack(
  '{property_path}',
  [{times_str}],
  [{values_str}]
);

const clip = new THREE.AnimationClip('animation', {duration}, [track]);
const {variable_name} = new THREE.AnimationMixer({target_var});
const action = {variable_name}.clipAction(clip);
action.setLoop(THREE.{loop});
action.play();

// Add to animation loop:
// {variable_name}.update(delta);"""


@mcp.tool()
def tween_animation() -> str:
  """Generate common Three.js animation patterns without a tween library.
  Shows lerp-based smooth animations for position, rotation, color, and
  opacity — the most-used animation patterns."""
  return """// Smooth position animation (lerp)
const targetPosition = new THREE.Vector3(5, 2, 0);
// In animation loop:
// mesh.position.lerp(targetPosition, 0.05);

// Rotation animation (constant speed)
// In animation loop:
// mesh.rotation.y += delta * 0.5; // radians per second

// Oscillation (sine wave)
// In animation loop:
// mesh.position.y = Math.sin(elapsed * 2) * 0.5;

// Color lerp
const startColor = new THREE.Color('#ff0000');
const endColor = new THREE.Color('#0000ff');
// In animation loop:
// const t = (Math.sin(elapsed) + 1) / 2; // 0-1 oscillation
// mesh.material.color.lerpColors(startColor, endColor, t);

// Opacity fade
// mesh.material.transparent = true;
// In animation loop:
// mesh.material.opacity = THREE.MathUtils.lerp(mesh.material.opacity, targetOpacity, 0.05);

// Scale pulse
// In animation loop:
// const s = 1 + Math.sin(elapsed * 3) * 0.1;
// mesh.scale.set(s, s, s);"""


# ---------------------------------------------------------------------------
# Raycasting & Interaction
# ---------------------------------------------------------------------------

@mcp.tool()
def raycaster(
  camera_var: str = "camera",
  objects_var: str = "scene.children",
  on_click: bool = True,
  on_hover: bool = False,
) -> str:
  """Generate Three.js Raycaster for mouse/touch picking and interaction.
  Detect which 3D objects the user clicks on or hovers over."""
  hover_code = ""
  if on_hover:
    hover_code = f"""
let hoveredObject = null;
window.addEventListener('pointermove', (event) => {{
  pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
  pointer.y = -(event.clientY / window.innerHeight) * 2 + 1;
  raycaster.setFromCamera(pointer, {camera_var});
  const intersects = raycaster.intersectObjects({objects_var});
  if (hoveredObject) {{
    hoveredObject.material.emissive?.setHex(hoveredObject.userData.originalEmissive || 0x000000);
  }}
  if (intersects.length > 0) {{
    hoveredObject = intersects[0].object;
    hoveredObject.userData.originalEmissive = hoveredObject.material.emissive?.getHex();
    hoveredObject.material.emissive?.setHex(0x333333);
    document.body.style.cursor = 'pointer';
  }} else {{
    hoveredObject = null;
    document.body.style.cursor = 'default';
  }}
}});"""

  click_code = ""
  if on_click:
    click_code = f"""
window.addEventListener('click', (event) => {{
  pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
  pointer.y = -(event.clientY / window.innerHeight) * 2 + 1;
  raycaster.setFromCamera(pointer, {camera_var});
  const intersects = raycaster.intersectObjects({objects_var});
  if (intersects.length > 0) {{
    const clicked = intersects[0].object;
    console.log('Clicked:', clicked.name || clicked.uuid);
    // Handle click interaction here
  }}
}});"""

  return f"""const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();{click_code}{hover_code}"""


# ---------------------------------------------------------------------------
# Helpers & Debug
# ---------------------------------------------------------------------------

@mcp.tool()
def debug_helpers(
  axes: bool = True,
  axes_size: float = 5,
  grid: bool = True,
  grid_size: float = 20,
  grid_divisions: int = 20,
  stats: bool = True,
) -> str:
  """Generate Three.js debug helpers: AxesHelper (RGB=XYZ), GridHelper,
  and Stats.js FPS counter. Essential for development."""
  lines = []

  if axes:
    lines.append(f"scene.add(new THREE.AxesHelper({axes_size}));")

  if grid:
    lines.append(f"scene.add(new THREE.GridHelper({grid_size}, {grid_divisions}));")

  if stats:
    lines.append("""
import Stats from 'three/addons/libs/stats.module.js';
const stats = new Stats();
document.body.appendChild(stats.dom);
// Add to animation loop: stats.update();""")

  return "\n".join(lines)


@mcp.tool()
def light_helpers(
  light_var: str = "directionalLight",
  light_type: str = "directional",
  size: float = 1,
) -> str:
  """Generate Three.js light visualization helpers for debugging light
  placement. Shows light direction, area, and shadow camera frustum."""
  helpers = {
    "directional": f"""const helper = new THREE.DirectionalLightHelper({light_var}, {size});
scene.add(helper);
const shadowHelper = new THREE.CameraHelper({light_var}.shadow.camera);
scene.add(shadowHelper);""",
    "spot": f"""const helper = new THREE.SpotLightHelper({light_var});
scene.add(helper);
const shadowHelper = new THREE.CameraHelper({light_var}.shadow.camera);
scene.add(shadowHelper);""",
    "point": f"""const helper = new THREE.PointLightHelper({light_var}, {size});
scene.add(helper);""",
    "hemisphere": f"""const helper = new THREE.HemisphereLightHelper({light_var}, {size});
scene.add(helper);""",
  }
  return helpers.get(light_type, f"// No helper available for '{light_type}' light type")


# ---------------------------------------------------------------------------
# Postprocessing
# ---------------------------------------------------------------------------

@mcp.tool()
def postprocessing_setup(
  effects: list[str] | None = None,
  renderer_var: str = "renderer",
  scene_var: str = "scene",
  camera_var: str = "camera",
) -> str:
  """Generate Three.js postprocessing pipeline setup. Available effects:
  bloom, ssao, fxaa, smaa, outline, film, glitch, dot_screen, halftone,
  unreal_bloom, bokeh, ssr. Combine multiple effects in the effects list."""
  fx = effects or ["bloom"]

  imports = [
    "import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';",
    "import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';",
  ]
  passes = [
    f"const composer = new EffectComposer({renderer_var});",
    f"composer.addPass(new RenderPass({scene_var}, {camera_var}));",
  ]

  effect_configs = {
    "bloom": {
      "import": "import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';",
      "code": """const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  0.5,  // strength
  0.4,  // radius
  0.85  // threshold
);
composer.addPass(bloomPass);""",
    },
    "unreal_bloom": {
      "import": "import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';",
      "code": """const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5,  // strength
  0.4,  // radius
  0.85  // threshold
);
composer.addPass(bloomPass);""",
    },
    "ssao": {
      "import": "import { SSAOPass } from 'three/addons/postprocessing/SSAOPass.js';",
      "code": f"""const ssaoPass = new SSAOPass({scene_var}, {camera_var}, window.innerWidth, window.innerHeight);
ssaoPass.kernelRadius = 16;
ssaoPass.minDistance = 0.005;
ssaoPass.maxDistance = 0.1;
composer.addPass(ssaoPass);""",
    },
    "fxaa": {
      "import": "import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';\nimport { FXAAShader } from 'three/addons/shaders/FXAAShader.js';",
      "code": """const fxaaPass = new ShaderPass(FXAAShader);
fxaaPass.uniforms['resolution'].value.set(1 / window.innerWidth, 1 / window.innerHeight);
composer.addPass(fxaaPass);""",
    },
    "smaa": {
      "import": "import { SMAAPass } from 'three/addons/postprocessing/SMAAPass.js';",
      "code": "const smaaPass = new SMAAPass(window.innerWidth, window.innerHeight);\ncomposer.addPass(smaaPass);",
    },
    "film": {
      "import": "import { FilmPass } from 'three/addons/postprocessing/FilmPass.js';",
      "code": "const filmPass = new FilmPass(0.35, false);\ncomposer.addPass(filmPass);",
    },
    "glitch": {
      "import": "import { GlitchPass } from 'three/addons/postprocessing/GlitchPass.js';",
      "code": "const glitchPass = new GlitchPass();\ncomposer.addPass(glitchPass);",
    },
    "dot_screen": {
      "import": "import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';\nimport { DotScreenShader } from 'three/addons/shaders/DotScreenShader.js';",
      "code": "const dotScreenPass = new ShaderPass(DotScreenShader);\ndotScreenPass.uniforms['scale'].value = 4;\ncomposer.addPass(dotScreenPass);",
    },
    "halftone": {
      "import": "import { HalftonePass } from 'three/addons/postprocessing/HalftonePass.js';",
      "code": "const halftonePass = new HalftonePass(window.innerWidth, window.innerHeight, { radius: 4, shape: 1 });\ncomposer.addPass(halftonePass);",
    },
    "outline": {
      "import": "import { OutlinePass } from 'three/addons/postprocessing/OutlinePass.js';",
      "code": f"""const outlinePass = new OutlinePass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  {scene_var},
  {camera_var}
);
outlinePass.edgeStrength = 3;
outlinePass.edgeGlow = 0;
outlinePass.edgeThickness = 1;
outlinePass.visibleEdgeColor.set('#ffffff');
// outlinePass.selectedObjects = [mesh];
composer.addPass(outlinePass);""",
    },
    "bokeh": {
      "import": "import { BokehPass } from 'three/addons/postprocessing/BokehPass.js';",
      "code": f"""const bokehPass = new BokehPass({scene_var}, {camera_var}, {{
  focus: 10,
  aperture: 0.025,
  maxblur: 0.01,
}});
composer.addPass(bokehPass);""",
    },
    "ssr": {
      "import": "import { SSRPass } from 'three/addons/postprocessing/SSRPass.js';",
      "code": f"""const ssrPass = new SSRPass({{
  renderer: {renderer_var},
  scene: {scene_var},
  camera: {camera_var},
  width: window.innerWidth,
  height: window.innerHeight,
}});
composer.addPass(ssrPass);""",
    },
  }

  for effect in fx:
    effect_lower = effect.lower()
    if effect_lower in effect_configs:
      cfg = effect_configs[effect_lower]
      imports.append(cfg["import"])
      passes.append(cfg["code"])
    else:
      passes.append(f"// Unknown effect: {effect}")

  return "\n".join(imports) + "\n\n" + "\n\n".join(passes) + """

// Replace renderer.render(scene, camera) with:
// composer.render();"""


# ---------------------------------------------------------------------------
# CSS2D/CSS3D Renderers
# ---------------------------------------------------------------------------

@mcp.tool()
def css2d_label(
  text: str = "Label",
  class_name: str = "label",
  attach_to: str = "mesh",
  offset_y: float = 1.5,
  renderer_var: str = "renderer",
) -> str:
  """Generate Three.js CSS2DRenderer labels — HTML elements positioned in 3D
  space. Use for tooltips, name tags, health bars, annotations."""
  return f"""import {{ CSS2DRenderer, CSS2DObject }} from 'three/addons/renderers/CSS2DRenderer.js';

// CSS2D renderer (add once)
const labelRenderer = new CSS2DRenderer();
labelRenderer.setSize(window.innerWidth, window.innerHeight);
labelRenderer.domElement.style.position = 'absolute';
labelRenderer.domElement.style.top = '0px';
labelRenderer.domElement.style.pointerEvents = 'none';
document.body.appendChild(labelRenderer.domElement);

// Create label
const div = document.createElement('div');
div.className = '{class_name}';
div.textContent = '{text}';
div.style.color = 'white';
div.style.fontSize = '14px';
div.style.padding = '2px 6px';
div.style.background = 'rgba(0, 0, 0, 0.6)';
div.style.borderRadius = '4px';
const label = new CSS2DObject(div);
label.position.set(0, {offset_y}, 0);
{attach_to}.add(label);

// Add to resize handler:
// labelRenderer.setSize(window.innerWidth, window.innerHeight);
// Add to animation loop:
// labelRenderer.render(scene, camera);"""


# ---------------------------------------------------------------------------
# Physics
# ---------------------------------------------------------------------------

@mcp.tool()
def rapier_physics(
  gravity_y: float = -9.81,
) -> str:
  """Generate Three.js + Rapier3D physics setup. Rapier is a fast WASM-based
  physics engine. Shows world creation, rigid body, and collider setup."""
  return f"""import RAPIER from 'https://cdn.skypack.dev/@dimforge/rapier3d-compat';

await RAPIER.init();

const world = new RAPIER.World({{ x: 0, y: {gravity_y}, z: 0 }});

// Create a dynamic rigid body (falling box)
const bodyDesc = RAPIER.RigidBodyDesc.dynamic().setTranslation(0, 5, 0);
const rigidBody = world.createRigidBody(bodyDesc);
const colliderDesc = RAPIER.ColliderDesc.cuboid(0.5, 0.5, 0.5);
world.createCollider(colliderDesc, rigidBody);

// Create a fixed ground plane
const groundDesc = RAPIER.RigidBodyDesc.fixed().setTranslation(0, -0.5, 0);
const groundBody = world.createRigidBody(groundDesc);
const groundCollider = RAPIER.ColliderDesc.cuboid(50, 0.5, 50);
world.createCollider(groundCollider, groundBody);

// In animation loop:
// world.step();
// const position = rigidBody.translation();
// mesh.position.set(position.x, position.y, position.z);
// const rotation = rigidBody.rotation();
// mesh.quaternion.set(rotation.x, rotation.y, rotation.z, rotation.w);"""


# ---------------------------------------------------------------------------
# Common Patterns & Recipes
# ---------------------------------------------------------------------------

@mcp.tool()
def ground_plane(
  size: float = 100,
  color: str = "#808080",
  receive_shadow: bool = True,
  variable_name: str = "ground",
) -> str:
  """Generate a ground plane mesh. Common base element for most scenes.
  Automatically rotated to lie flat on XZ plane."""
  return f"""const {variable_name} = new THREE.Mesh(
  new THREE.PlaneGeometry({size}, {size}),
  new THREE.MeshStandardMaterial({{ color: '{color}' }})
);
{variable_name}.rotation.x = -Math.PI / 2;
{variable_name}.receiveShadow = {str(receive_shadow).lower()};
scene.add({variable_name});"""


@mcp.tool()
def skybox(
  type: str = "color",
  color: str = "#87ceeb",
  texture_path: str = "textures/cubemap/",
) -> str:
  """Generate a skybox/background for the scene. type is 'color', 'gradient',
  'cubemap', or 'procedural'. Use 'procedural' for a dynamic sky with sun."""
  if type == "color":
    return f"scene.background = new THREE.Color('{color}');"
  elif type == "gradient":
    return f"""// Gradient background using a canvas texture
const canvas = document.createElement('canvas');
canvas.width = 2;
canvas.height = 256;
const ctx = canvas.getContext('2d');
const gradient = ctx.createLinearGradient(0, 0, 0, 256);
gradient.addColorStop(0, '#1e3a5f');
gradient.addColorStop(0.5, '#87ceeb');
gradient.addColorStop(1, '#f0e68c');
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, 2, 256);
const bgTexture = new THREE.CanvasTexture(canvas);
scene.background = bgTexture;"""
  elif type == "cubemap":
    return f"""const cubeTextureLoader = new THREE.CubeTextureLoader();
scene.background = cubeTextureLoader
  .setPath('{texture_path}')
  .load(['px.jpg', 'nx.jpg', 'py.jpg', 'ny.jpg', 'pz.jpg', 'nz.jpg']);
scene.environment = scene.background;"""
  elif type == "procedural":
    return """import { Sky } from 'three/addons/objects/Sky.js';

const sky = new Sky();
sky.scale.setScalar(450000);
scene.add(sky);

const sun = new THREE.Vector3();
const uniforms = sky.material.uniforms;
uniforms['turbidity'].value = 10;
uniforms['rayleigh'].value = 3;
uniforms['mieCoefficient'].value = 0.005;
uniforms['mieDirectionalG'].value = 0.7;

const phi = THREE.MathUtils.degToRad(88);
const theta = THREE.MathUtils.degToRad(180);
sun.setFromSphericalCoords(1, phi, theta);
uniforms['sunPosition'].value.copy(sun);"""
  return f"// Unknown skybox type: {type}"


@mcp.tool()
def water_surface(
  size: float = 100,
  sun_direction: list[float] | None = None,
  variable_name: str = "water",
) -> str:
  """Generate Three.js Water surface (addon). Animated ocean/water plane
  with reflections and wave distortion."""
  sun_dir = sun_direction or [0.7, 0.5, 0.3]

  return f"""import {{ Water }} from 'three/addons/objects/Water.js';

const waterGeometry = new THREE.PlaneGeometry({size}, {size});
const {variable_name} = new Water(waterGeometry, {{
  textureWidth: 512,
  textureHeight: 512,
  waterNormals: new THREE.TextureLoader().load(
    'https://threejs.org/examples/textures/waternormals.jpg',
    (texture) => {{ texture.wrapS = texture.wrapT = THREE.RepeatWrapping; }}
  ),
  sunDirection: new THREE.Vector3({sun_dir[0]}, {sun_dir[1]}, {sun_dir[2]}),
  sunColor: 0xffffff,
  waterColor: 0x001e0f,
  distortionScale: 3.7,
}});
{variable_name}.rotation.x = -Math.PI / 2;
scene.add({variable_name});

// In animation loop:
// {variable_name}.material.uniforms['time'].value += delta;"""


@mcp.tool()
def particles(
  count: int = 1000,
  spread: float = 50,
  size: float = 0.5,
  color: str = "#ffffff",
  texture_url: str = "",
  variable_name: str = "particles",
) -> str:
  """Generate a Three.js particle system using Points and BufferGeometry.
  Creates randomly distributed particles. Use for stars, snow, dust, sparks."""
  texture_code = ""
  if texture_url:
    texture_code = f"\n  map: new THREE.TextureLoader().load('{texture_url}'),"

  return f"""const particleGeometry = new THREE.BufferGeometry();
const positions = new Float32Array({count} * 3);
for (let i = 0; i < {count} * 3; i++) {{
  positions[i] = (Math.random() - 0.5) * {spread};
}}
particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

const particleMaterial = new THREE.PointsMaterial({{
  color: '{color}',
  size: {size},
  sizeAttenuation: true,
  transparent: true,
  opacity: 0.8,{texture_code}
}});

const {variable_name} = new THREE.Points(particleGeometry, particleMaterial);
scene.add({variable_name});

// Animate in loop:
// {variable_name}.rotation.y += delta * 0.05;"""


@mcp.tool()
def reflective_surface(
  geometry_var: str = "geometry",
  color: str = "#888888",
  position: list[float] | None = None,
  variable_name: str = "mirror",
) -> str:
  """Generate a Three.js Reflector (mirror surface). Creates real-time planar
  reflections. Good for floors, walls, water-like surfaces."""
  pos = position or [0, 0, 0]

  return f"""import {{ Reflector }} from 'three/addons/objects/Reflector.js';

const {variable_name} = new Reflector({geometry_var}, {{
  clipBias: 0.003,
  textureWidth: window.innerWidth * window.devicePixelRatio,
  textureHeight: window.innerHeight * window.devicePixelRatio,
  color: '{color}',
}});
{variable_name}.position.set({pos[0]}, {pos[1]}, {pos[2]});
scene.add({variable_name});"""


@mcp.tool()
def lensflare(
  light_var: str = "directionalLight",
  texture_url: str = "https://threejs.org/examples/textures/lensflare/lensflare0.png",
) -> str:
  """Generate Three.js Lensflare effect attached to a light source.
  Adds cinematic lens flare sprites that follow the light position."""
  return f"""import {{ Lensflare, LensflareElement }} from 'three/addons/objects/Lensflare.js';

const textureLoader = new THREE.TextureLoader();
const textureFlare = textureLoader.load('{texture_url}');

const lensflare = new Lensflare();
lensflare.addElement(new LensflareElement(textureFlare, 700, 0));
lensflare.addElement(new LensflareElement(textureFlare, 300, 0.6));
lensflare.addElement(new LensflareElement(textureFlare, 150, 0.9));
{light_var}.add(lensflare);"""


# ---------------------------------------------------------------------------
# Math Utilities
# ---------------------------------------------------------------------------

@mcp.tool()
def math_utils() -> str:
  """Generate Three.js math utility reference. Covers Vector3, Quaternion,
  Matrix4, Euler, Color, MathUtils — the most-used math operations."""
  return """// === Vector3 ===
const v = new THREE.Vector3(x, y, z);
v.add(other);              // Add vectors
v.sub(other);              // Subtract
v.multiplyScalar(s);       // Scale
v.normalize();             // Unit vector
v.length();                // Magnitude
v.distanceTo(other);       // Distance between points
v.lerp(target, alpha);     // Interpolate (0-1)
v.cross(other);            // Cross product
v.dot(other);              // Dot product
v.applyMatrix4(matrix);    // Transform by matrix
v.applyQuaternion(quat);   // Rotate by quaternion
v.clone();                 // Deep copy

// === Quaternion ===
const q = new THREE.Quaternion();
q.setFromAxisAngle(axis, angle);       // From axis + angle
q.setFromEuler(euler);                 // From Euler angles
q.slerp(target, alpha);               // Spherical interpolation
q.multiply(other);                     // Combine rotations

// === Euler ===
const e = new THREE.Euler(x, y, z, 'XYZ');  // Rotation in radians
// Order matters: 'XYZ', 'YXZ', 'ZXY', etc.

// === Matrix4 ===
const m = new THREE.Matrix4();
m.makeTranslation(x, y, z);
m.makeRotationFromQuaternion(q);
m.makeScale(x, y, z);
m.multiply(other);                     // Combine transforms
m.invert();                            // Inverse transform
m.decompose(position, quaternion, scale);  // Extract components

// === Color ===
const c = new THREE.Color('#ff0000');  // Hex string
const c2 = new THREE.Color(1, 0, 0);  // RGB floats 0-1
c.lerp(other, alpha);                 // Interpolate colors
c.getHSL({ h: 0, s: 0, l: 0 });      // Get HSL values

// === MathUtils ===
THREE.MathUtils.clamp(value, min, max);
THREE.MathUtils.lerp(start, end, alpha);
THREE.MathUtils.mapLinear(x, a1, a2, b1, b2);  // Remap range
THREE.MathUtils.degToRad(degrees);
THREE.MathUtils.radToDeg(radians);
THREE.MathUtils.randFloat(min, max);
THREE.MathUtils.randFloatSpread(range);  // -range/2 to range/2
THREE.MathUtils.smoothstep(x, min, max);"""


# ---------------------------------------------------------------------------
# WebXR
# ---------------------------------------------------------------------------

@mcp.tool()
def webxr_setup(
  mode: str = "vr",
  renderer_var: str = "renderer",
) -> str:
  """Generate Three.js WebXR setup for VR or AR experiences. Adds the
  appropriate enter button and configures the renderer for XR."""
  if mode == "vr":
    return f"""import {{ VRButton }} from 'three/addons/webxr/VRButton.js';

{renderer_var}.xr.enabled = true;
document.body.appendChild(VRButton.createButton({renderer_var}));

// Replace standard animation loop with XR-compatible version:
{renderer_var}.setAnimationLoop((time) => {{
  // Update logic here
  {renderer_var}.render(scene, camera);
}});"""
  else:
    return f"""import {{ ARButton }} from 'three/addons/webxr/ARButton.js';

{renderer_var}.xr.enabled = true;
document.body.appendChild(ARButton.createButton({renderer_var}, {{
  requiredFeatures: ['hit-test'],
}}));

// Replace standard animation loop with XR-compatible version:
{renderer_var}.setAnimationLoop((time, frame) => {{
  // Use frame for AR hit-testing, anchors, etc.
  {renderer_var}.render(scene, camera);
}});"""


# ---------------------------------------------------------------------------
# Dispose / Cleanup
# ---------------------------------------------------------------------------

@mcp.tool()
def dispose_resources(
  object_var: str = "scene",
) -> str:
  """Generate Three.js resource disposal/cleanup code. Properly frees GPU
  memory for geometries, materials, and textures. Essential for SPAs and
  dynamic scenes to prevent memory leaks."""
  return f"""function disposeObject(obj) {{
  if (obj.geometry) obj.geometry.dispose();
  if (obj.material) {{
    if (Array.isArray(obj.material)) {{
      obj.material.forEach((mat) => disposeMaterial(mat));
    }} else {{
      disposeMaterial(obj.material);
    }}
  }}
}}

function disposeMaterial(material) {{
  for (const key of Object.keys(material)) {{
    const value = material[key];
    if (value && typeof value.dispose === 'function') {{
      value.dispose(); // Dispose textures
    }}
  }}
  material.dispose();
}}

// Dispose entire scene
{object_var}.traverse(disposeObject);

// Dispose renderer
// renderer.dispose();
// renderer.forceContextLoss();"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
  mcp.run()
