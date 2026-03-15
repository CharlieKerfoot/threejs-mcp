# ComputeBuiltinNode
Extends: EventDispatcher→Node→

ComputeBuiltinNode represents a compute-scope builtin value that expose information
about the currently running dispatch and/or the device it is running on. This node can only be used with a WebGPU backend.

## Constructor
`newComputeBuiltinNode( builtinName :string, nodeType :string)`
Constructs a new compute builtin node.

## Methods
- `.getBuiltinName( builder :NodeBuilder) : string` — Returns the builtin name.
- `.getHash( builder :NodeBuilder) : string` — This method is overwritten since hash is derived from the built-in name.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is simply derived from nodeType ..
- `.hasBuiltin( builder :NodeBuilder) : boolean` — Whether the current node builder has the builtin or not.
- `.setBuiltinName( builtinName :string) :ComputeBuiltinNode` — Sets the builtin name.

## Source