# UnpackFloatNode
Extends: EventDispatcher→Node→TempNode→

This node represents an operation that unpacks values from a 32-bit unsigned integer, reinterpreting the results as a floating-point vector

## Constructor
`newUnpackFloatNode( encoding :'snorm' | 'unorm' | 'float16', uintNode :Node)`

## Properties
- `.encoding : string` — The numeric encoding.
- `.isUnpackFloatNode : boolean` — This flag can be used for type testing. Default is true .
- `.uintNode :Node` — The unsigned integer to be unpacked.

## Source