# SkeletonHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

A helper object to assist with visualizing a Skeleton .

## Constructor
`newSkeletonHelper( object :Object3D)`
Constructs a new skeleton helper.

## Properties
- `.bones : Array.<Bone>` — The list of bones that the helper visualizes.
- `.isSkeletonHelper : boolean` — This flag can be used for type testing. Default is true .
- `.root :Object3D` — The object being visualized.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setColors( color1 :Color, color2 :Color) :SkeletonHelper` — Defines the colors of the helper.

## Source