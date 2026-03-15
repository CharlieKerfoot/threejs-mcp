# SAOPass
Extends: Pass→

A SAO implementation inspired from @bhouston previous SAO work. SAOPass provides better quality than SSAOPass but is also more expensive.

## Constructor
`newSAOPass( scene :Scene, camera :Camera, resolution :Vector2)`
Constructs a new SAO pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.clear : boolean` — Overwritten to perform a clear operation by default. Default is true .
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.params : Object` — The SAO parameter.
- `.resolution :Vector2` — The effect's resolution. Default is (256,256) .
- `.scene :Scene` — The scene to render the AO for.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the SAO pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source