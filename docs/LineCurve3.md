# LineCurve3
Extends: Curve→

A curve representing a 3D line segment.

## Constructor
`newLineCurve3( v1 :Vector3, v2 :Vector3)`
Constructs a new line curve.

## Properties
- `.isLineCurve3 : boolean` — This flag can be used for type testing. Default is true .
- `.v1 :Vector3` — The start point.
- `.v2 :Vector2` — The end point.

## Methods
- `.getPoint( t :number, optionalTarget :Vector3) :Vector3` — Returns a point on the line.

## Source