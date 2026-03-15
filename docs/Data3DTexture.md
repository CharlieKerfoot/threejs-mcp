# Data3DTexture
Extends: EventDispatcher→Texture→

Creates a three-dimensional texture from raw data, with parameters to
divide it into width, height, and depth.

## Constructor
`newData3DTexture( data :TypedArray, width :number, height :number, depth :number)`
Constructs a new data array texture.

## Properties
- `.flipY : boolean` — If set to true , the texture is flipped along the vertical axis when
uploaded to the GPU. Overwritten and set to false by default. Default is false .
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Overwritten and set to false by default. Default is false .
- `.image : Object` — The image definition of a data texture.
- `.isData3DTexture : boolean` — This flag can be used for type testing. Default is true .
- `.magFilter :NearestFilter|NearestMipmapNearestFilter|NearestMipmapLinearFilter|LinearFilter|LinearMipmapNearestFilter|LinearMipmapLinearFilter` — How the texture is sampled when a texel covers more than one pixel. Overwritten and set to NearestFilter by default. Default is NearestFilter .
- `.minFilter :NearestFilter|NearestMipmapNearestFilter|NearestMipmapLinearFilter|LinearFilter|LinearMipmapNearestFilter|LinearMipmapLinearFilter` — How the texture is sampled when a texel covers less than one pixel. Overwritten and set to NearestFilter by default. Default is NearestFilter .
- `.unpackAlignment : boolean` — Specifies the alignment requirements for the start of each pixel row in memory. Overwritten and set to 1 by default. Default is 1 .
- `.wrapR :RepeatWrapping|ClampToEdgeWrapping|MirroredRepeatWrapping` — This defines how the texture is wrapped in the depth and corresponds to W in UVW mapping. Default is ClampToEdgeWrapping .

## Source