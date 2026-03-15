# FunctionNode
Extends: EventDispatcher→Node→CodeNode→

This class represents a native shader function. It can be used to implement
certain aspects of a node material with native shader code. There are two predefined
TSL functions for easier usage. wgslFn : Creates a WGSL function node. glslFn : Creates a GLSL function node. A basic example with one include looks like so:

## Constructor
`newFunctionNode( code :string, includes :Array.<Node>, language :'js' | 'wgsl' | 'glsl')`
Constructs a new function node.

## Methods
- `.getInputs( builder :NodeBuilder) : Array.<NodeFunctionInput>` — Returns the inputs of this function node.
- `.getMemberType( builder :NodeBuilder, name :string) : string` — Returns the type of a member of this function node.
- `.getNodeFunction( builder :NodeBuilder) :NodeFunction` — Returns the node function for this function node.
- `.getNodeType( builder :NodeBuilder) : string` — Returns the type of this function node.

## Source