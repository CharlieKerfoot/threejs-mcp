# Storage3DTexture
Extends: EventDispatcher→Texture→

This special type of texture is intended for compute shaders.
It can be used to compute the data of a texture with a compute shader. Note: This type of texture can only be used with WebGPURenderer and a WebGPU backend.

## Constructor
`newStorage3DTexture( width :number, height :number, depth :number)`
Constructs a new storage texture.

## Properties
- `.image : Object` — The image object which just represents the texture's dimension.
- `.is3DTexture : boolean` — Indicates whether this texture is a 3D texture.
- `.isStorageTexture : boolean` — This flag can be used for type testing. Default is true .
- `.magFilter : number` — The default magFilter for storage textures is THREE.LinearFilter .
- `.minFilter : number` — The default minFilter for storage textures is THREE.LinearFilter .
- `.wrapR : number` — This defines how the texture is wrapped in the depth direction and corresponds to W in UVW mapping.

## Methods
- `.setSize( width :number, height :number, depth :number)` — Sets the size of the storage 3d texture.

## Source