# WGSLNodeBuilder
Extends: NodeBuilder→

A node builder targeting WGSL. This module generates WGSL shader code from node materials and also
generates the respective bindings and vertex buffer definitions. These
data are later used by the renderer to create render and compute pipelines
for render objects.

## Constructor
`newWGSLNodeBuilder( object :Object3D, renderer :Renderer)`
Constructs a new WGSL node builder renderer.

## Properties
- `.builtins : Object.<string, Map.<string, Object>>` — A dictionary that holds for each shader stage a Map of builtins.
- `.directives : Object.<string, Set.<string>>` — A dictionary that holds for each shader stage a Set of directives.
- `.scopedArrays : Map.<string, Object>` — A map for managing scope arrays. Only relevant for when using WorkgroupInfoNode in context of compute shaders.
- `.uniformGroups : Object.<string, Object.<string,NodeUniformsGroup>>` — A dictionary that holds for each shader stage ('vertex', 'fragment', 'compute')
another dictionary which manages UBOs per group ('render','frame','object').
- `.uniformGroupsBindings : Object.<string, {index: number, id: number}>` — A dictionary that holds the assigned binding indices for each uniform group.
This ensures the same binding index is used across all shader stages.

## Methods
- `.buildCode()` — Controls the code build of the shader stages.
- `.buildFunctionCode( shaderNode :ShaderNodeInternal) : string` — Builds the given shader node.
- `.enableClipDistances()` — Enables the 'clip_distances' directive.
- `.enableDirective( name :string, shaderStage :string)` — Enables the given directive for the given shader stage.
- `.enableDualSourceBlending()` — Enables the 'dual_source_blending' directive.
- `.enableHardwareClipping( planeCount :string)` — Enables hardware clipping.
- `.enableShaderF16()` — Enables the 'f16' directive.
- `.enableSubGroups()` — Enables the 'subgroups' directive.
- `.enableSubgroupsF16()` — Enables the 'subgroups-f16' directive.
- `.generateArrayDeclaration( type :string, count :number) : string` — Generates the array declaration string.
- `.generateFilteredTexture( texture :Texture, textureProperty :string, uvSnippet :string, offsetSnippet :string, levelSnippet :string, depthSnippet :string) : string` — Generates the WGSL snippet for a manual filtered texture.
- `.generateStorageTextureLoad( texture :Texture, textureProperty :string, uvIndexSnippet :string, levelSnippet :string, depthSnippet :string, offsetSnippet :string) : string` — Generates the WGSL snippet that reads a single texel from a storage texture.
- `.generateTexture( texture :Texture, textureProperty :string, uvSnippet :string, depthSnippet :string, offsetSnippet :string, shaderStage :string) : string` — Generates the WGSL snippet for sampling/loading the given texture.
- `.generateTextureBias( texture :Texture, textureProperty :string, uvSnippet :string, biasSnippet :string, depthSnippet :string, offsetSnippet :string, shaderStage :string) : string` — Generates the WGSL snippet when sampling textures with a bias to the mip level.
- `.generateTextureCompare( texture :Texture, textureProperty :string, uvSnippet :string, compareSnippet :string, depthSnippet :string, offsetSnippet :string, shaderStage :string) : string` — Generates the WGSL snippet for sampling a depth texture and comparing the sampled depth values
against a reference value.
- `.generateTextureDimension( texture :Texture, textureProperty :string, levelSnippet :string) : string` — Generates a WGSL variable that holds the texture dimension of the given texture.
It also returns information about the number of layers (elements) of an arrayed
texture as well as the cube face cou...
- `.generateTextureGrad( texture :Texture, textureProperty :string, uvSnippet :string, gradSnippet :Array.<string>, depthSnippet :string, offsetSnippet :string, shaderStage :string) : string` — Generates the WGSL snippet for sampling/loading the given texture using explicit gradients.
- `.generateTextureLevel( texture :Texture, textureProperty :string, uvSnippet :string, levelSnippet :string, depthSnippet :string, offsetSnippet :string, shaderStage :string) : string` — Generates the WGSL snippet when sampling textures with explicit mip level.
- `.generateTextureLoad( texture :Texture, textureProperty :string, uvIndexSnippet :string, levelSnippet :string, depthSnippet :string, offsetSnippet :string) : string` — Generates the WGSL snippet that reads a single texel from a texture without sampling or filtering.
- `.generateTextureLod( texture :Texture, textureProperty :string, uvSnippet :string, depthSnippet :string, offsetSnippet :string, levelSnippet :string) : string` — Generates the WGSL snippet for a texture lookup with explicit level-of-detail.
Since it's a lookup, no sampling or filtering is applied.
- `.generateTextureStore( texture :Texture, textureProperty :string, uvIndexSnippet :string, depthSnippet :string, valueSnippet :string) : string` — Generates the WGSL snippet that writes a single texel to a texture.
- `.generateWrapFunction( texture :Texture) : string` — Generates a wrap function used in context of textures.
- `.getAttributes( shaderStage :string) : string` — Returns the shader attributes of the given shader stage as a WGSL string.
- `.getBitcastMethod( type :string) : string` — Returns the bitcast method name for a given input and outputType.
- `.getBuiltin( name :string, property :string, type :string, shaderStage :string) : string` — This method should be used whenever builtins are required in nodes.
The internal builtins data structure will make sure builtins are
defined in the WGSL source.
- `.getBuiltins( shaderStage :string) : string` — Returns the builtins of the given shader stage as a WGSL string.
- `.getClipDistance() : string` — Returns the clip distances builtin.
- `.getDirectives( shaderStage :string) : string` — Returns the directives of the given shader stage as a WGSL string.
- `.getDrawIndex() : null` — Overwritten as a NOP since this method is intended for the WebGL 2 backend.
- `.getFloatPackingMethod( encoding :string) : string` — Returns the float packing method name for a given numeric encoding.
- `.getFloatUnpackingMethod( encoding :string) : string` — Returns the float unpacking method name for a given numeric encoding.
- `.getFragCoord() : string` — Returns the frag coord builtin.
- `.getFragDepth() : string` — Returns the frag depth builtin.
- `.getFrontFacing() : string` — Returns the front facing builtin.
- `.getFunctionOperator( op :string) : string` — Returns the native shader operator name for a given generic name.
- `.getInstanceIndex() : string` — Contextually returns either the vertex stage instance index builtin
or the linearized index of an compute invocation within a grid of workgroups.
- `.getInvocationLocalIndex() : string` — Returns a builtin representing the index of a compute invocation within the scope of a workgroup load.
- `.getInvocationSubgroupIndex() : string` — Returns a builtin representing the index of a compute invocation within the scope of a subgroup.
- `.getMethod( method :string, output :string) : string` — Returns the native shader method name for a given generic name.
- `.getNodeAccess( node :StorageTextureNode|StorageBufferNode, shaderStage :string) : string` — Returns the node access for the given node and shader stage.
- `.getOutputStructName() : string` — Returns the output struct name.
- `.getPropertyName( node :Node, shaderStage :string) : string` — Returns a WGSL snippet that represents the property name of the given node.
- `.getScopedArray( name :string, scope :string, bufferType :string, bufferCount :string) : string` — This method should be used when a new scoped buffer is used in context of
compute shaders. It adds the array to the internal data structure which is
later used to generate the respective WGSL.
- `.getScopedArrays( shaderStage :string) : string | undefined` — Returns the scoped arrays of the given shader stage as a WGSL string.
- `.getStorageAccess( node :StorageTextureNode|StorageBufferNode, shaderStage :string) : string` — Returns A WGSL snippet representing the storage access.
- `.getStructMembers( struct :StructTypeNode) : string` — Returns the members of the given struct type node as a WGSL string.
- `.getStructs( shaderStage :string) : string` — Returns the structs of the given shader stage as a WGSL string.
- `.getSubgroupIndex() : string` — Returns a builtin representing the index of a compute invocation's subgroup within its workgroup.
- `.getSubgroupSize() : string` — Returns a builtin representing the size of a subgroup within the current shader.
- `.getTernary( condSnippet :string, ifSnippet :string, elseSnippet :string) : string` — Returns the native snippet for a ternary operation.
- `.getType( type :string) : string` — Returns the WGSL type of the given node data type.
- `.getUniformBufferLimit() : number` — Returns the maximum uniform buffer size limit.
- `.getUniformFromNode( node :UniformNode, type :string, shaderStage :string, name :string) :NodeUniform` — This method is one of the more important ones since it's responsible
for generating a matching binding instance for the given uniform node. These bindings are later used in the renderer to create b...
- `.getUniforms( shaderStage :string) : string` — Returns the uniforms of the given shader stage as a WGSL string.
- `.getVar( type :string, name :string, count :number) : string` — Returns a WGSL string representing a variable.
- `.getVars( shaderStage :string) : string` — Returns the variables of the given shader stage as a WGSL string.
- `.getVaryings( shaderStage :string) : string` — Returns the varyings of the given shader stage as a WGSL string.
- `.getVertexIndex() : string` — Returns the vertex index builtin.
- `.hasBuiltin( name :string, shaderStage :string) : boolean` — Returns true if the given builtin is defined in the given shader stage.
- `.isAvailable( name :string) : boolean` — Whether the requested feature is available or not.
- `.isFlipY() : boolean` — Whether to flip texture data along its vertical axis or not.
- `.isSampleCompare( texture :Texture) : boolean` — Returns true if the sampled values of the given texture should be compared against a reference value.
- `.isUnfilterable( texture :Texture) : boolean` — Returns true if the given texture is unfilterable.

## Source