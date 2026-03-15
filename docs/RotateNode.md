# RotateNode
Extends: EventDispatcher→Node→TempNode→

Applies a rotation to the given position node.

## Constructor
`newRotateNode( positionNode :Node, rotationNode :Node)`
Constructs a new rotate node.

## Properties
- `.positionNode :Node` — The position node.
- `.rotationNode :Node` — Represents the rotation that is applied to the position node.
Depending on whether the position data are 2D or 3D, the rotation is expressed a single float value or an Euler value.

## Methods
- `.getNodeType( builder :NodeBuilder) : string` — The type of the RotateNode#positionNode defines the node's type.

## Source