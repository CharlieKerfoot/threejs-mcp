# CylinderGeometry
Extends: EventDispatcher→BufferGeometry→

A geometry class for representing a cylinder.

## Constructor
`newCylinderGeometry( radiusTop :number, radiusBottom :number, height :number, radialSegments :number, heightSegments :number, openEnded :boolean, thetaStart :number, thetaLength :number)`
Constructs a new cylinder geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :CylinderGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source