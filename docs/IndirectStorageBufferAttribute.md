# IndirectStorageBufferAttribute
Extends: BufferAttribute→StorageBufferAttribute→

This special type of buffer attribute is intended for compute shaders.
It can be used to encode draw parameters for indirect draw calls. Note: This type of buffer attribute can only be used with WebGPURenderer and a WebGPU backend.

## Constructor
`newIndirectStorageBufferAttribute( count :number | Uint32Array, itemSize :number)`
Constructs a new storage buffer attribute.

## Properties
- `.isIndirectStorageBufferAttribute : boolean` — This flag can be used for type testing. Default is true .

## Source