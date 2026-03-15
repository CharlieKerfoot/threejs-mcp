# SceneOptimizer

This class can be used to optimized scenes by converting
individual meshes into BatchedMesh . This component
is an experimental attempt to implement auto-batching in three.js.

## Constructor
`newSceneOptimizer( scene :Scene, options :SceneOptimizer~Options)`
Constructs a new scene optimizer.

## Import

## Methods
- `.disposeMeshes( meshesToRemove :Set.<Mesh>)` — Removes the given array of meshes from the scene.
- `.removeEmptyNodes( object :Object3D)` — Removes empty nodes from all descendants of the given 3D object.
- `.toBatchedMesh() :Scene` — Performs the auto-baching by identifying groups of meshes in the scene
that can be represented as a single BatchedMesh . The method modifies
the scene by adding instances of BatchedMesh and removin...
- `.toInstancingMesh() :Scene` — Performs the auto-instancing by identifying groups of meshes in the scene
that can be represented as a single InstancedMesh . The method modifies
the scene by adding instances of InstancedMesh and ...

## Type Definitions
- `.Options` — Constructor options of SceneOptimizer .

## Source