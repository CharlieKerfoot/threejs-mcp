# FramebufferTexture
Extends: EventDispatcher→Texture→

This class can only be used in combination with copyFramebufferToTexture() methods
of renderers. It extracts the contents of the current bound framebuffer and provides it
as a texture for further usage.

## Constructor
`newFramebufferTexture( width :number, height :number)`
Constructs a new framebuffer texture.

## Properties
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Overwritten and set to false by default. Default is false .
- `.isFramebufferTexture : boolean` — This flag can be used for type testing. Default is true .
- `.magFilter :NearestFilter|NearestMipmapNearestFilter|NearestMipmapLinearFilter|LinearFilter|LinearMipmapNearestFilter|LinearMipmapLinearFilter` — How the texture is sampled when a texel covers more than one pixel. Overwritten and set to NearestFilter by default to disable filtering. Default is NearestFilter .
- `.minFilter :NearestFilter|NearestMipmapNearestFilter|NearestMipmapLinearFilter|LinearFilter|LinearMipmapNearestFilter|LinearMipmapLinearFilter` — How the texture is sampled when a texel covers less than one pixel. Overwritten and set to NearestFilter by default to disable filtering. Default is NearestFilter .

## Source