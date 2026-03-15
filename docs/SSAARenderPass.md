# SSAARenderPass
Extends: Pass→

Supersample Anti-Aliasing Render Pass. This manual approach to SSAA re-renders the scene ones for each sample with camera jitter and accumulates the results.

## Constructor
`newSSAARenderPass( scene :Scene, camera :Camera, clearColor :number |Color| string, clearAlpha :number)`
Constructs a new SSAA render pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.clearAlpha : number` — The clear alpha of the render pass. Default is 0 .
- `.clearColor : number |Color| string` — The clear color of the render pass. Default is 0x000000 .
- `.sampleLevel : number` — The sample level. Specified as n, where the number of
samples is 2^n, so sampleLevel = 4, is 2^4 samples, 16. Default is 4 .
- `.scene :Scene` — The scene to render.
- `.stencilBuffer : boolean` — Whether to use a stencil buffer or not. This property can't
be changed after the first render. Default is false .
- `.unbiased : boolean` — Whether the pass should be unbiased or not. This property has the most
visible effect when rendering to a RGBA8 buffer because it mitigates
rounding errors. By default RGBA16F is used. Default is t...

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the SSAA render pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source