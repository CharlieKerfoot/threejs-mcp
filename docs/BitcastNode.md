# BitcastNode
Extends: EventDispatcher→Node→TempNode→

This node represents an operation that reinterprets the bit representation of a value
in one type as a value in another type.

## Constructor
`newBitcastNode( valueNode :Node, conversionType :string, inputType :string)`
Constructs a new bitcast node.

## Properties
- `.conversionType : string` — The type the value will be converted to.
- `.inputType : string` — The expected input data type of the bitcast operation. Default is null .
- `.isBitcastNode : boolean` — This flag can be used for type testing. Default is true .
- `.valueNode :Node` — The data to bitcast to a new type.

## Source