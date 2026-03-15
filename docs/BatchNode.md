# BatchNode
Extends: EventDispatcher→Node→

This node implements the vertex shader logic which is required
when rendering 3D objects via batching. BatchNode must be used
with instances of BatchedMesh .

## Constructor
`newBatchNode( batchMesh :BatchedMesh)`
Constructs a new batch node.

## Properties
- `.batchMesh :BatchedMesh` — A reference to batched mesh.
- `.batchingIdNode :IndexNode` — The batching index node. Default is null .

## Methods
- `.setup( builder :NodeBuilder)` — Setups the internal buffers and nodes and assigns the transformed vertex data
to predefined node variables for accumulation. That follows the same patterns
like with morph and skinning nodes.

## Source