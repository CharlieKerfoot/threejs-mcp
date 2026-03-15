# HalftonePass
Extends: Pass→

Pass for creating a RGB halftone effect.

## Constructor
`newHalftonePass( params :Object)`
Constructs a new halftone pass.

## Import

## Properties
- `.material :ShaderMaterial` — The pass material.
- `.uniforms : Object` — The pass uniforms.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the halftone pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source