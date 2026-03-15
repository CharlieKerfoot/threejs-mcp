# OBB

Represents an oriented bounding box (OBB) in 3D space.

## Constructor
`newOBB( center :Vector3, halfSize :Vector3, rotation :Matrix3)`
Constructs a new OBB.

## Import

## Properties
- `.center :Vector3` — The center of the OBB.
- `.halfSize :Vector3` — Positive halfwidth extents of the OBB along each axis.
- `.rotation :Matrix3` — The rotation of the OBB.

## Methods
- `.applyMatrix4( matrix :Matrix4) :OBB` — Applies the given transformation matrix to this OBB. This method can be
used to transform the bounding volume with the world matrix of a 3D object
in order to keep both entities in sync.
- `.clampPoint( point :Vector3, target :Vector3) :Vector3` — Clamps the given point within the bounds of this OBB.
- `.clone() :OBB` — Returns a new OBB with copied values from this instance.
- `.containsPoint( point :Vector3) : boolean` — Returns true if the given point lies within this OBB.
- `.copy( obb :OBB) :OBB` — Copies the values of the given OBB to this instance.
- `.equals( obb :OBB) : boolean` — Returns true if the given OBB is equal to this OBB.
- `.fromBox3( box3 :Box3) :OBB` — Defines an OBB based on the given AABB.
- `.getSize( target :Vector3) :Vector3` — Returns the size of this OBB.
- `.intersectRay( ray :Ray, target :Vector3) :Vector3` — Performs a ray/OBB intersection test and stores the intersection point
in the given 3D vector.
- `.intersectsBox3( box3 :Box3) : boolean` — Returns true if the given AABB intersects this OBB.
- `.intersectsOBB( obb :OBB, epsilon :number) : boolean` — Returns true if the given OBB intersects this OBB.
- `.intersectsPlane( plane :Plane) : boolean` — Returns true if the given plane intersects this OBB.
- `.intersectsRay( ray :Ray) : boolean` — Returns true if the given ray intersects this OBB.
- `.intersectsSphere( sphere :Sphere) : boolean` — Returns true if the given bounding sphere intersects this OBB.
- `.set( center :Vector3, halfSize :Vector3, rotation :Matrix3) :OBB` — Sets the OBBs components to the given values.

## Source