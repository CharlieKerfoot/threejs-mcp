# EdgesGeometry
Extends: EventDispatcher→BufferGeometry→

Can be used as a helper object to view the edges of a geometry. Note: It is not yet possible to serialize/deserialize instances of this class.

## Constructor
`newEdgesGeometry( geometry :BufferGeometry, thresholdAngle :number)`
Constructs a new edges geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Source