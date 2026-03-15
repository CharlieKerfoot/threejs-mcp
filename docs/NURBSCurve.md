# NURBSCurve
Extends: Curve→

This class represents a NURBS curve. Implementation is based on (x, y [, z=0 [, w=1]]) control points with w=weight .

## Constructor
`newNURBSCurve( degree :number, knots :Array.<number>, controlPoints :Array.<(Vector2|Vector3|Vector4)>, startKnot :number, endKnot :number)`
Constructs a new NURBS curve.

## Import

## Properties
- `.controlPoints : Array.<Vector4>` — An array of control points.
- `.degree : number` — The NURBS degree.
- `.endKnot : number` — Index of the end knot into the knots array.
- `.knots : Array.<number>` — The knots as a flat array of numbers.
- `.startKnot : number` — Index of the start knot into the knots array.

## Methods
- `.getPoint( t :number, optionalTarget :Vector3) :Vector3` — This method returns a vector in 3D space for the given interpolation factor.
- `.getTangent( t :number, optionalTarget :Vector3) :Vector3` — Returns a unit vector tangent for the given interpolation factor.

## Source