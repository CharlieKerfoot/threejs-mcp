# Curve

An abstract base class for creating an analytic curve object that contains methods
for interpolation.

## Constructor
`newCurve()(abstract)`
Constructs a new curve.

## Properties
- `.arcLengthDivisions : number` — This value determines the amount of divisions when calculating the
cumulative segment lengths of a curve via Curve#getLengths . To ensure
precision when using methods like Curve#getSpacedPoints , i...
- `.needsUpdate : boolean` — Must be set to true if the curve parameters have changed. Default is false .
- `.type : string` — The type property is used for detecting the object type
in context of serialization/deserialization.

## Methods
- `.clone() :Curve` — Returns a new curve with copied values from this instance.
- `.computeFrenetFrames( segments :number, closed :boolean) : Object` — Generates the Frenet Frames. Requires a curve definition in 3D space. Used
in geometries like TubeGeometry or ExtrudeGeometry .
- `.copy( source :Curve) :Curve` — Copies the values of the given curve to this instance.
- `.fromJSON( json :Object) :Curve` — Deserializes the curve from the given JSON.
- `.getLength() : number` — Returns the total arc length of the curve.
- `.getLengths( divisions :number) : Array.<number>` — Returns an array of cumulative segment lengths of the curve.
- `.getPoint( t :number, optionalTarget :Vector2|Vector3) :Vector2|Vector3` — This method returns a vector in 2D or 3D space (depending on the curve definition)
for the given interpolation factor.
- `.getPointAt( u :number, optionalTarget :Vector2|Vector3) :Vector2|Vector3` — This method returns a vector in 2D or 3D space (depending on the curve definition)
for the given interpolation factor. Unlike Curve#getPoint , this method honors the length
of the curve which equid...
- `.getPoints( divisions :number) : Array.<(Vector2|Vector3)>` — This method samples the curve via Curve#getPoint and returns an array of points representing
the curve shape.
- `.getSpacedPoints( divisions :number) : Array.<(Vector2|Vector3)>` — This method samples the curve via Curve#getPointAt and returns an array of points representing
the curve shape. Unlike Curve#getPoints , this method returns equi-spaced points across the entire
curve.
- `.getTangent( t :number, optionalTarget :Vector2|Vector3) :Vector2|Vector3` — Returns a unit vector tangent for the given interpolation factor.
If the derived curve does not implement its tangent derivation,
two points a small delta apart will be used to find its gradient
wh...
- `.getTangentAt( u :number, optionalTarget :Vector2|Vector3) :Vector2|Vector3` — Same as Curve#getTangent but with equidistant samples.
- `.getUtoTmapping( u :number, distance :number) : number` — Given an interpolation factor in the range [0,1] , this method returns an updated
interpolation factor in the same range that can be ued to sample equidistant points
from a curve.
- `.toJSON() : Object` — Serializes the curve into JSON.
- `.updateArcLengths()` — Update the cumulative segment distance cache. The method must be called
every time curve parameters are changed. If an updated curve is part of a
composed curve like CurvePath , this method must be...

## Source