# Reflector
Extends: EventDispatcher→Object3D→Mesh→

Can be used to create a flat, reflective surface like a mirror. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use ReflectorNode .

## Constructor
`newReflector( geometry :BufferGeometry, options :Reflector~Options)`
Constructs a new reflector.

## Import

## Properties
- `.camera :PerspectiveCamera` — The reflector's virtual camera. This is used to render
the scene from the mirror's point of view.
- `.forceUpdate : boolean` — Whether to force an update, no matter if the reflector
is in view or not. Default is false .
- `.isReflector : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getRenderTarget() :WebGLRenderTarget` — Returns the reflector's internal render target.

## Type Definitions
- `.Options` — Constructor options of Reflector .

## Source