# CompressedTextureLoader
Extends: Loader→

Abstract base class for loading compressed texture formats S3TC, ASTC or ETC.
Textures are internally loaded via FileLoader . Derived classes have to implement the parse() method which holds the parsing
for the respective format.

## Constructor
`newCompressedTextureLoader( manager :LoadingManager)(abstract)`
Constructs a new compressed texture loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :CompressedTexture` — Starts loading from the given URL and passes the loaded compressed texture
to the onLoad() callback. The method also returns a new texture object which can
directly be used for material creation. I...

## Type Definitions
- `.TexData` — Represents the result object type of the parse() method.

## Source