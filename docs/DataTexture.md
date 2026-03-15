# DataTexture
Extends: EventDispatcher→Texture→

Creates a texture directly from raw buffer data. The interpretation of the data depends on type and format: If the type is UnsignedByteType , a Uint8Array will be useful for addressing the
texel data. If the format is RGBAFormat , data needs four values for
one texel; Red, Green, Blue and Alpha (typically the opacity).

## Constructor
`newDataTexture( data :TypedArray, width :number, height :number, format :number, type :number, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, anisotropy :number, colorSpace :string)`
Constructs a new data texture.

## Properties
- `.flipY : boolean` — If set to true , the texture is flipped along the vertical axis when
uploaded to the GPU. Overwritten and set to false by default. Default is false .
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Overwritten and set to false by default. Default is false .
- `.image : Object` — The image definition of a data texture.
- `.isDataTexture : boolean` — This flag can be used for type testing. Default is true .
- `.unpackAlignment : boolean` — Specifies the alignment requirements for the start of each pixel row in memory. Overwritten and set to 1 by default. Default is 1 .

## Source