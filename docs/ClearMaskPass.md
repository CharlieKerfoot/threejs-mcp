# ClearMaskPass
Extends: Pass→

This pass can be used to clear a mask previously defined with MaskPass .

## Constructor
`newClearMaskPass()`
Constructs a new clear mask pass.

## Properties
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .

## Methods
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the clear of the currently defined mask.

## Source