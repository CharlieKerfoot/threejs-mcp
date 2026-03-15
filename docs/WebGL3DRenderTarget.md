# WebGL3DRenderTarget
Extends: EventDispatcher→RenderTarget→WebGLRenderTarget→

A 3D render target used in context of WebGLRenderer .

## Constructor
`newWebGL3DRenderTarget( width :number, height :number, depth :number, options :RenderTarget~Options)`
Constructs a new 3D render target.

## Properties
- `.isWebGL3DRenderTarget : boolean` — This flag can be used for type testing. Default is true .
- `.texture :Data3DTexture` — Overwritten with a different texture type.

## Source