# ShapeGeometry
Extends: EventDispatcher→BufferGeometry→

Creates an one-sided polygonal geometry from one or more path shapes.

## Constructor
`newShapeGeometry( shapes :Shape| Array.<Shape>, curveSegments :number)`
Constructs a new shape geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object, shapes :Array.<Shape>) :ShapeGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source