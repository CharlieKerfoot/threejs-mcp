# Box3Helper
Extends: EventDispatcher→Object3D→Line→LineSegments→

A helper object to visualize an instance of Box3 .

## Constructor
`newBox3Helper( box :Box3, color :number |Color| string)`
Constructs a new box3 helper.

## Properties
- `.box :Box3` — The box being visualized.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source