# NodeMaterial
Extends: EventDispatcher→Material→

Base class for all node materials.

## Constructor
`newNodeMaterial()`
Constructs a new node material.

## Properties
- `.alphaTestNode :Node.<float>` — The alpha test of node materials is by default inferred from the alphaTest property. This node property allows to overwrite the default and define the
alpha test with a node instead. If you don't w...
- `.aoNode :Node.<float>` — The lighting of node materials might be influenced by ambient occlusion.
The default AO is inferred from an ambient occlusion map assigned to aoMap and the respective aoMapIntensity . This node pro...
- `.backdropAlphaNode :Node.<float>` — This node allows to modulate the influence of backdropNode to the outgoing light. Default is null .
- `.backdropNode :Node.<vec3>` — This node can be used to implement a variety of filter-like effects. The idea is
to store the current rendering into a texture e.g. via viewportSharedTexture() , use it
to create an arbitrary effec...
- `.castShadowNode :Node.<vec4>` — This node can be used to influence how an object using this node material
casts shadows. To apply a color to shadows, you can simply do: material.castShadowNode = vec4( 1, 0, 0, 1 ); Which can be n...
- `.castShadowPositionNode :Node.<float>` — Allows to overwrite the geometry position used for shadow map projection which
is by default positionLocal , the vertex position in local space. Default is null .
- `.colorNode :Node.<vec3>` — The diffuse color of node materials is by default inferred from the color and map properties. This node property allows to overwrite the default
and define the diffuse color with a node instead. ma...
- `.contextNode :ContextNode` — This node can be used as a global context management component for this material. Default is null .
- `.depthNode :Node.<float>` — Allows to overwrite depth values in the fragment shader. Default is null .
- `.envNode :Node.<vec3>` — The environment of node materials can be defined by an environment
map assigned to the envMap property or by Scene.environment if the node material is a PBR material. This node property allows to o...
- `.fog : boolean` — Whether this material is affected by fog or not. Default is true .
- `.fragmentNode :Node.<vec4>` — This node property can be used if you need complete freedom in implementing
the fragment shader. Assigning a node will replace the built-in material
logic used in the fragment stage. Default is null .
- `.geometryNode : function` — This node property is intended for logic which modifies geometry data once or per animation step.
Apps usually place such logic randomly in initialization routines or in the animation loop. geometr...
- `.hardwareClipping : boolean` — Whether this material uses hardware clipping or not.
This property is managed by the engine and should not be
modified by apps. Default is false .
- `.isNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Whether this material is affected by lights or not. Default is false .
- `.lightsNode :LightsNode` — Node materials which set their lights property to true are affected by all lights of the scene. Sometimes selective
lighting is wanted which means only some lights in the scene
affect a material. T...
- `.maskNode :Node.<bool>` — Discards the fragment if the mask value is false . Default is null .
- `.maskShadowNode :Node.<bool>` — This node can be used to implement a shadow mask for the material. Default is null .
- `.mrtNode :MRTNode` — MRT configuration is done on renderer or pass level. This node allows to
overwrite what values are written into MRT targets on material level. This
can be useful for implementing selective FX featu...
- `.normalNode :Node.<vec3>` — The normals of node materials are by default inferred from the normalMap / normalScale or bumpMap / bumpScale properties. This node property allows to overwrite the default
and define the normals w...
- `.opacityNode :Node.<float>` — The opacity of node materials is by default inferred from the opacity and alphaMap properties. This node property allows to overwrite the default
and define the opacity with a node instead. If you ...
- `.outputNode :Node.<vec4>` — This node can be used to define the final output of the material. TODO: Explain the differences to fragmentNode . Default is null .
- `.positionNode :Node.<vec3>` — The local vertex positions are computed based on multiple factors like the
attribute data, morphing or skinning. This node property allows to overwrite
the default and define local vertex positions...
- `.receivedShadowNode : function |FunctionNode.<vec4>` — This node can be used to influence how an object using this node material
receive shadows. const totalShadows = float( 1 ).toVar();
material.receivedShadowNode = Fn( ( [ shadow ] ) => {
	totalShado...
- `.receivedShadowPositionNode :Node.<float>` — Allows to overwrite the position used for shadow map rendering which
is by default positionWorld , the vertex position
in world space. Default is null .
- `.type : string` — Represents the type of the node material.
- `.vertexNode :Node.<vec4>` — This node property can be used if you need complete freedom in implementing
the vertex shader. Assigning a node will replace the built-in material logic
used in the vertex stage. Default is null .

## Methods
- `.build( builder :NodeBuilder)` — Builds this material with the given node builder.
- `.copy( source :NodeMaterial) :NodeMaterial` — Copies the properties of the given node material to this instance.
- `.customProgramCacheKey() : string` — Allows to define a custom cache key that influence the material key computation
for render objects.
- `.setDefaultValues( material :Material)` — Most classic material types have a node pendant e.g. for MeshBasicMaterial there is MeshBasicNodeMaterial . This utility method is intended for
defining all material properties of the classic type ...
- `.setup( builder :NodeBuilder)` — Setups the vertex and fragment stage of this node material.
- `.setupClipping( builder :NodeBuilder) :ClippingNode` — Setups the clipping node.
- `.setupDepth( builder :NodeBuilder)` — Setups the depth of this material.
- `.setupDiffuseColor( builder :NodeBuilder, geometry :BufferGeometry)` — Setups the computation of the material's diffuse color.
- `.setupEnvironment( builder :NodeBuilder) :Node.<vec4>` — Setups the environment node from the material.
- `.setupFog( builder :NodeBuilder, outputNode :Node.<vec4>) :Node.<vec4>` — Setup the fog.
- `.setupHardwareClipping( builder :NodeBuilder)` — Setups the hardware clipping if available on the current device.
- `.setupLightMap( builder :NodeBuilder) :Node.<vec3>` — Setups the light map node from the material.
- `.setupLighting( builder :NodeBuilder) :Node.<vec3>` — Setups the outgoing light node.
- `.setupLightingModel( builder :NodeBuilder) :LightingModel` — This method should be implemented by most derived materials
since it defines the material's lighting model.
- `.setupLights( builder :NodeBuilder) :LightsNode` — Setups the lights node based on the scene, environment and material.
- `.setupModelViewProjection( builder :NodeBuilder) :Node.<vec4>` — Setups the position in clip space.
- `.setupNormal() :Node.<vec3>` — Setups the normal node from the material.
- `.setupObserver( builder :NodeBuilder) :NodeMaterialObserver` — Setups a node material observer with the given builder.
- `.setupOutgoingLight() :Node.<vec3>` — Setups the outgoing light node variable
- `.setupOutput( builder :NodeBuilder, outputNode :Node.<vec4>) :Node.<vec4>` — Setups the output node.
- `.setupPosition( builder :NodeBuilder) :Node.<vec3>` — Setups the computation of the position in local space.
- `.setupPositionView( builder :NodeBuilder) :Node.<vec3>` — Setups the position node in view space. This method exists
so derived node materials can modify the implementation e.g. sprite materials.
- `.setupPremultipliedAlpha( builder :NodeBuilder, outputNode :Node.<vec4>) :Node.<vec4>` — Setups premultiplied alpha.
- `.setupVariants( builder :NodeBuilder) (abstract)` — Abstract interface method that can be implemented by derived materials
to setup material-specific node variables.
- `.setupVertex( builder :NodeBuilder) :Node.<vec4>` — Setups the logic for the vertex stage.
- `.toJSON( meta :Object | string) : Object` — Serializes this material to JSON.

## Source