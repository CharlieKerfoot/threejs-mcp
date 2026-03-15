# SphereGeometry
Extends: EventDispatcher→BufferGeometry→

A class for generating a sphere geometry.

## Constructor
`newSphereGeometry( radius :number, widthSegments :number, heightSegments :number, phiStart :number, phiLength :number, thetaStart :number, thetaLength :number)`
Constructs a new sphere geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :SphereGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source