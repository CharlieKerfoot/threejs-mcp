# MaxMipLevelNode
Extends: EventDispatcher→Node→InputNode→UniformNode→

A special type of uniform node that computes the
maximum mipmap level for a given texture node.

## Constructor
`newMaxMipLevelNode( textureNode :TextureNode)`
Constructs a new max mip level node.

## Properties
- `.texture :Texture` — The texture.
- `.textureNode :TextureNode` — The texture node to compute the max mip level for.
- `.updateType : string` — The updateType is set to NodeUpdateType.FRAME since the node updates
the texture once per frame in its MaxMipLevelNode#update method. Default is 'frame' .

## Source