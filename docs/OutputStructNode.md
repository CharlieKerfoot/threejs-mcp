# OutputStructNode
Extends: EventDispatcher→Node→

This node can be used to define multiple outputs in a shader programs.

## Constructor
`newOutputStructNode( …members :Node)`
Constructs a new output struct node. The constructor can be invoked with an
arbitrary number of nodes representing the members.

## Properties
- `.isOutputStructNode : boolean` — This flag can be used for type testing. Default is true .
- `.members : Array.<Node>` — An array of nodes which defines the output.

## Source