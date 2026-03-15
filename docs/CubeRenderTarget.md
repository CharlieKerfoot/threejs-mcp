# CubeRenderTarget
Extends: EventDispatcher→RenderTarget→

This class represents a cube render target. It is a special version
of WebGLCubeRenderTarget which is compatible with WebGPURenderer .

## Constructor
`newCubeRenderTarget( size :number, options :RenderTarget~Options)`
Constructs a new cube render target.

## Properties
- `.isCubeRenderTarget : boolean` — This flag can be used for type testing. Default is true .
- `.texture :DataArrayTexture` — Overwritten with a different texture type.

## Methods
- `.clear( renderer :Renderer, color :boolean, depth :boolean, stencil :boolean)` — Clears this cube render target.
- `.fromEquirectangularTexture( renderer :Renderer, texture :Texture) :CubeRenderTarget` — Converts the given equirectangular texture to a cube map.

## Source