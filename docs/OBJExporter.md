# OBJExporter

An exporter for OBJ. OBJExporter is not able to export material data into MTL files so only geometry data are supported.

## Constructor
`newOBJExporter()`

## Import

## Methods
- `.parse( object :Object3D) : string` — Parses the given 3D object and generates the OBJ output. If the 3D object is composed of multiple children and geometry, they are merged into a single mesh in the file.

## Source