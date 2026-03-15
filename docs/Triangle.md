# Triangle

A geometric triangle as defined by three vectors representing its three corners.

## Constructor
`newTriangle( a :Vector3, b :Vector3, c :Vector3)`
Constructs a new triangle.

## Properties
- `.a :Vector3` — The first corner of the triangle.
- `.b :Vector3` — The second corner of the triangle.
- `.c :Vector3` — The third corner of the triangle.

## Methods
- `.clone() :Triangle` — Returns a new triangle with copied values from this instance.
- `.closestPointToPoint( p :Vector3, target :Vector3) :Vector3` — Returns the closest point on the triangle to the given point.
- `.containsPoint( point :Vector3) : boolean` — Returns true if the given point, when projected onto the plane of the
triangle, lies within the triangle.
- `.copy( triangle :Triangle) :Triangle` — Copies the values of the given triangle to this instance.
- `.equals( triangle :Triangle) : boolean` — Returns true if this triangle is equal with the given one.
- `.getArea() : number` — Computes the area of the triangle.
- `.getBarycoord( point :Vector3, target :Vector3) :Vector3` — Computes a barycentric coordinates from the given vector.
Returns null if the triangle is degenerate.
- `.getInterpolation( point :Vector3, v1 :Vector3, v2 :Vector3, v3 :Vector3, target :Vector3) :Vector3` — Computes the value barycentrically interpolated for the given point on the
triangle. Returns null if the triangle is degenerate.
- `.getMidpoint( target :Vector3) :Vector3` — Computes the midpoint of the triangle.
- `.getNormal( target :Vector3) :Vector3` — Computes the normal of the triangle.
- `.getPlane( target :Plane) :Plane` — Computes a plane the triangle lies within.
- `.intersectsBox( box :Box3) : boolean` — Returns true if this triangle intersects with the given box.
- `.isFrontFacing( direction :Vector3) : boolean` — Returns true if the triangle is oriented towards the given direction.
- `.set( a :Vector3, b :Vector3, c :Vector3) :Triangle` — Sets the triangle's vertices by copying the given values.
- `.setFromAttributeAndIndices( attribute :BufferAttribute, i0 :number, i1 :number, i2 :number) :Triangle` — Sets the triangle's vertices by copying the given attribute values.
- `.setFromPointsAndIndices( points :Array.<Vector3>, i0 :number, i1 :number, i2 :number) :Triangle` — Sets the triangle's vertices by copying the given array values.

## Static Methods
- `.containsPoint( point :Vector3, a :Vector3, b :Vector3, c :Vector3) : boolean` — Returns true if the given point, when projected onto the plane of the
triangle, lies within the triangle.
- `.getBarycoord( point :Vector3, a :Vector3, b :Vector3, c :Vector3, target :Vector3) :Vector3` — Computes a barycentric coordinates from the given vector.
Returns null if the triangle is degenerate.
- `.getInterpolatedAttribute( attr :BufferAttribute, i1 :number, i2 :number, i3 :number, barycoord :Vector3, target :Vector3) :Vector3` — Computes the value barycentrically interpolated for the given attribute and indices.
- `.getInterpolation( point :Vector3, p1 :Vector3, p2 :Vector3, p3 :Vector3, v1 :Vector3, v2 :Vector3, v3 :Vector3, target :Vector3) :Vector3` — Computes the value barycentrically interpolated for the given point on the
triangle. Returns null if the triangle is degenerate.
- `.getNormal( a :Vector3, b :Vector3, c :Vector3, target :Vector3) :Vector3` — Computes the normal vector of a triangle.
- `.isFrontFacing( a :Vector3, b :Vector3, c :Vector3, direction :Vector3) : boolean` — Returns true if the triangle is oriented towards the given direction.

## Source