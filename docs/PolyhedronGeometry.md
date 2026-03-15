# PolyhedronGeometry
Extends: EventDispatcher→BufferGeometry→

A polyhedron is a solid in three dimensions with flat faces. This class
will take an array of vertices, project them onto a sphere, and then
divide them up to the desired level of detail.

## Constructor
`newPolyhedronGeometry( vertices :Array.<number>, indices :Array.<number>, radius :number, detail :number)`
Constructs a new polyhedron geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :PolyhedronGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source