# InstancedBufferAttribute
Extends: BufferAttribute→

An instanced version of a buffer attribute.

## Constructor
`newInstancedBufferAttribute( array :TypedArray, itemSize :number, normalized :boolean, meshPerAttribute :number)`
Constructs a new instanced buffer attribute.

## Properties
- `.isInstancedBufferAttribute : boolean` — This flag can be used for type testing. Default is true .
- `.meshPerAttribute : number` — Defines how often a value of this buffer attribute should be repeated. A
value of one means that each value of the instanced attribute is used for
a single instance. A value of two means that each ...

## Source