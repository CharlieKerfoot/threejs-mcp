# SetNode
Extends: EventDispatcher→Node→TempNode→

This module is part of the TSL core and usually not used in app level code. SetNode represents a set operation which means it is used to implement any setXYZW() , setRGBA() and setSTPQ() method invocations on node objects.
For example:

## Constructor
`newSetNode( sourceNode :Node, components :string, targetNode :Node)`
Constructs a new set node.

## Properties
- `.components : string` — The components that should be updated.
- `.sourceNode :Node` — The node that should be updated.
- `.targetNode :Node` — The value node.

## Methods
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from SetNode#sourceNode .

## Source