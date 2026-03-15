# TextureSizeNode
Extends: EventDispatcher→Node→

A node that represents the dimensions of a texture. The texture size is
retrieved in the shader via built-in shader functions like textureDimensions() or textureSize() .

## Constructor
`newTextureSizeNode( textureNode :TextureNode, levelNode :Node.<int>)`
Constructs a new texture size node.

## Properties
- `.isTextureSizeNode : boolean` — This flag can be used for type testing. Default is true .
- `.levelNode :Node.<int>` — A level node which defines the requested mip. Default is null .
- `.textureNode :TextureNode` — A texture node which size should be retrieved.

## Source