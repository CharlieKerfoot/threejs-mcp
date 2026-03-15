# CatmullRomCurve3
Extends: Curve→

A curve representing a Catmull-Rom spline.

## Constructor
`newCatmullRomCurve3( points :Array.<Vector3>, closed :boolean, curveType :'centripetal' | 'chordal' | 'catmullrom', tension :number)`
Constructs a new Catmull-Rom curve.

## Properties
- `.closed : boolean` — Whether the curve is closed or not. Default is false .
- `.curveType : 'centripetal' | 'chordal' | 'catmullrom'` — The curve type. Default is 'centripetal' .
- `.isCatmullRomCurve3 : boolean` — This flag can be used for type testing. Default is true .
- `.points : Array.<Vector3>` — An array of 3D points defining the curve.
- `.tension : number` — Tension of the curve. Default is 0.5 .

## Methods
- `.getPoint( t :number, optionalTarget :Vector3) :Vector3` — Returns a point on the curve.

## Source