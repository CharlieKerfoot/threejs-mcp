# LineLoop
Extends: EventDispatcher→Object3D→Line→

A continuous line. This is nearly the same as Line the only difference
is that the last vertex is connected with the first vertex in order to close
the line to form a loop.

## Constructor
`newLineLoop( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new line loop.

## Properties
- `.isLineLoop : boolean` — This flag can be used for type testing. Default is true .

## Source