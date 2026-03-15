# ExtrudeGeometry
Extends: EventDispatcher→BufferGeometry→

Creates extruded geometry from a path shape.

## Constructor
`newExtrudeGeometry( shapes :Shape| Array.<Shape>, options :ExtrudeGeometry~Options)`
Constructs a new extrude geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object, shapes :Array.<Shape>) :ExtrudeGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Type Definitions
- `.Options` — Represents the options type of the geometry's constructor.

## Source