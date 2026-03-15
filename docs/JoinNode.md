# JoinNode
Extends: EventDispatcher→Node→TempNode→

This module is part of the TSL core and usually not used in app level code.
It represents a join operation during the shader generation process.
For example in can compose/join two single floats into a vec2 type.

## Constructor
`newJoinNode( nodes :Array.<Node>, nodeType :string)`
Constructs a new join node.

## Properties
- `.nodes : Array.<Node>` — An array of nodes that should be joined.

## Methods
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type must be inferred from the
joined data length if not explicitly defined.

## Source