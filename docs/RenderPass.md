# RenderPass
Extends: Pass→

This class represents a render pass. It takes a camera and a scene and produces
a beauty pass for subsequent post processing effects.

## Constructor
`newRenderPass( scene :Scene, camera :Camera, overrideMaterial :Material, clearColor :number |Color| string, clearAlpha :number)`
Constructs a new render pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.clear : boolean` — Overwritten to perform a clear operation by default. Default is true .
- `.clearAlpha : number` — The clear alpha of the render pass. Default is null .
- `.clearColor : number |Color| string` — The clear color of the render pass. Default is null .
- `.clearDepth : boolean` — If set to true , only the depth can be cleared when clear is to false . Default is false .
- `.isRenderPass : boolean` — This flag indicates that this pass renders the scene itself. Default is true .
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.overrideMaterial :Material` — The override material. If set, this material is used
for all objects in the scene. Default is null .
- `.scene :Scene` — The scene to render.

## Methods
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs a beauty pass with the configured scene and camera.

## Source