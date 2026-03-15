# MaskPass
Extends: Pass→

This pass can be used to define a mask during post processing.
Meaning only areas of subsequent post processing are affected
which lie in the masking area of this pass. Internally, the masking
is implemented with the stencil buffer.

## Constructor
`newMaskPass( scene :Scene, camera :Camera)`
Constructs a new mask pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.clear : boolean` — Overwritten to perform a clear operation by default. Default is true .
- `.inverse : boolean` — Whether to inverse the mask or not. Default is false .
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.scene :Scene` — The scene that defines the mask.

## Methods
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs a mask pass with the configured scene and camera.

## Source