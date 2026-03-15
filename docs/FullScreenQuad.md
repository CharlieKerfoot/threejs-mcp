# FullScreenQuad
Extends: EventDispatcher→Object3D→Mesh→

This module is a helper for passes which need to render a full
screen effect which is quite common in context of post processing. The intended usage is to reuse a single full screen quad for rendering
subsequent passes by just reassigning the material reference. This module can only be used with WebGLRenderer .

## Constructor
`newFullScreenQuad( material :Material)`
Constructs a new full screen quad.

## Import

## Properties
- `.material :Material` — The quad's material.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the instance is no longer used in your app.
- `.render( renderer :WebGLRenderer)` — Renders the full screen quad.

## Source