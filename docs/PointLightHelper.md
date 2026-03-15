# PointLightHelper
Extends: EventDispatcher→Object3D→Mesh→

This displays a helper object consisting of a spherical mesh for
visualizing an instance of PointLight .

## Constructor
`newPointLightHelper( light :PointLight, sphereSize :number, color :number |Color| string)`
Constructs a new point light helper.

## Properties
- `.color : number |Color| string` — The color parameter passed in the constructor.
If not set, the helper will take the color of the light.
- `.light :PointLight` — The light being visualized.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the helper to match the position of the
light being visualized.

## Source