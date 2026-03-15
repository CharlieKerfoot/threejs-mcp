# ViewportSharedTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→ViewportTextureNode→

ViewportTextureNode creates an internal texture for each node instance. This module
shares a texture across all instances of ViewportSharedTextureNode . It should
be the first choice when using data of the default/screen framebuffer for performance reasons.

## Constructor
`newViewportSharedTextureNode( uvNode :Node, levelNode :Node)`
Constructs a new viewport shared texture node.

## Methods
- `.getTextureForReference() :FramebufferTexture` — Overwritten so the method always returns the unique shared
framebuffer texture.

## Source