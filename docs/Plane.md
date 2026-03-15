# Plane

A two dimensional surface that extends infinitely in 3D space, represented
in Hessian normal form by a unit length normal vector and a constant.

## Constructor
`newPlane( normal :Vector3, constant :number)`
Constructs a new plane.

## Properties
- `.constant : number` — The signed distance from the origin to the plane. Default is 0 .
- `.isPlane : boolean` — This flag can be used for type testing. Default is true .
- `.normal :Vector3` — A unit length vector defining the normal of the plane.

## Methods
- `.applyMatrix4( matrix :Matrix4, optionalNormalMatrix :Matrix4) :Plane` — Apply a 4x4 matrix to the plane. The matrix must be an affine, homogeneous transform. The optional normal matrix can be pre-computed like so: const optionalNormalMatrix = new THREE.Matrix3().getNor...
- `.clone() :Plane` — Returns a new plane with copied values from this instance.
- `.coplanarPoint( target :Vector3) :Vector3` — Returns a coplanar vector to the plane, by calculating the
projection of the normal at the origin onto the plane.
- `.copy( plane :Plane) :Plane` — Copies the values of the given plane to this instance.
- `.distanceToPoint( point :Vector3) : number` — Returns the signed distance from the given point to this plane.
- `.distanceToSphere( sphere :Sphere) : number` — Returns the signed distance from the given sphere to this plane.
- `.equals( plane :Plane) : boolean` — Returns true if this plane is equal with the given one.
- `.intersectLine( line :Line3, target :Vector3) :Vector3` — Returns the intersection point of the passed line and the plane. Returns null if the line does not intersect. Returns the line's starting point if
the line is coplanar with the plane.
- `.intersectsBox( box :Box3) : boolean` — Returns true if the given bounding box intersects with the plane.
- `.intersectsLine( line :Line3) : boolean` — Returns true if the given line segment intersects with (passes through) the plane.
- `.intersectsSphere( sphere :Sphere) : boolean` — Returns true if the given bounding sphere intersects with the plane.
- `.negate() :Plane` — Negates both the plane normal and the constant.
- `.normalize() :Plane` — Normalizes the plane normal and adjusts the constant accordingly.
- `.projectPoint( point :Vector3, target :Vector3) :Vector3` — Projects a the given point onto the plane.
- `.set( normal :Vector3, constant :number) :Plane` — Sets the plane components by copying the given values.
- `.setComponents( x :number, y :number, z :number, w :number) :Plane` — Sets the plane components by defining x , y , z as the
plane normal and w as the constant.
- `.setFromCoplanarPoints( a :Vector3, b :Vector3, c :Vector3) :Plane` — Sets the plane from three coplanar points. The winding order is
assumed to be counter-clockwise, and determines the direction of
the plane normal.
- `.setFromNormalAndCoplanarPoint( normal :Vector3, point :Vector3) :Plane` — Sets the plane from the given normal and coplanar point (that is a point
that lies onto the plane).
- `.translate( offset :Vector3) :Plane` — Translates the plane by the distance defined by the given offset vector.
Note that this only affects the plane constant and will not affect the normal vector.

## Source