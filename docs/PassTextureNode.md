# PassTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

Represents the texture of a pass node.

## Constructor
`newPassTextureNode( passNode :PassNode, texture :Texture)`
Constructs a new pass texture node.

## Properties
- `.isPassTextureNode : boolean` — This flag can be used for type testing. Default is true .
- `.passNode :PassNode` — A reference to the pass node.

## Source