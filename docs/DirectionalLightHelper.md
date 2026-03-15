# DirectionalLightHelper
Extends: EventDispatcher→Object3D→

Helper object to assist with visualizing a DirectionalLight 's
effect on the scene. This consists of a plane and a line representing the
light's position and direction. When the directional light or its target are transformed or light properties
are changed, it's necessary to call the update() method of the respective helper.

## Constructor
`newDirectionalLightHelper( light :DirectionalLight, size :number, color :number |Color| string)`
Constructs a new directional light helper.

## Properties
- `.color : number |Color| string` — The color parameter passed in the constructor.
If not set, the helper will take the color of the light.
- `.light :DirectionalLight` — The light being visualized.
- `.lightPlane :Line` — Contains the line showing the location of the directional light.
- `.targetLine :Line` — Represents the target line of the directional light.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the helper to match the position and direction of the
light being visualized.

## Source