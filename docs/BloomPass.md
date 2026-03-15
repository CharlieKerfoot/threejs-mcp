# BloomPass
Extends: Pass→

A pass for a basic Bloom effect. UnrealBloomPass produces a more advanced Bloom but is also
more expensive.

## Constructor
`newBloomPass( strength :number, kernelSize :number, sigma :number)`
Constructs a new Bloom pass.

## Import

## Properties
- `.combineUniforms : Object` — The combine pass uniforms.
- `.convolutionUniforms : Object` — The convolution pass uniforms.
- `.materialCombine :ShaderMaterial` — The combine pass material.
- `.materialConvolution :ShaderMaterial` — The convolution pass material.
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the Bloom pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source