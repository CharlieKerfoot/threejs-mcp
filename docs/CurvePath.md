# CurvePath
Extends: Curve→

A base class extending Curve . CurvePath is simply an
array of connected curves, but retains the API of a curve.

## Constructor
`newCurvePath()`
Constructs a new curve path.

## Properties
- `.autoClose : boolean` — Whether the path should automatically be closed
by a line curve. Default is false .
- `.curves : Array.<Curve>` — An array of curves defining the
path.

## Methods
- `.add( curve :Curve)` — Adds a curve to this curve path.
- `.closePath() :CurvePath` — Adds a line curve to close the path.
- `.getCurveLengths() : Array.<number>` — Returns list of cumulative curve lengths of the defined curves.
- `.getPoint( t :number, optionalTarget :Vector2|Vector3) :Vector2|Vector3` — This method returns a vector in 2D or 3D space (depending on the curve definitions)
for the given interpolation factor.

## Source