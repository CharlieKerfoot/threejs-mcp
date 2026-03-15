# UnrealBloomPass
Extends: Pass→

This pass is inspired by the bloom pass of Unreal Engine. It creates a
mip map chain of bloom textures and blurs them with different radii. Because
of the weighted combination of mips, and because larger blurs are done on
higher mips, this effect provides good quality and performance. When using this pass, tone mapping must be enabled in the renderer settings. Reference: Bloom in Unreal Engine

## Constructor
`newUnrealBloomPass( resolution :Vector2, strength :number, radius :number, threshold :number)`
Constructs a new Unreal Bloom pass.

## Import

## Properties
- `.clearColor :Color` — The effect's clear color Default is (0,0,0) .
- `.needsSwap : boolean` — Overwritten to disable the swap. Default is false .
- `.radius : number` — The Bloom radius. Must be in the range [0,1] .
- `.resolution :Vector2` — The effect's resolution. Default is (256,256) .
- `.strength : number` — The Bloom strength. Default is 1 .
- `.threshold : number` — The luminance threshold limits which bright areas contribute to the Bloom effect.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the Bloom pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source