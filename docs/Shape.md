# Shape
Extends: Curve→CurvePath→Path→

Defines an arbitrary 2d shape plane using paths with optional holes. It
can be used with ExtrudeGeometry , ShapeGeometry , to get
points, or to get triangulated faces.

## Constructor
`newShape( points :Array.<Vector2>)`
Constructs a new shape.

## Properties
- `.holes : Array.<Path>` — Defines the holes in the shape. Hole definitions must use the
opposite winding order (CW/CCW) than the outer shape.
- `.uuid : string` — The UUID of the shape.

## Methods
- `.extractPoints( divisions :number) : Object` — Returns an object that holds contour data for the shape and its holes as
arrays of 2D points.
- `.getPointsHoles( divisions :number) : Array.<Array.<Vector2>>` — Returns an array representing each contour of the holes
as a list of 2D points.

## Source