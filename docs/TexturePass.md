# TexturePass
Extends: Pass→

This pass can be used to render a texture over the entire screen.

## Constructor
`newTexturePass( map :Texture, opacity :number)`
Constructs a new texture pass.

## Import

## Properties
- `.map :Texture` — The texture to render.
- `.material :ShaderMaterial` — The pass material.
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.opacity : number` — The opacity. Default is 1 .
- `.uniforms : Object` — The pass uniforms.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the texture pass.

## Source