# AnalyticLightNode
Extends: EventDispatcher→Node→LightingNode→

Base class for analytic light nodes.

## Constructor
`newAnalyticLightNode( light :Light)`
Constructs a new analytic light node.

## Properties
- `.baseColorNode :Node` — This property is used to retain a reference to the original value of AnalyticLightNode#colorNode .
The final color node is represented by a different node when using shadows. Default is null .
- `.color :Color` — The light's color value.
- `.colorNode :Node` — The light's color node. Points to colorNode of the light source, if set. Otherwise
it creates a uniform node based on AnalyticLightNode#color .
- `.isAnalyticLightNode : boolean` — This flag can be used for type testing. Default is true .
- `.light :Light` — The light source. Default is null .
- `.shadowColorNode :Node` — Represents the light's shadow color. Default is null .
- `.shadowNode :ShadowNode` — Represents the light's shadow. Default is null .
- `.updateType : string` — Overwritten since analytic light nodes are updated
once per frame. Default is 'frame' .

## Methods
- `.disposeShadow()` — Frees internal resources related to shadows.
- `.getLightVector( builder :NodeBuilder) :Node.<vec3>` — Returns a node representing a direction vector which points from the current
position in view space to the light's position in view space.
- `.setup( builder :NodeBuilder)` — Unlike most other nodes, lighting nodes do not return a output node in Node#setup .
The main purpose of lighting nodes is to configure the current LightingModel and/or
invocate the respective inter...
- `.setupDirect( builder :NodeBuilder) : Object | undefined` — Sets up the direct lighting for the analytic light node.
- `.setupDirectRectArea( builder :NodeBuilder) : Object | undefined` — Sets up the direct rect area lighting for the analytic light node.
- `.setupShadow( builder :NodeBuilder)` — Setups the shadow for this light. This method is only executed if the light
cast shadows and the current build object receives shadows. It incorporates
shadows into the lighting computation.
- `.setupShadowNode() :ShadowNode` — Setups the shadow node for this light. The method exists so concrete light classes
can setup different types of shadow nodes.
- `.update( frame :NodeFrame)` — The update method is used to update light uniforms per frame.
Potentially overwritten in concrete light nodes to update light
specific uniforms.

## Source