# AtomicFunctionNode
Extends: EventDispatcher→Node→

AtomicFunctionNode represents any function that can operate on atomic variable types
within a shader. In an atomic function, any modification to an atomic variable will
occur as an indivisible step with a defined order relative to other modifications.
Accordingly, even if multiple atomic functions are modifying an atomic variable at once
atomic operations will not interfere with each other. This node can only be used with a WebGPU backend.

## Constructor
`newAtomicFunctionNode( method :string, pointerNode :Node, valueNode :Node)`
Constructs a new atomic function node.

## Properties
- `.method : string` — The signature of the atomic function to construct.
- `.parents : boolean` — Creates a list of the parents for this node for detecting if the node needs to return a value. Default is true .
- `.pointerNode :Node` — An atomic variable or element of an atomic buffer.
- `.valueNode :Node` — A value that modifies the atomic variable.

## Methods
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return the type of
the pointer node.
- `.getNodeType( builder :NodeBuilder) : string` — Overwritten since the node type is inferred from the input type.

## Source