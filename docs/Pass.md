# Pass

Abstract base class for all post processing passes. This module is only relevant for post processing with WebGLRenderer .

## Constructor
`newPass()(abstract)`
Constructs a new pass.

## Import

## Properties
- `.clear : boolean` — If set to true , the pass clears its buffer before rendering Default is false .
- `.enabled : boolean` — If set to true , the pass is processed by the composer. Default is true .
- `.isPass : boolean` — This flag can be used for type testing. Default is true .
- `.needsSwap : boolean` — If set to true , the pass indicates to swap read and write buffer after rendering. Default is true .
- `.renderToScreen : boolean` — If set to true , the result of the pass is rendered to screen. The last pass in the composers
pass chain gets automatically rendered to screen, no matter how this property is configured. Default is...

## Methods
- `.dispose() (abstract)` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean) (abstract)` — This method holds the render logic of a pass. It must be implemented in all derived classes.
- `.setSize( width :number, height :number) (abstract)` — Sets the size of the pass.

## Source