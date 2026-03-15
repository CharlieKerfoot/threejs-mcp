# ReflectorForSSRPass
Extends: EventDispatcher→Object3D→Mesh→

A special version of Reflector for usage with SSRPass .

## Constructor
`newReflectorForSSRPass( geometry :BufferGeometry, options :ReflectorForSSRPass~Options)`
Constructs a new reflector.

## Import

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getRenderTarget() :WebGLRenderTarget` — Returns the reflector's internal render target.

## Type Definitions
- `.Options` — Constructor options of ReflectorForSSRPass .

## Source