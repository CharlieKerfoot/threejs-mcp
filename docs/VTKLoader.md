# VTKLoader
Extends: Loader→

A loader for the VTK format. This loader only supports the POLYDATA dataset format so far. Other formats
(structured points, structured grid, rectilinear grid, unstructured grid, appended)
are not supported.

## Constructor
`newVTKLoader( manager :LoadingManager)`
Constructs a new VTK loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded VRML asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :BufferGeometry` — Parses the given VTK data and returns the resulting geometry.

## Source