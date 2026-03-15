# PointShadowNode
Extends: EventDispatcher→Node→ShadowBaseNode→ShadowNode→

Represents the shadow implementation for point light nodes.

## Constructor
`newPointShadowNode( light :PointLight, shadow :PointLightShadow)`
Constructs a new point shadow node.

## Methods
- `.getShadowFilterFn( type :number) : function` — Overwrites the default implementation to return point light shadow specific
filtering functions.
- `.renderShadow( frame :NodeFrame)` — Overwrites the default implementation with point light specific
rendering code.
- `.setupRenderTarget( shadow :LightShadow, builder :NodeBuilder) : Object` — Overwrites the default implementation to create a CubeRenderTarget with CubeDepthTexture.
- `.setupShadowCoord( builder :NodeBuilder, shadowPosition :Node.<vec3>) :Node.<vec3>` — Overwrites the default implementation so the unaltered shadow position is used.
- `.setupShadowFilter( builder :NodeBuilder, inputs :Object) :Node.<float>` — Overwrites the default implementation to only use point light specific
shadow filter functions.

## Source