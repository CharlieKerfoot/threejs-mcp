# BufferGeometryLoader
Extends: Loader→

Class for loading geometries. The files are internally
loaded via FileLoader .

## Constructor
`newBufferGeometryLoader( manager :LoadingManager)`
Constructs a new geometry loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and pass the loaded geometry to the onLoad() callback.
- `.parse( json :Object) :BufferGeometry` — Parses the given JSON object and returns a geometry.

## Source