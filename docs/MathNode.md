# MathNode
Extends: EventDispatcher→Node→TempNode→

This node represents a variety of mathematical methods available in shaders.
They are divided into three categories: Methods with one input like sin , cos or normalize . Methods with two inputs like dot , cross or pow . Methods with three inputs like mix , clamp or smoothstep .

## Constructor
`newMathNode( method :string, aNode :Node, bNode :Node, cNode :Node)`
Constructs a new math node.

## Properties
- `.aNode :Node` — The first input.
- `.bNode :Node` — The second input. Default is null .
- `.cNode :Node` — The third input. Default is null .
- `.isMathNode : boolean` — This flag can be used for type testing. Default is true .
- `.method : string` — The method name.

## Methods
- `.getInputType( builder :NodeBuilder) : string` — The input type is inferred from the node types of the input nodes.
- `.getNodeType( builder :NodeBuilder) : string` — The selected method as well as the input type determine the node type of this node.

## Source