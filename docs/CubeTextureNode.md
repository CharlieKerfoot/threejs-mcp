# CubeTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

This type of uniform node represents a cube texture.

## Constructor
`newCubeTextureNode( value :CubeTexture, uvNode :Node.<vec3>, levelNode :Node.<int>, biasNode :Node.<float>)`
Constructs a new cube texture node.

## Properties
- `.isCubeTextureNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.generateUV( builder :NodeBuilder, cubeUV :Node) : string` — Generates the uv code snippet.
- `.getDefaultUV() :Node.<vec3>` — Returns a default uvs based on the mapping type of the cube texture.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return the appropriate cube texture type.
- `.setUpdateMatrix( value :boolean)` — Overwritten with an empty implementation since the updateMatrix flag is ignored
for cube textures. The uv transformation matrix is not applied to cube textures.
- `.setupUV( builder :NodeBuilder, uvNode :Node) :Node` — Setups the uv node. Depending on the backend as well as the texture type, it might be necessary
to modify the uv node for correct sampling.

## Source