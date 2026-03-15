# AfterimagePass
Extends: Pass→

Pass for a basic after image effect.

## Constructor
`newAfterimagePass( damp :number)`
Constructs a new after image pass.

## Import

## Properties
- `.compFsMaterial :ShaderMaterial` — The composition material.
- `.copyFsMaterial :ShaderMaterial` — The copy material.
- `.damp : number` — The damping intensity, from 0.0 to 1.0. A higher value means a stronger after image effect.
- `.uniforms : Object` — The pass uniforms. Use this object if you want to update the damp value at runtime. pass.uniforms.damp.value = 0.9;

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the after image pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source