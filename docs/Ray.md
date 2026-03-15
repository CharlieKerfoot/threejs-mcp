# Ray

A ray that emits from an origin in a certain direction. The class is used by Raycaster to assist with raycasting. Raycasting is used for
mouse picking (working out what objects in the 3D space the mouse is over)
amongst other things.

## Constructor
`newRay( origin :Vector3, direction :Vector3)`
Constructs a new ray.

## Properties
- `.direction :Vector3` — The (normalized) direction of the ray.
- `.origin :Vector3` — The origin of the ray.

## Methods
- `.applyMatrix4( matrix4 :Matrix4) :Ray` — Transforms this ray with the given 4x4 transformation matrix.
- `.at( t :number, target :Vector3) :Vector3` — Returns a vector that is located at a given distance along this ray.
- `.clone() :Ray` — Returns a new ray with copied values from this instance.
- `.closestPointToPoint( point :Vector3, target :Vector3) :Vector3` — Returns the point along this ray that is closest to the given point.
- `.copy( ray :Ray) :Ray` — Copies the values of the given ray to this instance.
- `.distanceSqToPoint( point :Vector3) : number` — Returns the squared distance of the closest approach between this ray and the given point.
- `.distanceSqToSegment( v0 :Vector3, v1 :Vector3, optionalPointOnRay :Vector3, optionalPointOnSegment :Vector3) : number` — Returns the squared distance between this ray and the given line segment.
- `.distanceToPlane( plane :Plane) : number` — Computes the distance from the ray's origin to the given plane. Returns null if the ray
does not intersect with the plane.
- `.distanceToPoint( point :Vector3) : number` — Returns the distance of the closest approach between this ray and the given point.
- `.equals( ray :Ray) : boolean` — Returns true if this ray is equal with the given one.
- `.intersectBox( box :Box3, target :Vector3) :Vector3` — Intersects this ray with the given bounding box, returning the intersection
point or null if there is no intersection.
- `.intersectPlane( plane :Plane, target :Vector3) :Vector3` — Intersects this ray with the given plane, returning the intersection
point or null if there is no intersection.
- `.intersectSphere( sphere :Sphere, target :Vector3) :Vector3` — Intersects this ray with the given sphere, returning the intersection
point or null if there is no intersection.
- `.intersectTriangle( a :Vector3, b :Vector3, c :Vector3, backfaceCulling :boolean, target :Vector3) :Vector3` — Intersects this ray with the given triangle, returning the intersection
point or null if there is no intersection.
- `.intersectsBox( box :Box3) : boolean` — Returns true if this ray intersects with the given box.
- `.intersectsPlane( plane :Plane) : boolean` — Returns true if this ray intersects with the given plane.
- `.intersectsSphere( sphere :Sphere) : boolean` — Returns true if this ray intersects with the given sphere.
- `.lookAt( v :Vector3) :Ray` — Adjusts the direction of the ray to point at the given vector in world space.
- `.recast( t :number) :Ray` — Shift the origin of this ray along its direction by the given distance.
- `.set( origin :Vector3, direction :Vector3) :Ray` — Sets the ray's components by copying the given values.

## Source