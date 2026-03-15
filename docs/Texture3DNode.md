# Texture3DNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

This type of uniform node represents a 3D texture.

## Constructor
`newTexture3DNode( value :Data3DTexture, uvNode :Node.<(vec2|vec3)>, levelNode :Node.<int>)`
Constructs a new 3D texture node.

## Properties
- `.isTexture3DNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.generateOffset( builder :NodeBuilder, offsetNode :Node) : string` — Generates the offset code snippet.
- `.generateUV( builder :NodeBuilder, uvNode :Node) : string` — Generates the uv code snippet.
- `.getDefaultUV() :Node.<vec3>` — Returns a default uv node which is in context of 3D textures a three-dimensional
uv node.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return a fixed value 'texture3D' .
- `.normal( uvNode :Node.<vec3>) :Node.<vec3>` — Computes the normal for the given uv. These texture coordiantes represent a
position inside the 3D texture. Unlike geometric normals, this normal
represents a slope or gradient of scalar data insid...
- `.setUpdateMatrix( value :boolean)` — Overwritten with an empty implementation since the updateMatrix flag is ignored
for 3D textures. The uv transformation matrix is not applied to 3D textures.

## Source