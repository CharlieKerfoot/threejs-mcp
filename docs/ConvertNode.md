# ConvertNode
Extends: EventDispatcher→Node→

This module is part of the TSL core and usually not used in app level code.
It represents a convert operation during the shader generation process
meaning it converts the data type of a node to a target data type.

## Constructor
`newConvertNode( node :Node, convertTo :string)`
Constructs a new convert node.

## Properties
- `.convertTo : string` — The target node type. Multiple types can be defined by separating them with a | sign.
- `.node :Node` — The node which type should be converted.

## Methods
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the implementation tries to infer the best
matching type from the ConvertNode#convertTo property.

## Source