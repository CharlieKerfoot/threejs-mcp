# ViewportDepthTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→ViewportTextureNode→

Represents the depth of the current viewport as a texture. This module
can be used in combination with viewport texture to achieve effects
that require depth evaluation.

## Constructor
`newViewportDepthTextureNode( uvNode :Node, levelNode :Node)`
Constructs a new viewport depth texture node.

## Methods
- `.getTextureForReference() :DepthTexture` — Overwritten so the method always returns the unique shared
depth texture.

## Source