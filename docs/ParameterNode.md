# ParameterNode
Extends: EventDispatcher→Node→PropertyNode→

Special version of PropertyNode which is used for parameters.

## Constructor
`newParameterNode( nodeType :string, name :string)`
Constructs a new parameter node.

## Properties
- `.isParameterNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.getMemberType( builder :NodeBuilder, name :string) : string` — Gets the type of a member variable in the parameter node.

## Source