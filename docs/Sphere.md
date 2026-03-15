# Sphere

An analytical 3D sphere defined by a center and radius. This class is mainly
used as a Bounding Sphere for 3D objects.

## Constructor
`newSphere( center :Vector3, radius :number)`
Constructs a new sphere.

## Properties
- `.center :Vector3` — The center of the sphere
- `.isSphere : boolean` — This flag can be used for type testing. Default is true .
- `.radius : number` — The radius of the sphere.

## Methods
- `.applyMatrix4( matrix :Matrix4) :Sphere` — Transforms this sphere with the given 4x4 transformation matrix.
- `.clampPoint( point :Vector3, target :Vector3) :Vector3` — Clamps a point within the sphere. If the point is outside the sphere, it
will clamp it to the closest point on the edge of the sphere. Points
already inside the sphere will not be affected.
- `.clone() :Sphere` — Returns a new sphere with copied values from this instance.
- `.containsPoint( point :Vector3) : boolean` — Returns true if this sphere contains the given point inclusive of
the surface of the sphere.
- `.copy( sphere :Sphere) :Sphere` — Copies the values of the given sphere to this instance.
- `.distanceToPoint( point :Vector3) : number` — Returns the closest distance from the boundary of the sphere to the
given point. If the sphere contains the point, the distance will
be negative.
- `.equals( sphere :Sphere) : boolean` — Returns true if this sphere is equal with the given one.
- `.expandByPoint( point :Vector3) :Sphere` — Expands the boundaries of this sphere to include the given point.
- `.fromJSON( json :Object) :Sphere` — Returns a serialized structure of the bounding sphere.
- `.getBoundingBox( target :Box3) :Box3` — Returns a bounding box that encloses this sphere.
- `.intersectsBox( box :Box3) : boolean` — Returns true if this sphere intersects with the given box.
- `.intersectsPlane( plane :Plane) : boolean` — Returns true if this sphere intersects with the given plane.
- `.intersectsSphere( sphere :Sphere) : boolean` — Returns true if this sphere intersects with the given one.
- `.isEmpty() : boolean` — Returns true if the sphere is empty (the radius set to a negative number). Spheres with a radius of 0 contain only their center point and are not
considered to be empty.
- `.makeEmpty() :Sphere` — Makes this sphere empty which means in encloses a zero space in 3D.
- `.set( center :Vector3, radius :number) :Sphere` — Sets the sphere's components by copying the given values.
- `.setFromPoints( points :Array.<Vector3>, optionalCenter :Vector3) :Sphere` — Computes the minimum bounding sphere for list of points.
If the optional center point is given, it is used as the sphere's
center. Otherwise, the center of the axis-aligned bounding box
encompassin...
- `.toJSON() : Object` — Returns a serialized structure of the bounding sphere.
- `.translate( offset :Vector3) :Sphere` — Translates the sphere's center by the given offset.
- `.union( sphere :Sphere) :Sphere` — Expands this sphere to enclose both the original sphere and the given sphere.

## Source