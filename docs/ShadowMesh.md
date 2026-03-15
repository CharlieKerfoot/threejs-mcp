# ShadowMesh
Extends: EventDispatcher→Object3D→Mesh→

A Shadow Mesh that follows a shadow-casting mesh in the scene,
but is confined to a single plane. This technique can be used as
a very performant alternative to classic shadow mapping. However,
it has serious limitations like: Shadows can only be casted on flat planes. No soft shadows support.

## Constructor
`newShadowMesh( mesh :Mesh)`
Constructs a new shadow mesh.

## Import

## Properties
- `.frustumCulled : boolean` — Overwritten to disable view-frustum culling by default. Default is false .
- `.isShadowMesh : boolean` — This flag can be used for type testing. Default is true .
- `.matrixAutoUpdate : boolean` — Overwritten to disable automatic matrix update. The local
matrix is computed manually in ShadowMesh#update . Default is false .
- `.meshMatrix :Matrix4` — Represent the world matrix of the reference mesh.

## Methods
- `.update( plane :Plane, lightPosition4D :Vector4)` — Updates the shadow mesh so it follows its shadow-casting reference mesh.

## Source