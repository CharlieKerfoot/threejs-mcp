# ShadowNode
Extends: EventDispatcher→Node→ShadowBaseNode→

Represents the default shadow implementation for lighting nodes.

## Constructor
`newShadowNode( light :Light, shadow :LightShadow)`
Constructs a new shadow node.

## Properties
- `.depthLayer : number` — This index can be used when overriding setupRenderTarget with a RenderTarget Array to specify the depth layer. Default is true .
- `.isShadowNode : boolean` — This flag can be used for type testing. Default is true .
- `.shadow :LightShadow` — The light shadow which defines the properties light's
shadow. Default is null .
- `.shadowMap :RenderTarget` — A reference to the shadow map which is a render target. Default is null .
- `.vsmMaterialHorizontal :NodeMaterial` — Only relevant for VSM shadows. Node material which
is used to render the second VSM pass. Default is null .
- `.vsmMaterialVertical :NodeMaterial` — Only relevant for VSM shadows. Node material which
is used to render the first VSM pass. Default is null .
- `.vsmShadowMapHorizontal :RenderTarget` — Only relevant for VSM shadows. Render target for the
second VSM render pass. Default is null .
- `.vsmShadowMapVertical :RenderTarget` — Only relevant for VSM shadows. Render target for the
first VSM render pass. Default is null .

## Methods
- `.dispose()` — Frees the internal resources of this shadow node.
- `.getShadowFilterFn( type :number) : function` — Returns the shadow filtering function for the given shadow type.
- `.renderShadow( frame :NodeFrame)` — Renders the shadow. The logic of this function could be included
into ShadowNode#updateShadow however more specialized shadow
nodes might require a custom shadow map rendering. By having a
dedicate...
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — The implementation performs the setup of the output node. An output is only
produces if shadow mapping is globally enabled in the renderer.
- `.setupShadow( builder :NodeBuilder) :Node.<vec3>` — Setups the shadow output node.
- `.setupShadowCoord( builder :NodeBuilder, shadowPosition :Node.<vec3>) :Node.<vec3>` — Setups the shadow coordinates.
- `.setupShadowFilter( builder :NodeBuilder, inputs :Object) :Node.<float>` — Setups the shadow filtering.
- `.updateBefore( frame :NodeFrame)` — The implementation performs the update of the shadow map if necessary.
- `.updateShadow( frame :NodeFrame)` — Updates the shadow.
- `.vsmPass( renderer :Renderer)` — For VSM additional render passes are required.

## Source