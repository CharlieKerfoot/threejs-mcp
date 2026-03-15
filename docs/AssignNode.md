# AssignNode
Extends: EventDispatcher→Node→TempNode→

These node represents an assign operation. Meaning a node is assigned
to another node.

## Constructor
`newAssignNode( targetNode :Node, sourceNode :Node)`
Constructs a new assign node.

## Properties
- `.isAssignNode : boolean` — This flag can be used for type testing. Default is true .
- `.sourceNode :Node` — The source node.
- `.targetNode :Node` — The target node.

## Methods
- `.hasDependencies() : boolean` — Whether this node is used more than once in context of other nodes. This method
is overwritten since it always returns false (assigns are unique).
- `.needsSplitAssign( builder :NodeBuilder) : boolean` — Whether a split is required when assigning source to target. This can happen when the component length of
target and source data type does not match.

## Source