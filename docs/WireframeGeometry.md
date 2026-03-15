# WireframeGeometry
Extends: EventDispatcher→BufferGeometry→

Can be used as a helper object to visualize a geometry as a wireframe. Note: It is not yet possible to serialize/deserialize instances of this class.

## Constructor
`newWireframeGeometry( geometry :BufferGeometry)`
Constructs a new wireframe geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Source