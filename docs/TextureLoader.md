# TextureLoader
Extends: Loader→

Class for loading textures. Images are internally
loaded via ImageLoader . Please note that TextureLoader has dropped support for progress
events in r84 . For a TextureLoader that supports progress events, see this thread .

## Constructor
`newTextureLoader( manager :LoadingManager)`
Constructs a new texture loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :Texture` — Starts loading from the given URL and pass the fully loaded texture
to the onLoad() callback. The method also returns a new texture object which can
directly be used for material creation. If you d...

## Source