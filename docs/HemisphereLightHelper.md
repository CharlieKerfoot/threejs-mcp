# HemisphereLightHelper
Extends: EventDispatcher→Object3D→

Creates a visual aid consisting of a spherical mesh for a
given HemisphereLight . When the hemisphere light is transformed or its light properties are changed,
it's necessary to call the update() method of the respective helper.

## Constructor
`newHemisphereLightHelper( light :HemisphereLight, size :number, color :number |Color| string)`
Constructs a new hemisphere light helper.

## Properties
- `.color : number |Color| string` — The color parameter passed in the constructor.
If not set, the helper will take the color of the light.
- `.light :HemisphereLight` — The light being visualized.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the helper to match the position and direction of the
light being visualized.

## Source