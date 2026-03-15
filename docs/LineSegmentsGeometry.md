# LineSegmentsGeometry
Extends: InstancedBufferGeometry→

A series of vertex pairs, forming line segments. This is used in LineSegments2 to describe the shape.

## Constructor
`newLineSegmentsGeometry()`
Constructs a new line segments geometry.

## Import

## Properties
- `.isLineSegmentsGeometry : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.applyMatrix4( matrix :Matrix4) :LineSegmentsGeometry` — Applies the given 4x4 transformation matrix to the geometry.
- `.fromEdgesGeometry( geometry :EdgesGeometry) :LineSegmentsGeometry` — Setups this line segments geometry from the given edges geometry.
- `.fromLineSegments( lineSegments :LineSegments) :LineSegmentsGeometry` — Setups this line segments geometry from the given line segments.
- `.fromMesh( mesh :Mesh) :LineSegmentsGeometry` — Setups this line segments geometry from the given mesh.
- `.fromWireframeGeometry( geometry :WireframeGeometry) :LineSegmentsGeometry` — Setups this line segments geometry from the given wireframe geometry.
- `.setColors( array :Float32Array | Array.<number>) :LineSegmentsGeometry` — Sets the given line colors for this geometry. The length must be a multiple of six since
each line segment is defined by a start end color in the pattern (rgb rgb) .
- `.setPositions( array :Float32Array | Array.<number>) :LineSegmentsGeometry` — Sets the given line positions for this geometry. The length must be a multiple of six since
each line segment is defined by a start end vertex in the pattern (xyz xyz) .

## Source