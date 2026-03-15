# MeshBasicNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of MeshBasicMaterial .

## Constructor
`newMeshBasicNodeMaterial( parameters :Object)`
Constructs a new mesh basic node material.

## Properties
- `.isMeshBasicNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Although the basic material is by definition unlit, we set
this property to true since we use a lighting model to compute
the outgoing light of the fragment shader. Default is true .

## Methods
- `.setupEnvironment( builder :NodeBuilder) :BasicEnvironmentNode.<vec3>` — Overwritten since this type of material uses BasicEnvironmentNode to implement the default environment mapping.
- `.setupLightMap( builder :NodeBuilder) :BasicLightMapNode.<vec3>` — This method must be overwritten since light maps are evaluated
with a special scaling factor for basic materials.
- `.setupLightingModel() :BasicLightingModel` — Setups the lighting model.
- `.setupNormal() :Node.<vec3>` — Basic materials are not affected by normal and bump maps so we
return by default normalViewGeometry .
- `.setupOutgoingLight() :Node.<vec3>` — The material overwrites this method because lights is set to true but
we still want to return the diffuse color as the outgoing light.

## Source