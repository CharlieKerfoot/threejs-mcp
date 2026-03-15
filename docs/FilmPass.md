# FilmPass
Extends: Pass→

This pass can be used to create a film grain effect.

## Constructor
`newFilmPass( intensity :number, grayscale :boolean)`
Constructs a new film pass.

## Import

## Properties
- `.material :ShaderMaterial` — The pass material.
- `.uniforms : Object` — The pass uniforms. Use this object if you want to update the intensity or grayscale values at runtime. pass.uniforms.intensity.value = 1;
pass.uniforms.grayscale.value = true;

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the film pass.

## Source