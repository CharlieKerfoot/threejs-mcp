# Line3

An analytical line segment in 3D space represented by a start and end point.

## Constructor
`newLine3( start :Vector3, end :Vector3)`
Constructs a new line segment.

## Properties
- `.end :Vector3` — End of the line segment.
- `.start :Vector3` — Start of the line segment.

## Methods
- `.applyMatrix4( matrix :Matrix4) :Line3` — Applies a 4x4 transformation matrix to this line segment.
- `.at( t :number, target :Vector3) :Vector3` — Returns a vector at a certain position along the line segment.
- `.clone() :Line3` — Returns a new line segment with copied values from this instance.
- `.closestPointToPoint( point :Vector3, clampToLine :boolean, target :Vector3) :Vector3` — Returns the closest point on the line for a given point.
- `.closestPointToPointParameter( point :Vector3, clampToLine :boolean) : number` — Returns a point parameter based on the closest point as projected on the line segment.
- `.copy( line :Line3) :Line3` — Copies the values of the given line segment to this instance.
- `.delta( target :Vector3) :Vector3` — Returns the delta vector of the line segment's start and end point.
- `.distance() : number` — Returns the Euclidean distance between the line' start and end point.
- `.distanceSq() : number` — Returns the squared Euclidean distance between the line' start and end point.
- `.distanceSqToLine3( line :Line3, c1 :Vector3, c2 :Vector3) : number` — Returns the closest squared distance between this line segment and the given one.
- `.equals( line :Line3) : boolean` — Returns true if this line segment is equal with the given one.
- `.getCenter( target :Vector3) :Vector3` — Returns the center of the line segment.
- `.set( start :Vector3, end :Vector3) :Line3` — Sets the start and end values by copying the given vectors.

## Source