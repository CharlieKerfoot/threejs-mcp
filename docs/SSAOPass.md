# SSAOPass
Extends: Pass→

A pass for a basic SSAO effect. SAOPass and GTAPass produce a more advanced AO but are also
more expensive.

## Constructor
`newSSAOPass( scene :Scene, camera :Camera, width :number, height :number, kernelSize :number)`
Constructs a new SSAO pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.clear : boolean` — Overwritten to perform a clear operation by default. Default is true .
- `.height : number` — The height of the effect. Default is 512 .
- `.kernelRadius : number` — The kernel radius controls how wide the
AO spreads. Default is 8 .
- `.maxDistance : number` — Defines the maximum distance that should be
affected by the AO. Default is 0.1 .
- `.minDistance : number` — Defines the minimum distance that should be
affected by the AO. Default is 0.005 .
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.output : number` — The output configuration. Default is 0 .
- `.scene :Scene` — The scene to render the AO for.
- `.width : number` — The width of the effect. Default is 512 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the SSAO pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source