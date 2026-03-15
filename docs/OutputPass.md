# OutputPass
Extends: Pass→

This pass is responsible for including tone mapping and color space conversion
into your pass chain. In most cases, this pass should be included at the end
of each pass chain. If a pass requires sRGB input (e.g. like FXAA), the pass
must follow OutputPass in the pass chain. The tone mapping and color space settings are extracted from the renderer.

## Constructor
`newOutputPass()`
Constructs a new output pass.

## Import

## Properties
- `.isOutputPass : boolean` — This flag indicates that this is an output pass. Default is true .
- `.material :RawShaderMaterial` — The pass material.
- `.uniforms : Object` — The pass uniforms.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the output pass.

## Source