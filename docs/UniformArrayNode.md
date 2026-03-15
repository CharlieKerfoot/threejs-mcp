# UniformArrayNode
Extends: EventDispatcher→Node→InputNode→UniformNode→BufferNode→

Similar to BufferNode this module represents array-like data as
uniform buffers. Unlike BufferNode , it can handle more common
data types in the array (e.g three.js primitives) and automatically
manage buffer padding. It should be the first choice when working with
uniforms buffers.

## Constructor
`newUniformArrayNode( value :Array.<any>, elementType :string)`
Constructs a new uniform array node.

## Properties
- `.array : Array.<any>` — Array holding the buffer data. Unlike BufferNode , the array can
hold number primitives as well as three.js objects like vectors, matrices
or colors.
- `.elementType : string` — The data type of an array element.
- `.isArrayBufferNode : boolean` — This flag can be used for type testing. Default is true .
- `.paddedType : string` — The padded type. Uniform buffers must conform to a certain buffer layout
so a separate type is computed to ensure correct buffer size.
- `.updateType : string` — Overwritten since uniform array nodes are updated per render. Default is 'render' .

## Methods
- `.element( indexNode :IndexNode) :UniformArrayElementNode` — Overwrites the default element() method to provide element access
based on UniformArrayNode .
- `.getElementType( builder :NodeBuilder) : string` — The data type of the array elements.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from the UniformArrayNode#paddedType .
- `.getPaddedType() : string` — Returns the padded type based on the element type.
- `.setup( builder :NodeBuilder) : null` — Implement the value buffer creation based on the array data.
- `.update( frame :NodeFrame)` — The update makes sure to correctly transfer the data from the (complex) objects
in the array to the internal, correctly padded value buffer.

## Source