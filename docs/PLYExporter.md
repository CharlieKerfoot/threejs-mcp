# PLYExporter

An exporter for PLY. PLY (Polygon or Stanford Triangle Format) is a file format for efficient delivery and
loading of simple, static 3D content in a dense format. Both binary and ascii formats are
supported. PLY can store vertex positions, colors, normals and uv coordinates. No textures
or texture references are saved.

## Constructor
`newPLYExporter()`

## Import

## Methods
- `.parse( object :Object3D, onDone :PLYExporter~OnDone, options :PLYExporter~Options) : string | ArrayBuffer` — Parses the given 3D object and generates the PLY output. If the 3D object is composed of multiple children and geometry, they are merged into a single mesh in the file.

## Type Definitions
- `.OnDone( result :string | ArrayBuffer)` — onDone callback of PLYExporter .
- `.Options` — Export options of PLYExporter .

## Source