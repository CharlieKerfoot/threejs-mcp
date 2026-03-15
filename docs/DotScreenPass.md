# DotScreenPass
Extends: Pass→

Pass for creating a dot-screen effect.

## Constructor
`newDotScreenPass( center :Vector2, angle :number, scale :number)`
Constructs a new dot screen pass.

## Import

## Properties
- `.material :ShaderMaterial` — The pass material.
- `.uniforms : Object` — The pass uniforms. Use this object if you want to update the center , angle or scale values at runtime. pass.uniforms.center.value.copy( center );
pass.uniforms.angle.value = 0;
pass.uniforms.scale...

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the dot screen pass.

## Source