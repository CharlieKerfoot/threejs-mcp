# FunctionOverloadingNode
Extends: EventDispatcher→Node→

This class allows to define multiple overloaded versions
of the same function. Depending on the parameters of the function
call, the node picks the best-fit overloaded version.

## Constructor
`newFunctionOverloadingNode( functionNodes :Array.<function()>, …parametersNodes :Node)`
Constructs a new function overloading node.

## Properties
- `.functionNodes : Array.<function()>` — Array of Fn function definitions.
- `.global : boolean` — This node is marked as global. Default is true .
- `.parametersNodes : Array.<Node>` — A list of parameter nodes.

## Methods
- `.getCandidateFn( builder :NodeBuilder) :FunctionNode` — Returns the candidate function for the current parameters.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from
the function's return type.
- `.setup( builder :NodeBuilder) :Node` — Sets up the node for the current parameters.

## Source