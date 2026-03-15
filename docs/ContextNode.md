# ContextNode
Extends: EventDispatcher→Node→

This node can be used as a context management component for another node. NodeBuilder performs its node building process in a specific context and
this node allows the modify the context. A typical use case is to overwrite getUV() e.g.:

## Constructor
`newContextNode( node :Node, value :Object)`
Constructs a new context node.

## Properties
- `.isContextNode : boolean` — This flag can be used for type testing. Default is true .
- `.node :Node` — The node whose context should be modified.
- `.value : Object` — The modified context data. Default is {} .

## Methods
- `.getFlowContextData() : Object` — Gathers the context data from all parent context nodes.
- `.getMemberType( builder :NodeBuilder, name :string) : string` — This method is overwritten to ensure it returns the member type of ContextNode#node .
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten to ensure it returns the type of ContextNode#node .
- `.getScope() :Node` — This method is overwritten to ensure it returns the reference to ContextNode#node .

## Source