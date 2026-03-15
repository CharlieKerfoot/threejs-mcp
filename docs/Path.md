# Path
Extends: Curve→CurvePath→

A 2D path representation. The class provides methods for creating paths
and contours of 2D shapes similar to the 2D Canvas API.

## Constructor
`newPath( points :Array.<Vector2>)`
Constructs a new path.

## Properties
- `.currentPoint :Vector2` — The current offset of the path. Any new curve added will start here.

## Methods
- `.absarc( aX :number, aY :number, aRadius :number, aStartAngle :number, aEndAngle :number, aClockwise :boolean) :Path` — Adds an absolutely positioned arc as an instance of EllipseCurve to the path.
- `.absellipse( aX :number, aY :number, xRadius :number, yRadius :number, aStartAngle :number, aEndAngle :number, aClockwise :boolean, aRotation :number) :Path` — Adds an absolutely positioned ellipse as an instance of EllipseCurve to the path.
- `.arc( aX :number, aY :number, aRadius :number, aStartAngle :number, aEndAngle :number, aClockwise :boolean) :Path` — Adds an arc as an instance of EllipseCurve to the path, positioned relative
to the current point.
- `.bezierCurveTo( aCP1x :number, aCP1y :number, aCP2x :number, aCP2y :number, aX :number, aY :number) :Path` — Adds an instance of CubicBezierCurve to the path by connecting
the current point with the given one.
- `.ellipse( aX :number, aY :number, xRadius :number, yRadius :number, aStartAngle :number, aEndAngle :number, aClockwise :boolean, aRotation :number) :Path` — Adds an ellipse as an instance of EllipseCurve to the path, positioned relative
to the current point
- `.lineTo( x :number, y :number) :Path` — Adds an instance of LineCurve to the path by connecting
the current point with the given one.
- `.moveTo( x :number, y :number) :Path` — Moves Path#currentPoint to the given point.
- `.quadraticCurveTo( aCPx :number, aCPy :number, aX :number, aY :number) :Path` — Adds an instance of QuadraticBezierCurve to the path by connecting
the current point with the given one.
- `.setFromPoints( points :Array.<Vector2>) :Path` — Creates a path from the given list of points. The points are added
to the path as instances of LineCurve .
- `.splineThru( pts :Array.<Vector2>) :Path` — Adds an instance of SplineCurve to the path by connecting
the current point with the given list of points.

## Source