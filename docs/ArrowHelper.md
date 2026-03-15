# ArrowHelper
Extends: EventDispatcher→Object3D→

An 3D arrow object for visualizing directions.

## Constructor
`newArrowHelper( dir :Vector3, origin :Vector3, length :number, color :number |Color| string, headLength :number, headWidth :number)`
Constructs a new arrow helper.

## Properties
- `.cone :Mesh` — The cone part of the arrow helper.
- `.line :Line` — The line part of the arrow helper.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setColor( color :number |Color| string)` — Sets the color of the helper.
- `.setDirection( dir :Vector3)` — Sets the direction of the helper.
- `.setLength( length :number, headLength :number, headWidth :number)` — Sets the length of the helper.

## Source