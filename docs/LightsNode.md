# LightsNode
Extends: EventDispatcher→Node→

This node represents the scene's lighting and manages the lighting model's life cycle
for the current build 3D object. It is responsible for computing the total outgoing
light in a given lighting context.

## Constructor
`newLightsNode()`
Constructs a new lights node.

## Properties
- `.global : boolean` — LightsNode sets this property to true by default. Default is true .
- `.hasLights : boolean` — Whether the scene has lights or not.
- `.outgoingLightNode :Node.<vec3>` — A node representing the outgoing light.
- `.totalDiffuseNode :Node.<vec3>` — A node representing the total diffuse light.
- `.totalSpecularNode :Node.<vec3>` — A node representing the total specular light.

## Methods
- `.customCacheKey() : number` — Overwrites the default Node#customCacheKey implementation by including
light data into the cache key.
- `.getHash( builder :NodeBuilder) : string` — Computes a hash value for identifying the current light nodes setup.
- `.getLights() : Array.<Light>` — Returns an array of the scene's lights.
- `.setLights( lights :Array.<Light>) :LightsNode` — Configures this node with an array of lights.
- `.setup( builder :NodeBuilder) :Node.<vec3>` — The implementation makes sure that for each light in the scene
there is a corresponding light node. By building the light nodes
and evaluating the lighting model the outgoing light is computed.
- `.setupDirectLight( builder :Object, lightNode :Object, lightData :Object)` — Sets up a direct light in the lighting model.
- `.setupLights( builder :NodeBuilder, lightNodes :Array.<LightingNode>)` — Setups the internal lights by building all respective
light nodes.
- `.setupLightsNode( builder :NodeBuilder)` — Creates lighting nodes for each scene light. This makes it possible to further
process lights in the node system.

## Source