# RangeNode
Extends: EventDispatcher→Node→

RangeNode generates random instanced attribute data in a defined range.
An exemplary use case for this utility node is to generate random per-instance
colors:

## Constructor
`newRangeNode( minNode :Node.<any>, maxNode :Node.<any>)`
Constructs a new range node.

## Properties
- `.maxNode :Node.<any>` — A node defining the upper bound of the range. Default is float() .
- `.minNode :Node.<any>` — A node defining the lower bound of the range. Default is float() .

## Methods
- `.getConstNode( node :Node) :Node` — Returns a constant node from the given node by traversing it.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from range definition.
- `.getVectorLength( builder :NodeBuilder) : number` — Returns the vector length which is computed based on the range definition.

## Source