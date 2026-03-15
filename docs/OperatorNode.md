# OperatorNode
Extends: EventDispatcher→Node→TempNode→

This node represents basic mathematical and logical operations like addition,
subtraction or comparisons (e.g. equal() ).

## Constructor
`newOperatorNode( op :string, aNode :Node, bNode :Node, …params :Node)`
Constructs a new operator node.

## Properties
- `.aNode :Node` — The first input.
- `.bNode :Node` — The second input.
- `.isOperatorNode : boolean` — This flag can be used for type testing. Default is true .
- `.op : string` — The operator.

## Methods
- `.getNodeType( builder :NodeBuilder, output :string) : string` — This method is overwritten since the node type is inferred from the operator
and the input node types.
- `.getOperatorMethod( builder :NodeBuilder, output :string) : string` — Returns the operator method name.

## Source