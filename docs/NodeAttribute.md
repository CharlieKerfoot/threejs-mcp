# NodeAttribute

NodeBuilder is going to create instances of this class during the build process
of nodes. They represent the final shader attributes that are going to be generated
by the builder. Arrays of node attributes is maintained in NodeBuilder#attributes and NodeBuilder#bufferAttributes for this purpose.

## Constructor
`newNodeAttribute( name :string, type :string, node :Node)`
Constructs a new node attribute.

## Properties
- `.isNodeAttribute : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the attribute.
- `.node :Node` — An optional reference to the node. Default is null .
- `.type : string` — The type of the attribute.

## Source