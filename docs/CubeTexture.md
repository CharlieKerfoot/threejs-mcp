# CubeTexture
Extends: EventDispatcher→Texture→

Creates a cube texture made up of six images.

## Constructor
`newCubeTexture( images :Array.<Image>, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, format :number, type :number, anisotropy :number, colorSpace :string)`
Constructs a new cube texture.

## Properties
- `.flipY : boolean` — If set to true , the texture is flipped along the vertical axis when
uploaded to the GPU. Overwritten and set to false by default. Default is false .
- `.images : Array.<Image>` — Alias for CubeTexture#image .
- `.isCubeTexture : boolean` — This flag can be used for type testing. Default is true .

## Source