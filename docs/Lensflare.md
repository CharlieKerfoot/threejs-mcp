# Lensflare
Extends: EventDispatcher→Object3D→Mesh→

Creates a simulated lens flare that tracks a light. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use LensflareMesh .

## Constructor
`newLensflare()`
Constructs a new lensflare.

## Import

## Properties
- `.frustumCulled : boolean` — Overwritten to disable view-frustum culling by default. Default is false .
- `.isLensflare : boolean` — This flag can be used for type testing. Default is true .
- `.renderOrder : number` — Overwritten to make sure lensflares a rendered last. Default is Infinity .

## Methods
- `.addElement( element :LensflareElement)` — Adds the given lensflare element to this instance.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source