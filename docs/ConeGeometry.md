# ConeGeometry
Extends: EventDispatcher→BufferGeometry→CylinderGeometry→

A geometry class for representing a cone.

## Constructor
`newConeGeometry( radius :number, height :number, radialSegments :number, heightSegments :number, openEnded :boolean, thetaStart :number, thetaLength :number)`
Constructs a new cone geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :ConeGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source