# BufferNode
Extends: EventDispatcher→Node→InputNode→UniformNode→

A special type of uniform node which represents array-like data
as uniform buffers. The access usually happens via element() which returns an instance of ArrayElementNode . For example: In general, it is recommended to use the more managed UniformArrayNode since it handles more input types and automatically cares about buffer paddings.

## Constructor
`newBufferNode( value :Array.<number>, bufferType :string, bufferCount :number)`
Constructs a new buffer node.

## Properties
- `.bufferCount : number` — The uniform node that holds the value of the reference node. Default is 0 .
- `.bufferType : string` — The data type of the buffer.
- `.isBufferNode : boolean` — This flag can be used for type testing. Default is true .
- `.updateRanges : Array.<{start: number, count: number}>` — An array of update ranges.

## Methods
- `.addUpdateRange( start :number, count :number)` — Adds a range of data in the data array to be updated on the GPU.
- `.clearUpdateRanges()` — Clears the update ranges.
- `.getElementType( builder :NodeBuilder) : string` — The data type of the buffer elements.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return a fixed value 'buffer' .

## Source