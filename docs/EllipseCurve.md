# EllipseCurve
Extends: Curve→

A curve representing an ellipse.

## Constructor
`newEllipseCurve( aX :number, aY :number, xRadius :number, yRadius :number, aStartAngle :number, aEndAngle :number, aClockwise :boolean, aRotation :number)`
Constructs a new ellipse curve.

## Properties
- `.aClockwise : boolean` — Whether the ellipse is drawn clockwise or not. Default is false .
- `.aEndAngle : number` — The end angle of the curve in radians starting from the positive X axis. Default is Math.PI*2 .
- `.aRotation : number` — The rotation angle of the ellipse in radians, counterclockwise from the positive X axis. Default is 0 .
- `.aStartAngle : number` — The start angle of the curve in radians starting from the positive X axis. Default is 0 .
- `.aX : number` — The X center of the ellipse. Default is 0 .
- `.aY : number` — The Y center of the ellipse. Default is 0 .
- `.isEllipseCurve : boolean` — This flag can be used for type testing. Default is true .
- `.xRadius : number` — The radius of the ellipse in the x direction.
Setting the this value equal to the EllipseCurve#yRadius will result in a circle. Default is 1 .
- `.yRadius : number` — The radius of the ellipse in the y direction.
Setting the this value equal to the EllipseCurve#xRadius will result in a circle. Default is 1 .

## Methods
- `.getPoint( t :number, optionalTarget :Vector2) :Vector2` — Returns a point on the curve.

## Source