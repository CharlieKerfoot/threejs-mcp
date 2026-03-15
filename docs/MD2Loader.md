# MD2Loader
Extends: Loader→

A loader for the MD2 format. The loader represents the animations of the MD2 asset as an array of animation
clips and stores them in the animations property of the geometry.

## Constructor
`newMD2Loader( manager :LoadingManager)`
Constructs a new MD2 loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded MD2 asset
to the onLoad() callback.
- `.parse( buffer :ArrayBuffer) :BufferGeometry` — Parses the given MD2 data and returns a geometry.

## Source