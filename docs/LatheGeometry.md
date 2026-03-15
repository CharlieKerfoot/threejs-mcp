# LatheGeometry
Extends: EventDispatcher→BufferGeometry→

Creates meshes with axial symmetry like vases. The lathe rotates around the Y axis.

## Constructor
`newLatheGeometry( points :Array.<(Vector2|Vector3)>, segments :number, phiStart :number, phiLength :number)`
Constructs a new lathe geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :LatheGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source