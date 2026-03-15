# CubicBezierCurve
Extends: Curve→

A curve representing a 2D Cubic Bezier curve.

## Constructor
`newCubicBezierCurve( v0 :Vector2, v1 :Vector2, v2 :Vector2, v3 :Vector2)`
Constructs a new Cubic Bezier curve.

## Properties
- `.isCubicBezierCurve : boolean` — This flag can be used for type testing. Default is true .
- `.v0 :Vector2` — The start point.
- `.v1 :Vector2` — The first control point.
- `.v2 :Vector2` — The second control point.
- `.v3 :Vector2` — The end point.

## Methods
- `.getPoint( t :number, optionalTarget :Vector2) :Vector2` — Returns a point on the curve.

## Source