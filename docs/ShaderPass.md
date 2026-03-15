# ShaderPass
Extends: Pass→

This pass can be used to create a post processing effect
with a raw GLSL shader object. Useful for implementing custom
effects.

## Constructor
`newShaderPass( shader :Object |ShaderMaterial, textureID :string)`
Constructs a new shader pass.

## Import

## Properties
- `.material :ShaderMaterial` — The pass material.
- `.textureID : string` — The name of the texture uniform that should sample the read buffer. Default is 'tDiffuse' .
- `.uniforms : Object` — The pass uniforms.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the shader pass.

## Source