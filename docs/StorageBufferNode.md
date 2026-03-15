# StorageBufferNode
Extends: EventDispatcher→Node→InputNode→UniformNode→BufferNode→

This node is used in context of compute shaders and allows to define a
storage buffer for data. A typical workflow is to create instances of
this node with the convenience functions attributeArray() or instancedArray() ,
setup up a compute shader that writes into the buffers and then convert
the storage buffers to attribute nodes for rendering.

## Constructor
`newStorageBufferNode( value :StorageBufferAttribute|StorageInstancedBufferAttribute|BufferAttribute, bufferType :string | Struct, bufferCount :number)`
Constructs a new storage buffer node.

## Properties
- `.access : string` — The access type of the texture node. Default is 'readWrite' .
- `.global : boolean` — StorageBufferNode sets this property to true by default. Default is true .
- `.isAtomic : boolean` — Whether the node is atomic or not. Default is false .
- `.isPBO : boolean` — Whether the node represents a PBO or not.
Only relevant for WebGL. Default is false .
- `.isStorageBufferNode : boolean` — This flag can be used for type testing. Default is true .
- `.structTypeNode :StructTypeNode` — The buffer struct type. Default is null .

## Methods
- `.element( indexNode :IndexNode) :StorageArrayElementNode` — Enables element access with the given index node.
- `.generate( builder :NodeBuilder) : string` — Generates the code snippet of the storage buffer node.
- `.getAttributeData() : Object` — Returns attribute data for this storage buffer node.
- `.getHash( builder :NodeBuilder) : string` — This method is overwritten since the buffer data might be shared
and thus the hash should be shared as well.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return a fixed value 'indirectStorageBuffer' or 'storageBuffer' .
- `.getMemberType( builder :NodeBuilder, name :string) : string` — Returns the type of a member of the struct.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type from the availability of storage buffers
and the attribute data.
- `.getPBO() : boolean` — Returns the isPBO value.
- `.setAccess( value :string) :StorageBufferNode` — Defines the node access.
- `.setAtomic( value :boolean) :StorageBufferNode` — Defines whether the node is atomic or not.
- `.setPBO( value :boolean) :StorageBufferNode` — Defines whether this node is a PBO or not. Only relevant for WebGL.
- `.toAtomic() :StorageBufferNode` — Convenience method for making this node atomic.
- `.toReadOnly() :StorageBufferNode` — Convenience method for configuring a read-only node access.

## Source