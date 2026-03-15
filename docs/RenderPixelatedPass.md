# RenderPixelatedPass
Extends: Pass→

A special type of render pass that produces a pixelated beauty pass.

## Constructor
`newRenderPixelatedPass( pixelSize :number, scene :Scene, camera :Camera, options :Object)`
Constructs a new render pixelated pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.depthEdgeStrength : number` — The normal edge strength. Default is 0.4 .
- `.normalEdgeStrength : number` — The normal edge strength. Default is 0.3 .
- `.pixelSize : number` — The effect's pixel size.
- `.pixelatedMaterial :ShaderMaterial` — The pixelated material.
- `.scene :Scene` — The scene to render.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the pixelation pass.
- `.setPixelSize( pixelSize :number)` — Sets the effect's pixel size.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source