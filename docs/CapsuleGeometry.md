# CapsuleGeometry
Extends: EventDispatcher→BufferGeometry→

A geometry class for representing a capsule.

## Constructor
`newCapsuleGeometry( radius :number, height :number, capSegments :number, radialSegments :number, heightSegments :number)`
Constructs a new capsule geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :CapsuleGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source