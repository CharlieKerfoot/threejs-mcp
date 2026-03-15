# QuadraticBezierCurve
Extends: Curve→

A curve representing a 2D Quadratic Bezier curve.

## Constructor
`newQuadraticBezierCurve( v0 :Vector2, v1 :Vector2, v2 :Vector2)`
Constructs a new Quadratic Bezier curve.

## Properties
- `.isQuadraticBezierCurve : boolean` — This flag can be used for type testing. Default is true .
- `.v0 :Vector2` — The start point.
- `.v1 :Vector2` — The control point.
- `.v2 :Vector2` — The end point.

## Methods
- `.getPoint( t :number, optionalTarget :Vector2) :Vector2` — Returns a point on the curve.

## Source