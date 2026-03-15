# VarNode
Extends: EventDispatcher→Node→

Class for representing shader variables as nodes. Variables are created from
existing nodes like the following:

## Constructor
`newVarNode( node :Node, name :string, readOnly :boolean)`
Constructs a new variable node.

## Properties
- `.global : boolean` — VarNode sets this property to true by default. Default is true .
- `.intent : boolean` — This flag is used to indicate that this node is used for intent. Default is false .
- `.isVarNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the variable in the shader. If no name is defined,
the node system auto-generates one. Default is null .
- `.node :Node` — The node for which a variable should be created.
- `.parents : boolean` — Add this flag to the node system to indicate that this node require parents. Default is true .
- `.readOnly : boolean` — The read-only flag. Default is false .

## Methods
- `.getIntent() : boolean` — Returns the intent flag of this node.
- `.isIntent( builder :NodeBuilder) : boolean` — Checks if this node is used for intent.
- `.setIntent( value :boolean) :VarNode` — Sets the intent flag for this node. This flag is used to indicate that this node is used for intent
and should not be built directly. Instead, it is used to indicate that
the node should be treated...

## Source