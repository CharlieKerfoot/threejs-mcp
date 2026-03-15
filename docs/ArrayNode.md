# ArrayNode
Extends: EventDispatcher→Node→TempNode→

ArrayNode represents a collection of nodes, typically created using the array function.

## Constructor
`newArrayNode( nodeType :string, count :number, values :Array.<Node>)`
Constructs a new array node.

## Properties
- `.count : number` — Array size.
- `.isArrayNode : boolean` — This flag can be used for type testing. Default is true .
- `.values : Array.<Node>` — Array default values.

## Methods
- `.generate( builder :NodeBuilder) : string` — This method builds the output node and returns the resulting array as a shader string.
- `.getArrayCount( builder :NodeBuilder) : number` — Returns the number of elements in the node array.
- `.getElementType( builder :NodeBuilder) : string` — Returns the node's type.
- `.getMemberType( builder :NodeBuilder, name :string) : string` — Returns the type of a member variable.
- `.getNodeType( builder :NodeBuilder) : string` — Returns the node's type.

## Source