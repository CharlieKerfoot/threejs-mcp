# DRACOExporter

An exporter to compress geometry with the Draco library. Draco is an open source library for compressing and
decompressing 3D meshes and point clouds. Compressed geometry can be significantly smaller,
at the cost of additional decoding time on the client device. Standalone Draco files have a .drc extension, and contain vertex positions,
normals, colors, and other attributes. Draco files do not contain materials,
textures, animation, or node hierarchies – to use these features, embed Draco geometry
inside of a glTF file. A normal glTF file can be converted to a Draco-compressed glTF file
using glTF-Pipeline .

## Constructor
`newDRACOExporter()`

## Import

## Properties
- `.MESH_EDGEBREAKER_ENCODING : number` — Edgebreaker encoding. Default is 1 .
- `.MESH_SEQUENTIAL_ENCODING : number` — Sequential encoding. Default is 0 .

## Methods
- `.parse( object :Mesh|Points, options :DRACOExporter~Options) : Int8Array` — Parses the given mesh or point cloud and generates the Draco output.

## Type Definitions
- `.Options` — Export options of DRACOExporter .

## Source