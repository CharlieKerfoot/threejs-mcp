# NodeCode

NodeBuilder is going to create instances of this class during the build process
of nodes. They represent user-defined, native shader code portions that are going to be
injected by the builder. A dictionary of node codes is maintained in NodeBuilder#codes for this purpose.

## Constructor
`newNodeCode( name :string, type :string, code :string)`
Constructs a new code node.

## Properties
- `.code : string` — The native shader code. Default is '' .
- `.name : string` — The name of the code.
- `.type : string` — The node type.

## Source