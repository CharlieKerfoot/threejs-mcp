# ExpressionNode
Extends: EventDispatcher→Node→

This class can be used to implement basic expressions in shader code.
Basic examples for that are return , continue or discard statements.

## Constructor
`newExpressionNode( snippet :string, nodeType :string)`
Constructs a new expression node.

## Properties
- `.snippet : string` — The native code snippet. Default is '' .

## Source