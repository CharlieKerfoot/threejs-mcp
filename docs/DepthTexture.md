# DepthTexture
Extends: EventDispatcher→Texture→

This class can be used to automatically save the depth information of a
rendering into a texture.

## Constructor
`newDepthTexture( width :number, height :number, type :number, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, anisotropy :number, format :number, depth :number)`
Constructs a new depth texture.

## Properties
- `.compareFunction :NeverCompare|LessCompare|EqualCompare|LessEqualCompare|GreaterCompare|NotEqualCompare|GreaterEqualCompare|AlwaysCompare` — Code corresponding to the depth compare function. Default is null .
- `.flipY : boolean` — If set to true , the texture is flipped along the vertical axis when
uploaded to the GPU. Overwritten and set to false by default. Default is false .
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Overwritten and set to false by default. Default is false .
- `.isDepthTexture : boolean` — This flag can be used for type testing. Default is true .

## Source