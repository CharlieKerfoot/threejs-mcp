# StorageTexture
Extends: EventDispatcher→Texture→

This special type of texture is intended for compute shaders.
It can be used to compute the data of a texture with a compute shader. Note: This type of texture can only be used with WebGPURenderer and a WebGPU backend.

## Constructor
`newStorageTexture( width :number, height :number)`
Constructs a new storage texture.

## Properties
- `.image : Object` — The image object which just represents the texture's dimension.
- `.isStorageTexture : boolean` — This flag can be used for type testing. Default is true .
- `.magFilter : number` — The default magFilter for storage textures is THREE.LinearFilter .
- `.minFilter : number` — The default minFilter for storage textures is THREE.LinearFilter .
- `.mipmapsAutoUpdate : boolean` — When true , mipmaps will be auto-generated after compute writes.
When false , mipmaps must be written manually via compute shaders. Default is true .

## Methods
- `.setSize( width :number, height :number)` — Sets the size of the storage texture.

## Source