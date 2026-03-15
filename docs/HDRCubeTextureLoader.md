# HDRCubeTextureLoader
Extends: Loader→

A loader for loading HDR cube textures.

## Constructor
`newHDRCubeTextureLoader( manager :LoadingManager)`
Constructs a new HDR cube texture loader.

## Import

## Properties
- `.hdrLoader :HDRLoader` — The internal HDR loader that loads the
individual textures for each cube face.
- `.type :HalfFloatType|FloatType` — The texture type. Default is HalfFloatType .

## Methods
- `.load( urls :Array.<string>, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :CubeTexture` — Starts loading from the given URLs and passes the loaded HDR cube texture
to the onLoad() callback.
- `.setDataType( value :HalfFloatType|FloatType) :HDRCubeTextureLoader` — Sets the texture type.

## Source