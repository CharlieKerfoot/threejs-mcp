# PolarGridHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

This helper is an object to define polar grids. Grids are
two-dimensional arrays of lines.

## Constructor
`newPolarGridHelper( radius :number, sectors :number, rings :number, divisions :number, color1 :number |Color| string, color2 :number |Color| string)`
Constructs a new polar grid helper.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source