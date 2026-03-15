# SubBuildNode
Extends: EventDispatcher→Node→

This node is used to build a sub-build in the node system.

## Constructor
`newSubBuildNode( node :Node, name :string, nodeType :string)`

## Properties
- `.isSubBuildNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the sub-build.
- `.node :Node` — The node to be built in the sub-build.

## Source