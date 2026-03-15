# ArrayElementNode
Extends: EventDispatcher→Node→

Base class for representing element access on an array-like
node data structures.

## Constructor
`newArrayElementNode( node :Node, indexNode :Node)`
Constructs an array element node.

## Properties
- `.indexNode :Node` — The index node that defines the element access.
- `.isArrayElementNode : boolean` — This flag can be used for type testing. Default is true .
- `.node :Node` — The array-like node.

## Methods
- `.getMemberType( builder :NodeBuilder, name :string) : string` — This method is overwritten since the member type is inferred from the array-like node.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from the array-like node.

## Source