# InstanceNode
Extends: EventDispatcher→Node→

This node implements the vertex shader logic which is required
when rendering 3D objects via instancing. The code makes sure
vertex positions, normals and colors can be modified via instanced
data.

## Constructor
`newInstanceNode( count :number, instanceMatrix :InstancedBufferAttribute|StorageInstancedBufferAttribute, instanceColor :InstancedBufferAttribute|StorageInstancedBufferAttribute)`
Constructs a new instance node.

## Properties
- `.buffer :InstancedInterleavedBuffer` — A reference to a buffer that is used by instanceMatrixNode .
- `.bufferColor :InstancedBufferAttribute` — A reference to a buffer that is used by instanceColorNode .
- `.count : number` — The number of instances.
- `.instanceColor :InstancedBufferAttribute` — Instanced buffer attribute representing the color of instances.
- `.instanceColorNode :Node` — The node that represents the instance color data. Default is null .
- `.instanceMatrix :InstancedBufferAttribute` — Instanced buffer attribute representing the transformation of instances.
- `.instanceMatrixNode :Node` — The node that represents the instance matrix data.
- `.isStorageColor : boolean` — Tracks whether the color data is provided via a storage buffer.
- `.isStorageMatrix : boolean` — Tracks whether the matrix data is provided via a storage buffer.
- `.previousInstanceMatrixNode :Node` — The previous instance matrices. Required for computing motion vectors. Default is null .
- `.updateType : string` — The update type is set to frame since an update
of instanced buffer data must be checked per frame. Default is 'frame' .

## Methods
- `.getPreviousInstancedPosition( builder :NodeBuilder) :Node.<vec3>` — Computes the transformed/instanced vertex position of the previous frame.
- `.setup( builder :NodeBuilder)` — Setups the internal buffers and nodes and assigns the transformed vertex data
to predefined node variables for accumulation. That follows the same patterns
like with morph and skinning nodes.
- `.update( frame :NodeFrame)` — Checks if the internal buffers require an update.

## Source