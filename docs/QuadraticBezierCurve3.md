# QuadraticBezierCurve3
Extends: Curve→

A curve representing a 3D Quadratic Bezier curve.

## Constructor
`newQuadraticBezierCurve3( v0 :Vector3, v1 :Vector3, v2 :Vector3)`
Constructs a new Quadratic Bezier curve.

## Properties
- `.isQuadraticBezierCurve3 : boolean` — This flag can be used for type testing. Default is true .
- `.v0 :Vector3` — The start point.
- `.v1 :Vector3` — The control point.
- `.v2 :Vector3` — The end point.

## Methods
- `.getPoint( t :number, optionalTarget :Vector3) :Vector3` — Returns a point on the curve.

## Source