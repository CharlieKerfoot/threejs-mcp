# RectAreaLightHelper
Extends: EventDispatcher→Object3D→Line→

Creates a visual aid for rect area lights. RectAreaLightHelper must be added as a child of the light.

## Constructor
`newRectAreaLightHelper( light :RectAreaLight, color :number |Color| string)`
Constructs a new rect area light helper.

## Import

## Properties
- `.color : number |Color| string | undefined` — The helper's color. If undefined , the helper will take the color of the light.
- `.light :RectAreaLight` — The light to visualize.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source