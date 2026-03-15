# VideoTexture
Extends: EventDispatcher→Texture→

A texture for use with a video. Note: When using video textures with WebGPURenderer , Texture#colorSpace must be
set to THREE.SRGBColorSpace. Note: After the initial use of a texture, its dimensions, format, and type
cannot be changed. Instead, call Texture#dispose on the texture and instantiate a new one.

## Constructor
`newVideoTexture( video :HTMLVideoElement, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, format :number, type :number, anisotropy :number)`
Constructs a new video texture.

## Properties
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Overwritten and set to false by default. Default is false .
- `.isVideoTexture : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.update()` — This method is called automatically by the renderer and sets Texture#needsUpdate to true every time a new frame is available. Only relevant if requestVideoFrameCallback is not supported in the brow...

## Source