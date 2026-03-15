# TorusGeometry
Extends: EventDispatcher→BufferGeometry→

A geometry class for representing an torus.

## Constructor
`newTorusGeometry( radius :number, tube :number, radialSegments :number, tubularSegments :number, arc :number, thetaStart :number, thetaLength :number)`
Constructs a new torus geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :TorusGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source