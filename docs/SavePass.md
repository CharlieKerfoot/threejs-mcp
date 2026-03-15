# SavePass
Extends: Pass→

A pass that saves the contents of the current read buffer in a render target.

## Constructor
`newSavePass( renderTarget :WebGLRenderTarget)`
Constructs a new save pass.

## Import

## Properties
- `.material :ShaderMaterial` — The pass material.
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.renderTarget :WebGLRenderTarget` — The render target which is used to save the read buffer.
- `.uniforms : Object` — The pass uniforms.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the save pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source