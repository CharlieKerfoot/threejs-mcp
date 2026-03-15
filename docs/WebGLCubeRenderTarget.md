# WebGLCubeRenderTarget
Extends: EventDispatcher→RenderTarget→WebGLRenderTarget→

A cube render target used in context of WebGLRenderer .

## Constructor
`newWebGLCubeRenderTarget( size :number, options :RenderTarget~Options)`
Constructs a new cube render target.

## Properties
- `.isWebGLCubeRenderTarget : boolean` — This flag can be used for type testing. Default is true .
- `.texture :DataArrayTexture` — Overwritten with a different texture type.

## Methods
- `.clear( renderer :WebGLRenderer, color :boolean, depth :boolean, stencil :boolean)` — Clears this cube render target.
- `.fromEquirectangularTexture( renderer :WebGLRenderer, texture :Texture) :WebGLCubeRenderTarget` — Converts the given equirectangular texture to a cube map.

## Source