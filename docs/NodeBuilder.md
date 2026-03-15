# NodeBuilder

Base class for builders which generate a shader program based
on a 3D object and its node material definition.

## Constructor
`newNodeBuilder( object :Object3D, renderer :Renderer, parser :NodeParser)`
Constructs a new node builder.

## Properties
- `.activeStacks : Array.<StackNode>` — The active stack nodes.
- `.attributes : Array.<NodeAttribute>` — This array holds the node attributes of this builder
created via AttributeNode .
- `.bindGroups : Array.<BindGroup>` — Reference to the array of bind groups.
- `.bindings : Object` — This dictionary holds the bindings for each shader stage.
- `.bindingsIndexes : Object` — This dictionary maintains the binding indices per bind group.
- `.bufferAttributes : Array.<NodeAttribute>` — This array holds the node attributes of this builder
created via BufferAttributeNode .
- `.buildStage : 'setup' | 'analyze' | 'generate'` — The current build stage.
- `.cache :NodeCache` — The builder's cache.
- `.camera :Camera` — The camera the 3D object is rendered with. Default is null .
- `.chaining : Array.<Node>` — A chain of nodes.
Used to check recursive calls in node-graph.
- `.clippingContext :ClippingContext` — The current clipping context.
- `.codes : Object.<string, Array.<NodeCode>>` — This dictionary holds the (native) node codes of this builder.
The codes are maintained in an array for each shader stage.
- `.computeShader : string` — The generated compute shader.
- `.context : Object` — The builder's context.
- `.currentFunctionNode :FunctionNode` — Reference to the current function node. Default is null .
- `.currentNode :Node` — A reference the current node which is the
last node in the chain of nodes.
- `.declarations : Object` — This dictionary holds the declarations for each shader stage.
- `.environmentNode :Node` — A reference to the current environment node. Default is null .
- `.flow : Object` — Current code flow.
All code generated in this stack will be stored in .flow .
- `.flowCode : Object.<string, string>` — Nodes code from .flowNodes .
- `.flowNodes : Object.<string, Array.<Node>>` — Nodes used in the primary flow of code generation.
- `.fnCall :Node` — The current TSL function(Fn) call node. Default is null .
- `.fogNode :Node` — A reference to the current fog node. Default is null .
- `.fragmentShader : string` — The generated fragment shader.
- `.geometry :BufferGeometry` — The geometry of the 3D object.
- `.globalCache :NodeCache` — Since the NodeBuilder#cache might be temporarily
overwritten by other caches, this member retains the reference
to the builder's own cache. Default is this.cache .
- `.hashNodes : Object.<number,Node>` — A dictionary that assigns each node to a unique hash.
- `.lightsNode :LightsNode` — A reference to the current lights node. Default is null .
- `.material :Material` — The material of the 3D object.
- `.nodes : Array.<Node>` — A list of all nodes the builder is processing
for this 3D object.
- `.object :Object3D` — The 3D object.
- `.observer :NodeMaterialObserver` — A reference to a node material observer. Default is null .
- `.parser :NodeParser` — A reference to a node parser.
- `.renderer :Renderer` — The current renderer.
- `.scene :Scene` — The scene the 3D object belongs to. Default is null .
- `.sequentialNodes : Array.<Node>` — A list of all nodes the builder is processing in sequential order. This is used to determine the update order of nodes, which is important for
NodeUpdateType#UPDATE_BEFORE and NodeUpdateType#UPDATE...
- `.shaderStage : 'vertex' | 'fragment' | 'compute' | 'any'` — The current shader stage.
- `.stack :StackNode` — The current stack.
This reflects the current process in the code block hierarchy,
it is useful to know if the current process is inside a conditional for example.
- `.stacks : Array.<StackNode>` — List of stack nodes.
The current stack hierarchy is stored in an array.
- `.structs : Object` — This dictionary holds the output structs of the builder.
The structs are maintained in an array for each shader stage.
- `.subBuild` — Returns the current sub-build layer.
- `.subBuildFn : string` — The current sub-build TSL function(Fn). Default is null .
- `.subBuildLayers : Array.<SubBuildNode>` — The sub-build layers. Default is [] .
- `.tab : string` — A tab value. Used for shader string generation. Default is '\t' .
- `.types : Object` — This dictionary holds the types of the builder.
- `.uniforms : Object` — This dictionary holds the node uniforms of the builder.
The uniforms are maintained in an array for each shader stage.
- `.updateAfterNodes : Array.<Node>` — A list of all nodes which Node#updateAfter method should be executed.
- `.updateBeforeNodes : Array.<Node>` — A list of all nodes which Node#updateBefore method should be executed.
- `.updateNodes : Array.<Node>` — A list of all nodes which Node#update method should be executed.
- `.vars : Object.<string, (Array.<NodeVar>|number)>` — This dictionary holds the node variables of this builder.
The variables are maintained in an array for each shader stage.
This dictionary is also used to count the number of variables
according to ...
- `.varyings : Array.<NodeVarying>` — This array holds the node varyings of this builder.
- `.vertexShader : string` — The generated vertex shader.

