# ReferenceElementNode
Extends: EventDispatcher→Node→ArrayElementNode→

This class is only relevant if the referenced property is array-like.
In this case, ReferenceElementNode allows to refer to a specific
element inside the data structure via an index.

## Constructor
`newReferenceElementNode( referenceNode :ReferenceBaseNode, indexNode :Node)`
Constructs a new reference element node.

## Properties
- `.isReferenceElementNode : boolean` — This flag can be used for type testing. Default is true .
- `.isReferenceElementNode : boolean` — This flag can be used for type testing. Default is true .
- `.referenceNode :ReferenceBaseNode` — Similar to ReferenceBaseNode#reference , an additional
property references to the current node. Default is null .
- `.referenceNode :ReferenceNode` — Similar to ReferenceNode#reference , an additional
property references to the current node. Default is null .

## Methods
- `.getNodeType() : string` — This method is overwritten since the node type is inferred from
the uniform type of the reference node.
- `.getNodeType() : string` — This method is overwritten since the node type is inferred from
the uniform type of the reference node.

## Source