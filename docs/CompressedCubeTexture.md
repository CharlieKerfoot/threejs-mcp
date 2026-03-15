# CompressedCubeTexture
Extends: EventDispatcher→Texture→CompressedTexture→

Creates a cube texture based on data in compressed form. These texture are usually loaded with CompressedTextureLoader .

## Constructor
`newCompressedCubeTexture( images :Array.<CompressedTexture>, format :number, type :number)`
Constructs a new compressed texture.

## Properties
- `.isCompressedCubeTexture : boolean` — This flag can be used for type testing. Default is true .
- `.isCubeTexture : boolean` — This flag can be used for type testing. Default is true .

## Source