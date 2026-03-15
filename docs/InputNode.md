# InputNode
Extends: EventDispatcher→Node→

Base class for representing data input nodes.

## Constructor
`newInputNode( value :any, nodeType :string)`
Constructs a new input node.

## Properties
- `.isInputNode : boolean` — This flag can be used for type testing. Default is true .
- `.precision : 'low' | 'medium' | 'high'` — The precision of the value in the shader. Default is null .
- `.value :any` — The value of this node. This can be any JS primitive, functions, array buffers or even three.js objects (vector, matrices, colors).

## Methods
- `.getInputType( builder :NodeBuilder) : string` — Returns the input type of the node which is by default the node type. Derived modules
might overwrite this method and use a fixed type or compute one analytically. A typical example for different i...
- `.setPrecision( precision :'low' | 'medium' | 'high') :InputNode` — Sets the precision to the given value. The method can be
overwritten in derived classes if the final precision must be computed
analytically.

## Source