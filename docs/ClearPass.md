# ClearPass
Extends: Pass→

This class can be used to force a clear operation for the current read or
default framebuffer (when rendering to screen).

## Constructor
`newClearPass( clearColor :number |Color| string, clearAlpha :number)`
Constructs a new clear pass.

## Import

## Properties
- `.clearAlpha : number` — The clear alpha. Default is 0 .
- `.clearColor : number |Color| string` — The clear color. Default is 0x000000 .
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .

## Methods
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the clear operation. This affects the current read or the default framebuffer.

## Source