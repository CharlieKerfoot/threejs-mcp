# TAARenderPass
Extends: Pass→SSAARenderPass→

Temporal Anti-Aliasing Render Pass. When there is no motion in the scene, the TAA render pass accumulates jittered camera
samples across frames to create a high quality anti-aliased result. Note: This effect uses no reprojection so it is no TRAA implementation.

## Constructor
`newTAARenderPass( scene :Scene, camera :Camera, clearColor :number |Color| string, clearAlpha :number)`
Constructs a new TAA render pass.

## Import

## Properties
- `.accumulate : boolean` — Whether to accumulate frames or not. This enables
the TAA. Default is false .
- `.accumulateIndex : number` — The accumulation index. Default is -1 .
- `.sampleLevel : number` — Overwritten and set to 0 by default. Default is 0 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the TAA render pass.

## Source