## Methods
- `.addChain( node :Node)` — Adds the given node to the internal node chain.
This is used to check recursive calls in node-graph.
- `.addContext( context :Object) : Object` — Adds context data to the builder's current context.
- `.addFlow( shaderStage :'vertex' | 'fragment' | 'compute', node :Node) :Node` — Adds the Node to a target flow so that it can generate code in the 'generate' process.
- `.addFlowCode( code :string) :NodeBuilder` — Adds a code to the current code flow.
- `.addFlowCodeHierarchy( node :Node, nodeBlock :Node)` — Adds a code flow based on the code-block hierarchy.
This is used so that code-blocks like If,Else create their variables locally if the Node
is only used inside one of these conditionals in the cur...
- `.addFlowTab() :NodeBuilder` — Add tab in the code that will be generated so that other snippets respect the current tabulation.
Typically used in codes with If,Else.
- `.addInclude( node :Node) : void` — Includes a node in the current function node.
- `.addLineFlowCode( code :string, node :Node) :NodeBuilder` — Add a inline-code to the current flow.
- `.addLineFlowCodeBlock( node :Node, code :string, nodeBlock :Node)` — Add a inline-code to the current flow code-block.
- `.addNode( node :Node)` — Adds a node to this builder.
- `.addSequentialNode( node :Node)` — It is used to add Nodes that will be used as FRAME and RENDER events,
and need to follow a certain sequence in the calls to work correctly.
This function should be called after 'setup()' in the 'bu...
- `.addStack() :StackNode` — Adds a stack node to the internal stack.
- `.addSubBuild( subBuild :SubBuildNode)` — Adds a sub-build layer to the node builder.
- `.build() :NodeBuilder` — Central build method which controls the build for the given object.
- `.buildCode() (abstract)` — Controls the code build of the shader stages.
- `.buildFunctionCode( shaderNode :ShaderNodeInternal) : string` — Builds the given shader node.
- `.buildFunctionNode( shaderNode :ShaderNodeInternal) :FunctionNode` — Returns the native shader operator name for a given generic name.
It is a similar type of method like NodeBuilder#getMethod .
- `.buildUpdateNodes()` — Checks the update types of nodes
- `.changeComponentType( type :string, newComponentType :string) : string` — For a given type this method changes the component type to the
given value. E.g. vec4 should be changed to the new component type uint which results in uvec4 .
- `.createCubeRenderTarget( size :number, options :Object) :CubeRenderTarget` — Factory method for creating an instance of CubeRenderTarget with the given
dimensions and options.
- `.createRenderTarget( width :number, height :number, options :Object) :RenderTarget` — Factory method for creating an instance of RenderTarget with the given
dimensions and options.
- `.flowBuildStage( node :Node, buildStage :string, output :Node| string) :Node| string` — Executes the node in a specific build stage. This function can be used to arbitrarily execute the specified build stage
outside of the standard build process. For instance, if a node's type depends...
- `.flowChildNode( node :Node, output :string) : Object` — Generates a code flow based on a child Node.
- `.flowNode( node :Node) : Object` — Executes the node flow based on a root node to generate the final shader code.
- `.flowNodeFromShaderStage( shaderStage :'vertex' | 'fragment' | 'compute' | 'any', node :Node, output :string, propertyName :string) : Object |Node` — Executes a flow of code in a different stage. Some nodes like varying() have the ability to compute code in vertex-stage and
return the value in fragment-stage even if it is being executed in an in...
- `.flowShaderNode( shaderNode :ShaderNodeInternal) : Object` — Generates a code flow based on a TSL function: Fn().
- `.flowStagesNode( node :Node, output :string) : Object` — Runs the node flow through all the steps of creation, 'setup', 'analyze', 'generate'.
- `.format( snippet :string, fromType :string, toType :string) : string` — Formats the given shader snippet from a given type into another one. E.g.
this method might be used to convert a simple float string "1.0" into a vec3 representation: "vec3<f32>( 1.0 )" .
- `.generateArray( type :string, count :number, values :Array.<Node>) : string` — Generates the array shader string for the given type and value.
- `.generateArrayDeclaration( type :string, count :number) : string` — Generates the array declaration string.
- `.generateConst( type :string, value :any) : string` — Generates the shader string for the given type and value.
- `.generateStruct( type :string, membersLayout :Array.<Object>, values :Array.<Node>) : string` — Generates the struct shader string.
- `.generateTexture( texture :Texture, textureProperty :string, uvSnippet :string) : string` — Generates a texture sample shader string for the given texture data.
- `.generateTextureLod( texture :Texture, textureProperty :string, uvSnippet :string, depthSnippet :string, levelSnippet :string) : string` — Generates a texture LOD shader string for the given texture data.
- `.getActiveStack() :StackNode` — Returns the active stack.
- `.getAttribute( name :string, type :string) :NodeAttribute` — Returns a node attribute for the given name and type.
- `.getAttributes( shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : string` — Returns the attribute definitions as a shader string for the given shader stage.
- `.getAttributesArray() : Array.<NodeAttribute>` — Returns an array holding all node attributes of this node builder.
- `.getBaseStack() :StackNode` — Returns the base stack.
- `.getBindGroupArray( groupName :string, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : Array.<NodeUniformsGroup>` — Returns an array of node uniform groups for the given group name and shader stage.
- `.getBindings() : Array.<BindGroup>` — Returns a list bindings of all shader stages separated by groups.
- `.getBufferAttributeFromNode( node :BufferAttributeNode, type :string) :NodeAttribute` — Returns an instance of NodeAttribute for the given buffer attribute node.
- `.getBuildStage() : 'setup' | 'analyze' | 'generate'` — Returns the current build stage.
- `.getCache() :NodeCache` — Returns the builder's current cache.
- `.getCacheFromNode( node :Node, parent :boolean) :NodeCache` — Returns a cache for the given node.
- `.getClosestSubBuild( data :Node| Set.<string> | Array.<string>) : string` — Returns the closest sub-build layer for the given data.
- `.getCodeFromNode( node :CodeNode, type :string, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') :NodeCode` — Returns an instance of NodeCode for the given code node.
- `.getCodes( shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : string` — Returns the native code definitions as a shader string for the given shader stage.
- `.getComponentType( type :string) : string` — Returns the component type for a given type.
- `.getComponentTypeFromTexture( texture :Texture) : string` — Returns the component type of a given texture.
- `.getContext() : Object` — Returns the builder's current context.
- `.getDataFromNode( node :Node, shaderStage :'vertex' | 'fragment' | 'compute' | 'any', cache :NodeCache) : Object` — The builder maintains (cached) data for each node during the building process. This method
can be used to get these data for a specific shader stage and cache.
- `.getDrawIndex() : string` — Returns the drawIndex input variable as a native shader string.
Only relevant for WebGL and its WEBGL_multi_draw extension.
- `.getElementType( type :string) : string` — Returns the element type for a given type.
- `.getFlowData( node :Node, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : Object` — Gets the current flow data based on a Node.
- `.getFragCoord() : string` — Returns the fragCoord input variable as a native shader string.
- `.getFrontFacing() : string` — Returns the frontFacing input variable as a native shader string.
- `.getFunctionOperator( op :string) : string` — Returns the native shader operator name for a given generic name.
It is a similar type of method like NodeBuilder#getMethod .
- `.getHash() : string` — Returns the hash of this node builder.
- `.getInstanceIndex() : string` — Contextually returns either the vertex stage instance index builtin
or the linearized index of an compute invocation within a grid of workgroups.
- `.getIntegerType( type :string) : string` — Returns the integer type pendant for the given type.
- `.getMethod( method :string) : string` — Returns the native shader method name for a given generic name. E.g.
the method name textureDimensions matches the WGSL name but must be
resolved to textureSize in GLSL.
- `.getNodeFromHash( hash :number) :Node` — Returns a node for the given hash, see NodeBuilder#setHashNode .
- `.getNodeProperties( node :Node, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : Object` — Returns the properties for the given node and shader stage. Properties are typically used within a build stage to reference a node's
child node or nodes manually assigned to the properties in a sep...
- `.getNodeUniform( uniformNode :NodeUniform, type :string) :Uniform` — Returns a uniform representation which is later used for UBO generation and rendering.
- `.getOutputStructName() : string` — Returns the output struct name which is required by OutputStructNode .
- `.getOutputStructTypeFromNode( node :OutputStructNode, membersLayout :Array.<Object>) : StructType` — Returns an instance of StructType for the given output struct node.
- `.getPropertyName( node :Node, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : string` — Returns for the given node and shader stage the property name for the shader.
- `.getShaderStage() : 'vertex' | 'fragment' | 'compute' | 'any'` — Returns the current shader stage.
- `.getSharedContext() : Object` — Gets a context used in shader construction that can be shared across different materials.
This is necessary since the renderer cache can reuse shaders generated in one material and use them in anot...
- `.getSharedDataFromNode( node :Node) : Object` — Returns shared data object for the given node.
- `.getSignature() : string` — Returns a signature with the engine's current revision.
- `.getStructTypeFromNode( node :OutputStructNode, membersLayout :Array.<Object>, name :string, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : StructType` — Returns an instance of StructType for the given output struct node.
- `.getStructTypeNode( name :string, shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : StructType` — Returns an instance of StructType for the given struct name and shader stage
or null if not found.
- `.getSubBuildOutput( node :Node) : string` — Returns the output node of a sub-build layer.
- `.getSubBuildProperty( property :string, node :Node) : string` — Returns the sub-build property name for the given property and node.
- `.getTernary( condSnippet :string, ifSnippet :string, elseSnippet :string) : string` — Returns the native snippet for a ternary operation. E.g. GLSL would output
a ternary op as cond ? x : y whereas WGSL would output it as select(y, x, cond)
- `.getType( type :string) : string` — It might be necessary to convert certain data types to different ones
so this method can be used to hide the conversion.
- `.getTypeFromArray( array :TypedArray) : string` — Returns the type for a given typed array.
- `.getTypeFromAttribute( attribute :BufferAttribute) : string` — Returns the type for a given buffer attribute.
- `.getTypeFromLength( length :number, componentType :string) : string` — Returns the data type for the given the length and component type.
- `.getTypeLength( type :string) : number` — Returns the length for the given data type.
- `.getUniformBufferLimit() : number` — Returns the maximum number of bytes available for uniform buffers.
- `.getUniformFromNode( node :UniformNode, type :string, shaderStage :'vertex' | 'fragment' | 'compute' | 'any', name :string) :NodeUniform` — Returns an instance of NodeUniform for the given uniform node.
- `.getUniforms( shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : string` — Returns the uniform definitions as a shader string for the given shader stage.
- `.getVar( type :string, name :string, count :number) : string` — Returns a single variable definition as a shader string for the given variable type and name.
- `.getVarFromNode( node :VarNode, name :string, type :string, shaderStage :'vertex' | 'fragment' | 'compute' | 'any', readOnly :boolean) :NodeVar` — Returns an instance of NodeVar for the given variable node.
- `.getVars( shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : string` — Returns the variable definitions as a shader string for the given shader stage.
- `.getVaryingFromNode( node :VaryingNode|PropertyNode, name :string, type :string, interpolationType :string, interpolationSampling :string) :NodeVar` — Returns an instance of NodeVarying for the given varying node.
- `.getVaryings( shaderStage :'vertex' | 'fragment' | 'compute' | 'any') : string` — Returns the varying definitions as a shader string for the given shader stage.
- `.getVectorFromMatrix( type :string) : string` — Returns the vector type for a given matrix type.
- `.getVectorType( type :string) : string` — Returns the vector type for a given type.
- `.getVertexIndex() : string` — Returns the vertexIndex input variable as a native shader string.
- `.hasGeometryAttribute( name :string) : boolean` — Whether the given attribute name is defined in the geometry or not.
- `.includes( node :Node) : boolean` — Whether the given node is included in the internal array of nodes or not.
- `.increaseUsage( node :Node) : number` — Calling this method increases the usage count for the given node by one.
- `.isAvailable( name :string) : boolean` — Whether the requested feature is available or not.
- `.isDeterministic( node :Node) : boolean` — Returns whether a Node or its flow is deterministic, useful for use in const .
- `.isFilteredTexture( texture :Texture) : boolean` — Whether the given texture is filtered or not.
- `.isFlatShading() : boolean` — Whether the material is using flat shading or not.
- `.isFlipY() : boolean` — Whether to flip texture data along its vertical axis or not. WebGL needs
this method evaluate to true , WebGPU to false .
- `.isInteger( type :string) : boolean` — Returns the type is an integer type.
- `.isMatrix( type :string) : boolean` — Whether the given type is a matrix type or not.
- `.isOpaque() : boolean` — Whether the material is opaque or not.
- `.isReference( type :string) : boolean` — Whether the given type is a reference type or not.
- `.isVector( type :string) : boolean` — Whether the given type is a vector type or not.
- `.needsPreviousData() : boolean` — Returns true if data from the previous frame are required. Relevant
when computing motion vectors with VelocityNode .
- `.needsToWorkingColorSpace( texture :Texture) : boolean` — Checks if the given texture requires a manual conversion to the working color space.
- `.registerDeclaration( node :Object)` — Registers a node declaration in the current shader stage.
- `.removeActiveStack( stack :StackNode)` — Removes the active stack from the internal stack.
- `.removeChain( node :Node)` — Removes the given node from the internal node chain.
- `.removeFlowTab() :NodeBuilder` — Removes a tab.
- `.removeStack() :StackNode` — Removes the last stack node from the internal stack.
- `.removeSubBuild() :SubBuildNode` — Removes the last sub-build layer from the node builder.
- `.setActiveStack( stack :StackNode)` — Adds an active stack to the internal stack.
- `.setBuildStage( buildStage :'setup' | 'analyze' | 'generate')` — Sets the current build stage.
- `.setCache( cache :NodeCache)` — Sets builder's cache.
- `.setContext( context :Object)` — Sets builder's context.
- `.setHashNode( node :Node, hash :number)` — The builder maintains each node in a hash-based dictionary.
This method sets the given node (value) with the given hash (key) into this dictionary.
- `.setShaderStage( shaderStage :'vertex' | 'fragment' | 'compute' | 'any')` — Sets the current shader stage.
- `.sortBindingGroups()` — Sorts the bind groups and updates NodeBuilder#bindingsIndexes .

## Source