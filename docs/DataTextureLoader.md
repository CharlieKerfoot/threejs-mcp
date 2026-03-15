# DataTextureLoader
Extends: Loader→

Abstract base class for loading binary texture formats RGBE, EXR or TGA.
Textures are internally loaded via FileLoader . Derived classes have to implement the parse() method which holds the parsing
for the respective format.

## Constructor
`newDataTextureLoader( manager :LoadingManager)(abstract)`
Constructs a new data texture loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :DataTexture` — Starts loading from the given URL and passes the loaded data texture
to the onLoad() callback. The method also returns a new texture object which can
directly be used for material creation. If you ...

## Type Definitions
- `.TexData` — Represents the result object type of the parse() method.

## Source