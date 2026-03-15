# LineCurve
Extends: Curve→

A curve representing a 2D line segment.

## Constructor
`newLineCurve( v1 :Vector2, v2 :Vector2)`
Constructs a new line curve.

## Properties
- `.isLineCurve : boolean` — This flag can be used for type testing. Default is true .
- `.v1 :Vector2` — The start point.
- `.v2 :Vector2` — The end point.

## Methods
- `.getPoint( t :number, optionalTarget :Vector2) :Vector2` — Returns a point on the line.

## Source