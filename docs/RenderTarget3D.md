# RenderTarget3D
Extends: EventDispatcher→RenderTarget→

Represents a 3D render target.

## Constructor
`newRenderTarget3D( width :number, height :number, depth :number, options :RenderTarget~Options)`
Constructs a new 3D render target.

## Properties
- `.isRenderTarget3D : boolean` — This flag can be used for type testing. Default is true .
- `.texture :Data3DTexture` — Overwritten with a different texture type.

## Source