# CircleGeometry
Extends: EventDispatcher→BufferGeometry→

A simple shape of Euclidean geometry. It is constructed from a
number of triangular segments that are oriented around a central point and
extend as far out as a given radius. It is built counter-clockwise from a
start angle and a given central angle. It can also be used to create
regular polygons, where the number of segments determines the number of
sides.

## Constructor
`newCircleGeometry( radius :number, segments :number, thetaStart :number, thetaLength :number)`
Constructs a new circle geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :CircleGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source