# ConvexHull

Can be used to compute the convex hull in 3D space for a given set of points. It
is primarily intended for ConvexGeometry . This Quickhull 3D implementation is a port of quickhull3d by Mauricio Poppe.

## Constructor
`newConvexHull()`
Constructs a new convex hull.

## Import

## Methods
- `.containsPoint( point :Vector3) : boolean` — Returns true if the given point lies in the convex hull.
- `.intersectRay( ray :Ray, target :Vector3) :Vector3` — Computes the intersections point of the given ray and this convex hull.
- `.intersectsRay( ray :Ray) : boolean` — Returns true if the given ray intersects with this convex hull.
- `.makeEmpty() :ConvexHull` — Makes the convex hull empty.
- `.setFromObject( object :Object3D) :ConvexHull` — Computes the convex hull of the given 3D object (including its descendants),
accounting for the world transforms of both the 3D object and its descendants.
- `.setFromPoints( points :Array.<Vector3>) :ConvexHull` — Computes to convex hull for the given array of points.

## Source