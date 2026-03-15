# SplineCurve
Extends: Curve→

A curve representing a 2D spline curve.

## Constructor
`newSplineCurve( points :Array.<Vector2>)`
Constructs a new 2D spline curve.

## Properties
- `.isSplineCurve : boolean` — This flag can be used for type testing. Default is true .
- `.points : Array.<Vector2>` — An array of 2D points defining the curve.

## Methods
- `.getPoint( t :number, optionalTarget :Vector2) :Vector2` — Returns a point on the curve.

## Source