# FunctionCallNode
Extends: EventDispatcher→Node→TempNode→

This module represents the call of a FunctionNode . Developers are usually not confronted
with this module since they use the predefined TSL syntax wgslFn and glslFn which encapsulate
this logic.

## Constructor
`newFunctionCallNode( functionNode :FunctionNode, parameters :Object.<string,Node>)`
Constructs a new function call node.

## Properties
- `.functionNode :FunctionNode` — The function node. Default is null .
- `.parameters : Object.<string,Node>` — The parameters of the function call. Default is {} .

## Methods
- `.getMemberType( builder :NodeBuilder, name :string) : string` — Returns the function node of this function call node.
- `.getNodeType( builder :NodeBuilder) : string` — Returns the type of this function call node.
- `.getParameters() : Object.<string,Node>` — Returns the parameters of the function call node.
- `.setParameters( parameters :Object.<string,Node>) :FunctionCallNode` — Sets the parameters of the function call node.

## Source