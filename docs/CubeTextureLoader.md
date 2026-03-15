# CubeTextureLoader
Extends: Loader→

Class for loading cube textures. Images are internally loaded via ImageLoader . The loader returns an instance of CubeTexture and expects the cube map to
be defined as six separate images representing the sides of a cube. Other cube map definitions
like vertical and horizontal cross, column and row layouts are not supported. Note that, by convention, cube maps are specified in a coordinate system
in which positive-x is to the right when looking up the positive-z axis --
in other words, using a left-handed coordinate system. Since three.js uses
a right-handed coordinate system, environment maps used in three.js will
have pos-x and neg-x swapped. The loaded cube texture is in sRGB color space. Meaning Texture#colorSpace is set to SRGBColorSpace by default.

## Constructor
`newCubeTextureLoader( manager :LoadingManager)`
Constructs a new cube texture loader.

## Methods
- `.load( urls :Array.<string>, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :CubeTexture` — Starts loading from the given URL and pass the fully loaded cube texture
to the onLoad() callback. The method also returns a new cube texture object which can
directly be used for material creation...

## Source