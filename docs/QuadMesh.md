# QuadMesh
Extends: EventDispatcher→Object3D→Mesh→

This module is a helper for passes which need to render a full
screen effect which is quite common in context of post processing. The intended usage is to reuse a single quad mesh for rendering
subsequent passes by just reassigning the material reference. Note: This module can only be used with WebGPURenderer .

## Constructor
`newQuadMesh( material :Material)`
Constructs a new quad mesh.

## Properties
- `.camera :OrthographicCamera` — The camera to render the quad mesh with.
- `.isQuadMesh : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.render( renderer :Renderer)` — Renders the quad mesh
- `.renderAsync( renderer :Renderer) : Promise` — Async version of render() .

## Source