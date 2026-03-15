# RingGeometry
Extends: EventDispatcher→BufferGeometry→

A class for generating a two-dimensional ring geometry.

## Constructor
`newRingGeometry( innerRadius :number, outerRadius :number, thetaSegments :number, phiSegments :number, thetaStart :number, thetaLength :number)`
Constructs a new ring geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :RingGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source