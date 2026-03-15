# CCDIKHelper
Extends: EventDispatcher→Object3D→

Helper for visualizing IK bones.

## Constructor
`newCCDIKHelper( mesh :SkinnedMesh, iks :Array.<CCDIKSolver~IK>, sphereSize :number)`

## Import

## Properties
- `.effectorSphereMaterial :MeshBasicMaterial` — The material for the effector spheres.
- `.iks : Array.<CCDIKSolver~IK>` — The IK objects.
- `.lineMaterial :LineBasicMaterial` — A global line material.
- `.linkSphereMaterial :MeshBasicMaterial` — The material for the link spheres.
- `.root :SkinnedMesh` — The skinned mesh this helper refers to.
- `.sphereGeometry :SphereGeometry` — The helpers sphere geometry.
- `.targetSphereMaterial :MeshBasicMaterial` — The material for the target spheres.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance.
Call this method whenever this instance is no longer used in your app.

## Source