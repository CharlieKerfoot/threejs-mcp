# CompressedTexture
Extends: EventDispatcher→Texture→

Creates a texture based on data in compressed form. These texture are usually loaded with CompressedTextureLoader .

## Constructor
`newCompressedTexture( mipmaps :Array.<Object>, width :number, height :number, format :number, type :number, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, anisotropy :number, colorSpace :string)`
Constructs a new compressed texture.

## Properties
- `.flipY : boolean` — If set to true , the texture is flipped along the vertical axis when
uploaded to the GPU. Overwritten and set to false by default since it is not possible to
flip compressed textures. Default is fa...
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Overwritten and set to false by default since it is not
possible to generate mipmaps for compressed data. Mipmaps
must be embedded in the co...
- `.image : Object` — The image property of a compressed texture just defines its dimensions.
- `.isCompressedTexture : boolean` — This flag can be used for type testing. Default is true .
- `.mipmaps : Array.<Object>` — This array holds for all mipmaps (including the bases mip) the data and dimensions.

## Source