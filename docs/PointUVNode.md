# PointUVNode
Extends: EventDispatcher→Node→

A node for representing the uv coordinates of points. Can only be used with a WebGL backend. In WebGPU, point
primitives always have the size of one pixel and can thus
can't be used as sprite-like objects that display textures.

## Constructor
`newPointUVNode()`
Constructs a new point uv node.

## Properties
- `.isPointUVNode : boolean` — This flag can be used for type testing. Default is true .

## Source