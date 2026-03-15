# PackFloatNode
Extends: EventDispatcher→Node→TempNode→

This node represents an operation that packs floating-point values of a vector into an unsigned 32-bit integer

## Constructor
`newPackFloatNode( encoding :'snorm' | 'unorm' | 'float16', vectorNode :Node)`

## Properties
- `.encoding : string` — The numeric encoding.
- `.isPackFloatNode : boolean` — This flag can be used for type testing. Default is true .
- `.vectorNode :Node` — The vector to be packed.

## Source