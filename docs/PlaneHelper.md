# PlaneHelper
Extends: EventDispatcher→Object3D→Line→

A helper object to visualize an instance of Plane .

## Constructor
`newPlaneHelper( plane :Plane, size :number, hex :number |Color| string)`
Constructs a new plane helper.

## Properties
- `.plane :Plane` — The plane being visualized.
- `.size : number` — The side length of plane helper. Default is 1 .

## Methods
- `.dispose()` — Updates the helper to match the position and direction of the
light being visualized.

## Source