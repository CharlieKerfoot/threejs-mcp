# AxesHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

An axis object to visualize the 3 axes in a simple way.
The X axis is red. The Y axis is green. The Z axis is blue.

## Constructor
`newAxesHelper( size :number)`
Constructs a new axes helper.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setColors( xAxisColor :number |Color| string, yAxisColor :number |Color| string, zAxisColor :number |Color| string) :AxesHelper` — Defines the colors of the axes helper.

## Source