# STLExporter

An exporter for STL. STL files describe only the surface geometry of a three-dimensional object without
any representation of color, texture or other common model attributes. The STL format
specifies both ASCII and binary representations, with binary being more compact.
STL files contain no scale information or indexes, and the units are arbitrary.

## Constructor
`newSTLExporter()`

## Import

## Methods
- `.parse( scene :Object3D, options :STLExporter~Options) : string | ArrayBuffer` — Parses the given 3D object and generates the STL output. If the 3D object is composed of multiple children and geometry, they are merged into a single mesh in the file.

## Type Definitions
- `.Options` — Export options of STLExporter .

## Source