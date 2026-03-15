# Refractor
Extends: EventDispatcher→Object3D→Mesh→

Can be used to create a flat, refractive surface like for special
windows or water effects. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use viewportSharedTexture .

## Constructor
`newRefractor( geometry :BufferGeometry, options :Refractor~Options)`
Constructs a new refractor.

## Import

## Properties
- `.camera :PerspectiveCamera` — The reflector's virtual camera.
- `.isRefractor : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getRenderTarget() :WebGLRenderTarget` — Returns the reflector's internal render target.

## Type Definitions
- `.Options` — Constructor options of Refractor .

## Source