# WebGLArrayRenderTarget
Extends: EventDispatcher→RenderTarget→WebGLRenderTarget→

An array render target used in context of WebGLRenderer .

## Constructor
`newWebGLArrayRenderTarget( width :number, height :number, depth :number, options :RenderTarget~Options)`
Constructs a new array render target.

## Properties
- `.isWebGLArrayRenderTarget : boolean` — This flag can be used for type testing. Default is true .
- `.texture :DataArrayTexture` — Overwritten with a different texture type.

## Source