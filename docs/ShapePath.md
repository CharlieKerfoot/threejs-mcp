# ShapePath

This class is used to convert a series of paths to an array of
shapes. It is specifically used in context of fonts and SVG.

## Constructor
`newShapePath()`
Constructs a new shape path.

## Properties
- `.color :Color` — The color of the shape.
- `.currentPath :Path` — The current path that is being generated. Default is null .
- `.subPaths : Array.<Path>` — The paths that have been generated for this shape. Default is null .

## Methods
- `.bezierCurveTo( aCP1x :number, aCP1y :number, aCP2x :number, aCP2y :number, aX :number, aY :number) :ShapePath` — Adds an instance of CubicBezierCurve to the path by connecting
the current point with the given one.
- `.lineTo( x :number, y :number) :ShapePath` — Adds an instance of LineCurve to the path by connecting
the current point with the given one.
- `.moveTo( x :number, y :number) :ShapePath` — Creates a new path and moves it current point to the given one.
- `.quadraticCurveTo( aCPx :number, aCPy :number, aX :number, aY :number) :ShapePath` — Adds an instance of QuadraticBezierCurve to the path by connecting
the current point with the given one.
- `.splineThru( pts :Array.<Vector2>) :ShapePath` — Adds an instance of SplineCurve to the path by connecting
the current point with the given list of points.
- `.toShapes( isCCW :boolean) : Array.<Shape>` — Converts the paths into an array of shapes.

## Source