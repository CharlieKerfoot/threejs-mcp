# TextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→

This type of uniform node represents a 2D texture.

## Constructor
`newTextureNode( value :Texture, uvNode :Node.<(vec2|vec3)>, levelNode :Node.<int>, biasNode :Node.<float>)`
Constructs a new texture node.

## Properties
- `.biasNode :Node.<float>` — Represents the bias to be applied during level-of-detail computation. Default is null .
- `.compareNode :Node.<float>` — Represents a reference value a texture sample is compared to. Default is null .
- `.depthNode :Node.<int>` — When using texture arrays, the depth node defines the layer to select. Default is null .
- `.gradNode : Array.<Node.<vec2>>` — When defined, a texture is sampled using explicit gradients. Default is null .
- `.isTextureNode : boolean` — This flag can be used for type testing. Default is true .
- `.levelNode :Node.<int>` — Represents the mip level that should be selected. Default is null .
- `.offsetNode :Node.<(ivec2|ivec3)>` — Represents the optional texel offset applied to the unnormalized texture
coordinate before sampling the texture. Default is null .
- `.referenceNode :Node` — The reference node. Default is null .
- `.sampler : boolean` — Whether texture values should be sampled or fetched. Default is true .
- `.updateMatrix : boolean` — Whether the uv transformation matrix should be
automatically updated or not. Use setUpdateMatrix() if you want to change the value of the property. Default is false .
- `.updateType : string` — By default the update() method is not executed. Depending on
whether a uv transformation matrix and/or flipY is applied, update() is executed per object. Default is 'none' .
- `.uvNode :Node.<(vec2|vec3)>` — Represents the texture coordinates. Default is null .
- `.value :Texture` — The texture value.

## Methods
- `.bias( biasNode :Node.<float>) :TextureNode` — Samples the texture with the given bias.
- `.blur( amountNode :Node.<float>) :TextureNode` — Samples a blurred version of the texture by defining an internal bias.
- `.clone() :TextureNode` — Clones the texture node.
- `.compare( compareNode :Node.<float>) :TextureNode` — Samples the texture by executing a compare operation.
- `.depth( depthNode :Node.<int>) :TextureNode` — Samples the texture by defining a depth node.
- `.generate( builder :NodeBuilder, output :string) : string` — Generates the code snippet of the texture node.
- `.generateOffset( builder :NodeBuilder, offsetNode :Node) : string` — Generates the offset code snippet.
- `.generateSnippet( builder :NodeBuilder, textureProperty :string, uvSnippet :string, levelSnippet :string, biasSnippet :string, depthSnippet :string, compareSnippet :string, gradSnippet :Array.<string>, offsetSnippet :string) : string` — Generates the snippet for the texture sampling.
- `.generateUV( builder :NodeBuilder, uvNode :Node) : string` — Generates the uv code snippet.
- `.getBase() :TextureNode` — Returns the base texture of this node.
- `.getDefaultUV() :AttributeNode.<vec2>` — Returns a default uvs based on the current texture's channel.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return a fixed value 'texture' .
- `.getNodeType( builder :NodeBuilder) : string` — Overwritten since the node type is inferred from the texture type.
- `.getSampler() : boolean` — Returns the sampler value.
- `.getTransformedUV( uvNode :Node) :Node` — Transforms the given uv node with the texture transformation matrix.
- `.getUniformHash( builder :NodeBuilder) : string` — Overwritten since the uniform hash is defined by the texture's UUID.
- `.grad( gradNodeX :Node.<vec2>, gradNodeY :Node.<vec2>) :TextureNode` — Samples the texture using an explicit gradient.
- `.level( levelNode :Node.<int>) :TextureNode` — Samples a specific mip of the texture.
- `.load( uvNode :Node.<uvec2>) :TextureNode` — TSL function for creating a texture node that fetches/loads texels without interpolation.
- `.offset( offsetNode :Node.<ivec2>) :TextureNode` — Samples the texture by defining an offset node.
- `.sample( uvNode :Node) :TextureNode` — Samples the texture with the given uv node.
- `.setSampler( value :boolean) :TextureNode` — Sets the sampler value.
- `.setUpdateMatrix( value :boolean) :TextureNode` — Defines whether the uv transformation matrix should automatically be updated or not.
- `.setup( builder :NodeBuilder)` — Setups texture node by preparing the internal nodes for code generation.
- `.setupUV( builder :NodeBuilder, uvNode :Node) :Node` — Setups the uv node. Depending on the backend as well as texture's image and type, it might be necessary
to modify the uv node for correct sampling.
- `.size( levelNode :Node.<int>) :TextureSizeNode` — Returns the texture size of the requested level.
- `.update()` — The update is used to implement the update of the uv transformation matrix.
- `.updateReference( state :any) :Texture` — Overwritten to always return the texture reference of the node.

## Source