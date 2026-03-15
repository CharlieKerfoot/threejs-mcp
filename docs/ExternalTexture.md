# ExternalTexture
Extends: EventDispatcher→Texture→

Represents a texture created externally with the same renderer context. This may be a texture from a protected media stream, device camera feed,
or other data feeds like a depth sensor. Note that this class is only supported in WebGLRenderer , and in
the WebGPURenderer WebGPU backend.

## Constructor
`newExternalTexture( sourceTexture :WebGLTexture | GPUTexture)`
Creates a new raw texture.

## Properties
- `.isExternalTexture : boolean` — This flag can be used for type testing. Default is true .
- `.sourceTexture : WebGLTexture | GPUTexture` — The external source texture. Default is null .

## Source