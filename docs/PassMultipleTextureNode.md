# PassMultipleTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→PassTextureNode→

An extension of PassTextureNode which allows to manage more than one
internal texture. Relevant for the getPreviousTexture() related API.

## Constructor
`newPassMultipleTextureNode( passNode :PassNode, textureName :string, previousTexture :boolean)`
Constructs a new pass texture node.

## Properties
- `.isPassMultipleTextureNode : boolean` — This flag can be used for type testing. Default is true .
- `.previousTexture : boolean` — Whether previous frame data should be used or not.
- `.textureName : string` — The output texture name.

## Methods
- `.updateTexture()` — Updates the texture reference of this node.

## Source