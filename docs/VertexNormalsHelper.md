# VertexNormalsHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

Visualizes an object's vertex normals. Requires that normals have been specified in the geometry as a buffer attribute or
have been calculated using BufferGeometry#computeVertexNormals .

## Constructor
`newVertexNormalsHelper( object :Object3D, size :number, color :number |Color| string)`
Constructs a new vertex normals helper.

## Import

## Properties
- `.isVertexNormalsHelper : boolean` — This flag can be used for type testing. Default is true .
- `.matrixAutoUpdate : boolean` — Overwritten and set to false since the object's world transformation
is encoded in the helper's geometry data. Default is false .
- `.object :Object3D` — The object for which to visualize vertex normals.
- `.size : number` — The helper's size. Default is 1 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the vertex normals preview based on the object's world transform.

## Source