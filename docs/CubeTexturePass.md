# CubeTexturePass
Extends: Pass→

This pass can be used to render a cube texture over the entire screen.

## Constructor
`newCubeTexturePass( camera :PerspectiveCamera, tCube :CubeTexture, opacity :number)`
Constructs a new cube texture pass.

## Import

## Properties
- `.camera :PerspectiveCamera` — The camera.
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.opacity : number` — The opacity. Default is 1 .
- `.tCube :CubeTexture` — The cube texture to render.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the cube texture pass.

## Source