# InstancedInterleavedBuffer
Extends: InterleavedBuffer→

An instanced version of an interleaved buffer.

## Constructor
`newInstancedInterleavedBuffer( array :TypedArray, stride :number, meshPerAttribute :number)`
Constructs a new instanced interleaved buffer.

## Properties
- `.isInstancedInterleavedBuffer : boolean` — This flag can be used for type testing. Default is true .
- `.meshPerAttribute : number` — Defines how often a value of this buffer attribute should be repeated,
see InstancedBufferAttribute#meshPerAttribute . Default is 1 .

## Source