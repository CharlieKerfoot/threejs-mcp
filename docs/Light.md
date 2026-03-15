# Light
Extends: EventDispatcher→Object3D→

Abstract base class for lights - all other light types inherit the
properties and methods described here.

## Constructor
`newLight( color :number |Color| string, intensity :number)(abstract)`
Constructs a new light.

## Properties
- `.color :Color` — The light's color.
- `.intensity : number` — The light's intensity. Default is 1 .
- `.isLight : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source