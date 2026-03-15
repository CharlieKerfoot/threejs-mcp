# TetrahedronGeometry
Extends: EventDispatcher→BufferGeometry→PolyhedronGeometry→

A geometry class for representing an tetrahedron.

## Constructor
`newTetrahedronGeometry( radius :number, detail :number)`
Constructs a new tetrahedron geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :TetrahedronGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source