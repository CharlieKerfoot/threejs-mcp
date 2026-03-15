# Frustum

Frustums are used to determine what is inside the camera's field of view.
They help speed up the rendering process - objects which lie outside a camera's
frustum can safely be excluded from rendering. This class is mainly intended for use internally by a renderer.

## Constructor
`newFrustum( p0 :Plane, p1 :Plane, p2 :Plane, p3 :Plane, p4 :Plane, p5 :Plane)`
Constructs a new frustum.

## Properties
- `.planes : Array.<Plane>` — This array holds the planes that enclose the frustum.

## Methods
- `.clone() :Frustum` — Returns a new frustum with copied values from this instance.
- `.containsPoint( point :Vector3) : boolean` — Returns true if the given point lies within the frustum.
- `.copy( frustum :Frustum) :Frustum` — Copies the values of the given frustum to this instance.
- `.intersectsBox( box :Box3) : boolean` — Returns true if the given bounding box is intersecting this frustum.
- `.intersectsObject( object :Object3D) : boolean` — Returns true if the 3D object's bounding sphere is intersecting this frustum. Note that the 3D object must have a geometry so that the bounding sphere can be calculated.
- `.intersectsSphere( sphere :Sphere) : boolean` — Returns true if the given bounding sphere is intersecting this frustum.
- `.intersectsSprite( sprite :Sprite) : boolean` — Returns true if the given sprite is intersecting this frustum.
- `.set( p0 :Plane, p1 :Plane, p2 :Plane, p3 :Plane, p4 :Plane, p5 :Plane) :Frustum` — Sets the frustum planes by copying the given planes.
- `.setFromProjectionMatrix( m :Matrix4, coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem, reversedDepth :boolean) :Frustum` — Sets the frustum planes from the given projection matrix.

## Source