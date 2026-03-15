# NURBSSurface

This class represents a NURBS surface. Implementation is based on (x, y [, z=0 [, w=1]]) control points with w=weight .

## Constructor
`newNURBSSurface( degree1 :number, degree2 :number, knots1 :Array.<number>, knots2 :Array.<number>, controlPoints :Array.<Array.<(Vector2|Vector3|Vector4)>>)`
Constructs a new NURBS surface.

## Import

## Properties
- `.controlPoints : Array.<Array.<(Vector2|Vector3|Vector4)>>` — An array holding arrays of control points.
- `.degree1 : number` — The first NURBS degree.
- `.degree2 : number` — The second NURBS degree.
- `.knots1 : Array.<number>` — The first knots as a flat array of numbers.
- `.knots2 : Array.<number>` — The second knots as a flat array of numbers.

## Methods
- `.getPoint( t1 :number, t2 :number, target :Vector3)` — This method returns a vector in 3D space for the given interpolation factor. This vector lies on the NURBS surface.

## Source