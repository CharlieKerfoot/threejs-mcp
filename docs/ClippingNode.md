# ClippingNode
Extends: EventDispatcher→Node→

This node is used in NodeMaterial to setup the clipping
which can happen hardware-accelerated (if supported) and optionally
use alpha-to-coverage for anti-aliasing clipped edges.

## Constructor
`newClippingNode( scope :'default' | 'hardware' | 'alphaToCoverage')`
Constructs a new clipping node.

## Properties
- `.scope : 'default' | 'hardware' | 'alphaToCoverage'` — The node's scope. Similar to other nodes, the selected scope influences
the behavior of the node and what type of code is generated.

## Methods
- `.setup( builder :NodeBuilder) :Node` — Setups the node depending on the selected scope.
- `.setupAlphaToCoverage( intersectionPlanes :Array.<Vector4>, unionPlanes :Array.<Vector4>) :Node` — Setups alpha to coverage.
- `.setupDefault( intersectionPlanes :Array.<Vector4>, unionPlanes :Array.<Vector4>) :Node` — Setups the default clipping.
- `.setupHardwareClipping( unionPlanes :Array.<Vector4>, builder :NodeBuilder) :Node` — Setups hardware clipping.

## Source