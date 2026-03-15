# BoxHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

Helper object to graphically show the world-axis-aligned bounding box
around an object. The actual bounding box is handled with Box3 ,
this is just a visual helper for debugging. It can be automatically
resized with BoxHelper#update when the object it's created from
is transformed. Note that the object must have a geometry for this to work,
so it won't work with sprites.

## Constructor
`newBoxHelper( object :Object3D, color :number |Color| string)`
Constructs a new box helper.

## Properties
- `.object :Object3D` — The 3D object being visualized.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setFromObject( object :Object3D) :BoxHelper` — Updates the wireframe box for the passed object.
- `.update()` — Updates the helper's geometry to match the dimensions of the object,
including any children.

## Source