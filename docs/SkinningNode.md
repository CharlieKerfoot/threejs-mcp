# SkinningNode
Extends: EventDispatcher→Node→

This node implements the vertex transformation shader logic which is required
for skinning/skeletal animation.

## Constructor
`newSkinningNode( skinnedMesh :SkinnedMesh)`
Constructs a new skinning node.

## Properties
- `.bindMatrixInverseNode :Node.<mat4>` — The bind matrix inverse node.
- `.bindMatrixNode :Node.<mat4>` — The bind matrix node.
- `.boneMatricesNode :Node` — The bind matrices as a uniform buffer node.
- `.positionNode :Node.<vec3>` — The current vertex position in local space.
- `.previousBoneMatricesNode :Node` — The previous bind matrices as a uniform buffer node.
Required for computing motion vectors. Default is null .
- `.skinIndexNode :AttributeNode` — The skin index attribute.
- `.skinWeightNode :AttributeNode` — The skin weight attribute.
- `.skinnedMesh :SkinnedMesh` — The skinned mesh.
- `.toPositionNode :Node.<vec3>` — The result of vertex position in local space.
- `.updateType : string` — The update type overwritten since skinning nodes are updated per object.

## Methods
- `.generate( builder :NodeBuilder, output :string) : string` — Generates the code snippet of the skinning node.
- `.getPreviousSkinnedPosition( builder :NodeBuilder) :Node.<vec3>` — Computes the transformed/skinned vertex position of the previous frame.
- `.getSkinnedNormalAndTangent( boneMatrices :Node, normal :Node.<vec3>, tangent :Node.<vec3>) : Object` — Transforms the given vertex normal and tangent via skinning.
- `.getSkinnedPosition( boneMatrices :Node, position :Node.<vec3>) :Node.<vec3>` — Transforms the given vertex position via skinning.
- `.setup( builder :NodeBuilder) :Node.<vec3>` — Setups the skinning node by assigning the transformed vertex data to predefined node variables.
- `.update( frame :NodeFrame)` — Updates the state of the skinned mesh by updating the skeleton once per frame.

## Source