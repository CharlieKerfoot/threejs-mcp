# SpotLightHelper
Extends: EventDispatcher→Object3D→

This displays a cone shaped helper object for a SpotLight . When the spot light or its target are transformed or light properties are
changed, it's necessary to call the update() method of the respective helper.

## Constructor
`newSpotLightHelper( light :HemisphereLight, color :number |Color| string)`
Constructs a new spot light helper.

## Properties
- `.color : number |Color| string` — The color parameter passed in the constructor.
If not set, the helper will take the color of the light.
- `.light :SpotLight` — The light being visualized.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the helper to match the position and direction of the
light being visualized.

## Source