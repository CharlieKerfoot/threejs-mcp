# TempNode
Extends: EventDispatcher→Node→

This module uses cache management to create temporary variables
if the node is used more than once to prevent duplicate calculations. The class acts as a base class for many other nodes types.

## Constructor
`newTempNode( nodeType :string)`
Constructs a temp node.

## Properties
- `.isTempNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.hasDependencies( builder :NodeBuilder) : boolean` — Whether this node is used more than once in context of other nodes.

## Source