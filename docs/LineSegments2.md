# LineSegments2
Extends: EventDispatcher→Object3D→Mesh→

A series of lines drawn between pairs of vertices. This adds functionality beyond LineSegments , like arbitrary line width and changing width
to be in world units. Line2 extends this object, forming a polyline instead of individual
segments. This module can only be used with WebGLRenderer . When using WebGPURenderer ,
import the class from lines/webgpu/LineSegments2.js .

## Constructor
`newLineSegments2( geometry :LineSegmentsGeometry, material :LineMaterial)`
Constructs a new wide line.

## Import

## Properties
- `.isLineSegments2 : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.computeLineDistances() :LineSegments2` — Computes an array of distance values which are necessary for rendering dashed lines.
For each vertex in the geometry, the method calculates the cumulative length from the
current point to the very ...
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>)` — Computes intersection points between a casted ray and this instance.

## Source