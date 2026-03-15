# Box3

Represents an axis-aligned bounding box (AABB) in 3D space.

## Constructor
`newBox3( min :Vector3, max :Vector3)`
Constructs a new bounding box.

## Properties
- `.isBox3 : boolean` — This flag can be used for type testing. Default is true .
- `.max :Vector3` — The upper boundary of the box.
- `.min :Vector3` — The lower boundary of the box.

## Methods
- `.applyMatrix4( matrix :Matrix4) :Box3` — Transforms this bounding box by the given 4x4 transformation matrix.
- `.clampPoint( point :Vector3, target :Vector3) :Vector3` — Clamps the given point within the bounds of this box.
- `.clone() :Box3` — Returns a new box with copied values from this instance.
- `.containsBox( box :Box3) : boolean` — Returns true if this bounding box includes the entirety of the given bounding box.
If this box and the given one are identical, this function also returns true .
- `.containsPoint( point :Vector3) : boolean` — Returns true if the given point lies within or on the boundaries of this box.
- `.copy( box :Box3) :Box3` — Copies the values of the given box to this instance.
- `.distanceToPoint( point :Vector3) : number` — Returns the euclidean distance from any edge of this box to the specified point. If
the given point lies inside of this box, the distance will be 0 .
- `.equals( box :Box3) : boolean` — Returns true if this bounding box is equal with the given one.
- `.expandByObject( object :Object3D, precise :boolean) :Box3` — Expands the boundaries of this box to include the given 3D object and
its children, accounting for the object's, and children's, world
transforms. The function may result in a larger box than stric...
- `.expandByPoint( point :Vector3) :Box3` — Expands the boundaries of this box to include the given point.
- `.expandByScalar( scalar :number) :Box3` — Expands each dimension of the box by the given scalar. If negative, the
dimensions of the box will be contracted.
- `.expandByVector( vector :Vector3) :Box3` — Expands this box equilaterally by the given vector. The width of this
box will be expanded by the x component of the vector in both
directions. The height of this box will be expanded by the y comp...
- `.fromJSON( json :Object) :Box3` — Returns a serialized structure of the bounding box.
- `.getBoundingSphere( target :Sphere) :Sphere` — Returns a bounding sphere that encloses this bounding box.
- `.getCenter( target :Vector3) :Vector3` — Returns the center point of this box.
- `.getParameter( point :Vector3, target :Vector3) :Vector3` — Returns a point as a proportion of this box's width, height and depth.
- `.getSize( target :Vector3) :Vector3` — Returns the dimensions of this box.
- `.intersect( box :Box3) :Box3` — Computes the intersection of this bounding box and the given one, setting the upper
bound of this box to the lesser of the two boxes' upper bounds and the
lower bound of this box to the greater of ...
- `.intersectsBox( box :Box3) : boolean` — Returns true if the given bounding box intersects with this bounding box.
- `.intersectsPlane( plane :Plane) : boolean` — Returns true if the given plane intersects with this bounding box.
- `.intersectsSphere( sphere :Sphere) : boolean` — Returns true if the given bounding sphere intersects with this bounding box.
- `.intersectsTriangle( triangle :Triangle) : boolean` — Returns true if the given triangle intersects with this bounding box.
- `.isEmpty() : boolean` — Returns true if this box includes zero points within its bounds.
Note that a box with equal lower and upper bounds still includes one
point, the one both bounds share.
- `.makeEmpty() :Box3` — Makes this box empty which means in encloses a zero space in 3D.
- `.set( min :Vector3, max :Vector3) :Box3` — Sets the lower and upper boundaries of this box.
Please note that this method only copies the values from the given objects.
- `.setFromArray( array :Array.<number>) :Box3` — Sets the upper and lower bounds of this box so it encloses the position data
in the given array.
- `.setFromBufferAttribute( attribute :BufferAttribute) :Box3` — Sets the upper and lower bounds of this box so it encloses the position data
in the given buffer attribute.
- `.setFromCenterAndSize( center :Vector3, size :Vector3) :Box3` — Centers this box on the given center vector and sets this box's width, height and
depth to the given size values.
- `.setFromObject( object :Object3D, precise :boolean) :Box3` — Computes the world-axis-aligned bounding box for the given 3D object
(including its children), accounting for the object's, and children's,
world transforms. The function may result in a larger box...
- `.setFromPoints( points :Array.<Vector3>) :Box3` — Sets the upper and lower bounds of this box so it encloses the position data
in the given array.
- `.toJSON() : Object` — Returns a serialized structure of the bounding box.
- `.translate( offset :Vector3) :Box3` — Adds the given offset to both the upper and lower bounds of this bounding box,
effectively moving it in 3D space.
- `.union( box :Box3) :Box3` — Computes the union of this box and another and the given one, setting the upper
bound of this box to the greater of the two boxes' upper bounds and the
lower bound of this box to the lesser of the ...

## Source