# BoxGeometry
Extends: EventDispatcher→BufferGeometry→

A geometry class for a rectangular cuboid with a given width, height, and depth.
On creation, the cuboid is centred on the origin, with each edge parallel to one
of the axes.

## Constructor
`newBoxGeometry( width :number, height :number, depth :number, widthSegments :number, heightSegments :number, depthSegments :number)`
Constructs a new box geometry.

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Static Methods
- `.fromJSON( data :Object) :BoxGeometry` — Factory method for creating an instance of this class from the given
JSON object.

## Source