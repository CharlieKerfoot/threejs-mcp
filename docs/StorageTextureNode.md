# StorageTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

This special version of a texture node can be used to
write data into a storage texture with a compute shader. This node can only be used with a WebGPU backend.

## Constructor
`newStorageTextureNode( value :StorageTexture, uvNode :Node.<(vec2|vec3)>, storeNode :Node)`
Constructs a new storage texture node.

## Properties
- `.access : string` — The access type of the texture node. Default is 'writeOnly' .
- `.isStorageTextureNode : boolean` — This flag can be used for type testing. Default is true .
- `.mipLevel : number` — The mip level to write to for storage textures. Default is 0 .
- `.storeNode :Node` — The value node that should be stored in the texture. Default is null .

## Methods
- `.generate( builder :NodeBuilder, output :string) : string` — Generates the code snippet of the storage node. If no storeNode is defined, the texture node is generated as normal texture.
- `.generateSnippet( builder :NodeBuilder, textureProperty :string, uvSnippet :string, levelSnippet :string, biasSnippet :string, depthSnippet :string, compareSnippet :string, gradSnippet :Array.<string>, offsetSnippet :string) : string` — Generates the snippet for the storage texture.
- `.generateStore( builder :NodeBuilder)` — Generates the code snippet of the storage texture node.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return a fixed value 'storageTexture' .
- `.setAccess( value :string) :StorageTextureNode` — Defines the node access.
- `.setMipLevel( level :number) :StorageTextureNode` — Sets the mip level to write to.
- `.toReadOnly() :StorageTextureNode` — Convenience method for configuring a read-only node access.
- `.toReadWrite() :StorageTextureNode` — Convenience method for configuring a read/write node access.
- `.toWriteOnly() :StorageTextureNode` — Convenience method for configuring a write-only node access.

## Source