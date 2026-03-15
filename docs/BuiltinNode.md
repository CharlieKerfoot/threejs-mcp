# BuiltinNode
Extends: EventDispatcher→Node→

The node allows to set values for built-in shader variables. That is
required for features like hardware-accelerated vertex clipping.

## Constructor
`newBuiltinNode( name :string)`
Constructs a new builtin node.

## Properties
- `.isBuiltinNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the built-in shader variable.

## Methods
- `.generate( builder :NodeBuilder) : string` — Generates the code snippet of the builtin node.

## Source