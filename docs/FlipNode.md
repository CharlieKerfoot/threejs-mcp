# FlipNode
Extends: EventDispatcher→Node→TempNode→

This module is part of the TSL core and usually not used in app level code.
It represents a flip operation during the shader generation process
meaning it flips normalized values with the following formula: FlipNode is internally used to implement any flipXYZW() , flipRGBA() and flipSTPQ() method invocations on node objects. For example: uvNode = uvNode.flipY();

## Constructor
`newFlipNode( sourceNode :Node, components :string)`
Constructs a new flip node.

## Properties
- `.components : string` — The components that should be flipped e.g. 'x' or 'xy' .
- `.sourceNode :Node` — The node which component(s) should be flipped.

## Methods
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from the source node.

## Source