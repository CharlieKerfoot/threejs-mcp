# StorageBufferAttribute
Extends: BufferAttribute→

This special type of buffer attribute is intended for compute shaders.
In earlier three.js versions it was only possible to update attribute data
on the CPU via JavaScript and then upload the data to the GPU. With the
new material system and renderer it is now possible to use compute shaders
to compute the data for an attribute more efficiently on the GPU. The idea is to create an instance of this class and provide it as an input
to StorageBufferNode . Note: This type of buffer attribute can only be used with WebGPURenderer .

## Constructor
`newStorageBufferAttribute( count :number | TypedArray, itemSize :number, typeClass :TypedArray.constructor)`
Constructs a new storage buffer attribute.

## Properties
- `.isStorageBufferAttribute : boolean` — This flag can be used for type testing. Default is true .

## Source