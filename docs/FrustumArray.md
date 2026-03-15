# FrustumArray

FrustumArray is used to determine if an object is visible in at least one camera
from an array of cameras. This is particularly useful for multi-view renderers.

## Constructor
`newFrustumArray()`
Constructs a new frustum array.

## Properties
- `.coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem` — The coordinate system to use. Default is WebGLCoordinateSystem .

## Methods
- `.clone() :FrustumArray` — Returns a new frustum array with copied values from this instance.
- `.containsPoint( point :Vector3, cameraArray :Object) : boolean` — Returns true if the given point lies within any frustum
from the camera array.
- `.intersectsBox( box :Box3, cameraArray :Object) : boolean` — Returns true if the given bounding box is intersecting any frustum
from the camera array.
- `.intersectsObject( object :Object3D, cameraArray :Object) : boolean` — Returns true if the 3D object's bounding sphere is intersecting any frustum
from the camera array.
- `.intersectsSphere( sphere :Sphere, cameraArray :Object) : boolean` — Returns true if the given bounding sphere is intersecting any frustum
from the camera array.
- `.intersectsSprite( sprite :Sprite, cameraArray :Object) : boolean` — Returns true if the given sprite is intersecting any frustum
from the camera array.

## Source