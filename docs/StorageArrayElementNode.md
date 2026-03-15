# StorageArrayElementNode
Extends: EventDispatcher→Node→ArrayElementNode→

This class enables element access on instances of StorageBufferNode .
In most cases, it is indirectly used when accessing elements with the StorageBufferNode#element method.

## Constructor
`newStorageArrayElementNode( storageBufferNode :StorageBufferNode, indexNode :Node)`
Constructs storage buffer element node.

## Properties
- `.isStorageArrayElementNode : boolean` — This flag can be used for type testing. Default is true .
- `.storageBufferNode :StorageBufferNode` — The storage buffer node.

## Source