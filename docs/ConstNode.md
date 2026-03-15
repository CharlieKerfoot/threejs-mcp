# ConstNode
Extends: EventDispatcher→Node→InputNode→

Class for representing a constant value in the shader.

## Constructor
`newConstNode( value :any, nodeType :string)`
Constructs a new input node.

## Properties
- `.isConstNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.generateConst( builder :NodeBuilder) : string` — Generates the shader string of the value with the current node builder.

## Source