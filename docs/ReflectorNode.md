# ReflectorNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

This node can be used to implement mirror-like flat reflective surfaces.

## Constructor
`newReflectorNode( parameters :Object)`
Constructs a new reflector node.

## Properties
- `.reflector :ReflectorBaseNode` — A reference to the internal reflector node.
- `.target :Object3D` — A reference to 3D object the reflector is linked to.

## Methods
- `.dispose()` — Frees internal resources. Should be called when the node is no longer in use.
- `.getDepthNode() :Node` — Returns a node representing the mirror's depth. That can be used
to implement more advanced reflection effects like distance attenuation.

## Source