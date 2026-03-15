# GlitchPass
Extends: Pass→

Pass for creating a glitch effect.

## Constructor
`newGlitchPass( dt_size :number)`
Constructs a new glitch pass.

## Import

## Properties
- `.goWild : boolean` — Whether to noticeably increase the effect intensity or not. Default is false .
- `.material :ShaderMaterial` — The pass material.
- `.uniforms : Object` — The pass uniforms.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the glitch pass.

## Source