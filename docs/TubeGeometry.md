# TubeGeometry
Extends: EventDispatcher→BufferGeometry→

Creates a tube that extrudes along a 3D curve.

## Constructor
`newTubeGeometry( path :Curve, tubularSegments :number, radius :number, radialSegments :number, closed :boolean)`
Constructs a new tube geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :TubeGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source