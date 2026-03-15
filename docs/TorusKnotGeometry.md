# TorusKnotGeometry
Extends: EventDispatcher→BufferGeometry→

Creates a torus knot, the particular shape of which is defined by a pair
of coprime integers, p and q. If p and q are not coprime, the result will
be a torus link.

## Constructor
`newTorusKnotGeometry( radius :number, tube :number, tubularSegments :number, radialSegments :number, p :number, q :number)`
Constructs a new torus knot geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :TorusKnotGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source