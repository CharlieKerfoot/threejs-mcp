# SMAAPass
Extends: Pass→

A pass for applying SMAA. Unlike FXAAPass , SMAAPass operates in linear-srgb so this pass must be executed before OutputPass .

## Constructor
`newSMAAPass()`
Constructs a new SMAA pass.

## Import

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the SMAA pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source