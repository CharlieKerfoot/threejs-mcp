# GLSLNodeBuilder
Extends: NodeBuilder→

A node builder targeting GLSL. This module generates GLSL shader code from node materials and also
generates the respective bindings and vertex buffer definitions. These
data are later used by the renderer to create render and compute pipelines
for render objects.

## Constructor
`newGLSLNodeBuilder( object :Object3D, renderer :Renderer)`
Constructs a new GLSL node builder renderer.

## Properties
- `.builtins : Object.<string, Array.<string>>` — A dictionary that holds for each shader stage an Array of used builtins.
- `.extensions : Object.<string, Map.<string, Object>>` — A dictionary that holds for each shader stage a Map of used extensions.
- `.transforms : Array.<Object.<string, (AttributeNode|string)>>` — An array that holds objects defining the varying and attribute data in
context of Transform Feedback.
- `.uniformGroups : Object.<string, Object.<string,NodeUniformsGroup>>` — A dictionary holds for each shader stage ('vertex', 'fragment', 'compute')
another dictionary which manages UBOs per group ('render','frame','object').

## Methods
- `.buildCode()` — Controls the code build of the shader stages.
- `.buildFunctionCode( shaderNode :ShaderNodeInternal) : string` — Builds the given shader node.
- `.enableExtension( name :string, behavior :string, shaderStage :string)` — Enables the given extension.
- `.enableHardwareClipping( planeCount :string)` — Enables hardware clipping.
- `.enableMultiview()` — Enables multiview.
- `.generatePBO( storageArrayElementNode :StorageArrayElementNode) : string` — Setups the Pixel Buffer Object (PBO) for the given storage
buffer node.
- `.generateTexture( texture :Texture, textureProperty :string, uvSnippet :string, depthSnippet :string, offsetSnippet :string) : string` — Generates the GLSL snippet for sampling/loading the given texture.
- `.generateTextureBias( texture :Texture, textureProperty :string, uvSnippet :string, biasSnippet :string, depthSnippet :string, offsetSnippet :string) : string` — Generates the GLSL snippet when sampling textures with a bias to the mip level.
- `.generateTextureCompare( texture :Texture, textureProperty :string, uvSnippet :string, compareSnippet :string, depthSnippet :string, offsetSnippet :string, shaderStage :string) : string` — Generates the GLSL snippet for sampling a depth texture and comparing the sampled depth values
against a reference value.
- `.generateTextureGrad( texture :Texture, textureProperty :string, uvSnippet :string, gradSnippet :Array.<string>, depthSnippet :string, offsetSnippet :string) : string` — Generates the GLSL snippet for sampling/loading the given texture using explicit gradients.
- `.generateTextureLevel( texture :Texture, textureProperty :string, uvSnippet :string, levelSnippet :string, depthSnippet :string, offsetSnippet :string) : string` — Generates the GLSL snippet when sampling textures with explicit mip level.
- `.generateTextureLoad( texture :Texture, textureProperty :string, uvIndexSnippet :string, levelSnippet :string, depthSnippet :string, offsetSnippet :string) : string` — Generates the GLSL snippet that reads a single texel from a texture without sampling or filtering.
- `.getAttributes( shaderStage :string) : string` — Returns the shader attributes of the given shader stage as a GLSL string.
- `.getBitcastMethod( type :string, inputType :string) : string` — Returns the bitcast method name for a given input and outputType.
- `.getClipDistance() : string` — Returns the clip distances builtin.
- `.getDrawIndex() : string` — Returns the draw index builtin.
- `.getExtensions( shaderStage :string) : string` — Returns the enabled extensions of the given shader stage as a GLSL string.
- `.getFloatPackingMethod( encoding :string) : string` — Returns the float packing method name for a given numeric encoding.
- `.getFloatUnpackingMethod( encoding :string) : string` — Returns the float unpacking method name for a given numeric encoding.
- `.getFragCoord() : string` — Returns the frag coord builtin.
- `.getFragDepth() : string` — Returns the frag depth builtin.
- `.getFrontFacing() : string` — Returns the front facing builtin.
- `.getInstanceIndex() : string` — Contextually returns either the vertex stage instance index builtin
or the linearized index of an compute invocation within a grid of workgroups.
- `.getInvocationLocalIndex() : string` — Returns a builtin representing the index of an invocation within its workgroup.
- `.getInvocationSubgroupIndex()` — Returns a builtin representing the index of an invocation within its subgroup.
- `.getMethod( method :string) : string` — Returns the native shader method name for a given generic name.
- `.getOutputStructName() : string` — Returns the output struct name. Not relevant for GLSL.
- `.getPropertyName( node :Node, shaderStage :string) : string` — Returns a GLSL snippet that represents the property name of the given node.
- `.getStructMembers( struct :StructTypeNode) : string` — Returns the members of the given struct type node as a GLSL string.
- `.getStructs( shaderStage :string) : string` — Returns the structs of the given shader stage as a GLSL string.
- `.getSubgroupIndex()` — Returns a builtin representing the index of the current invocation's subgroup within its workgroup.
- `.getSubgroupSize()` — Returns a builtin representing the size of a subgroup within the current shader.
- `.getTernary( condSnippet :string, ifSnippet :string, elseSnippet :string) : string` — Returns the native snippet for a ternary operation.
- `.getTransforms( shaderStage :string) : string` — Returns the transforms of the given shader stage as a GLSL string.
- `.getTypeFromAttribute( attribute :BufferAttribute) : string` — Returns the type for a given buffer attribute.
- `.getUniformBufferLimit() : number` — Returns the maximum number of bytes available for uniform buffers.
- `.getUniformFromNode( node :UniformNode, type :string, shaderStage :string, name :string) :NodeUniform` — This method is one of the more important ones since it's responsible
for generating a matching binding instance for the given uniform node. These bindings are later used in the renderer to create b...
- `.getUniforms( shaderStage :string) : string` — Returns the uniforms of the given shader stage as a GLSL string.
- `.getVars( shaderStage :string) : string` — Returns the variables of the given shader stage as a GLSL string.
- `.getVaryings( shaderStage :string) : string` — Returns the varyings of the given shader stage as a GLSL string.
- `.getVertexIndex() : string` — Returns the vertex index builtin.
- `.isAvailable( name :string) : boolean` — Whether the requested feature is available or not.
- `.isFlipY() : boolean` — Whether to flip texture data along its vertical axis or not.
- `.needsToWorkingColorSpace( texture :Texture) : boolean` — Checks if the given texture requires a manual conversion to the working color space.
- `.registerTransform( varyingName :string, attributeNode :AttributeNode)` — Registers a transform in context of Transform Feedback.
- `.setupPBO( storageBufferNode :StorageBufferNode)` — Setups the Pixel Buffer Object (PBO) for the given storage
buffer node.

## Source