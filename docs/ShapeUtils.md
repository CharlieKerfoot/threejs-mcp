# ShapeUtils

A class containing utility functions for shapes.

## Static Methods
- `.area( contour :Array.<Vector2>) : number` — Calculate area of a ( 2D ) contour polygon.
- `.isClockWise( pts :Array.<Vector2>) : boolean` — Returns true if the given contour uses a clockwise winding order.
- `.triangulateShape( contour :Array.<Vector2>, holes :Array.<Array.<Vector2>>) : Array.<Array.<number>>` — Triangulates the given shape definition.

## Source