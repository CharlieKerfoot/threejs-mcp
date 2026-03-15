# LineGeometry
Extends: InstancedBufferGeometry→LineSegmentsGeometry→

A chain of vertices, forming a polyline. This is used in Line2 to describe the shape.

## Constructor
`newLineGeometry()`
Constructs a new line geometry.

## Import

## Properties
- `.isLineGeometry : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.fromLine( line :Line) :LineGeometry` — Setups this line segments geometry from the given line.
- `.setColors( array :Float32Array | Array.<number>) :LineGeometry` — Sets the given line colors for this geometry.
- `.setFromPoints( points :Array.<(Vector3|Vector2)>) :LineGeometry` — Setups this line segments geometry from the given sequence of points.
- `.setPositions( array :Float32Array | Array.<number>) :LineGeometry` — Sets the given line positions for this geometry.

## Source