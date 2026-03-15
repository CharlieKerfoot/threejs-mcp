# PlaneGeometry
Extends: EventDispatcher→BufferGeometry→

A geometry class for representing a plane.

## Constructor
`newPlaneGeometry( width :number, height :number, widthSegments :number, heightSegments :number)`
Constructs a new plane geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :PlaneGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source