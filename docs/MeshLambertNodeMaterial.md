# MeshLambertNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of MeshLambertMaterial .

## Constructor
`newMeshLambertNodeMaterial( parameters :Object)`
Constructs a new mesh lambert node material.

## Properties
- `.isMeshLambertNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Set to true because lambert materials react on lights. Default is true .

## Methods
- `.setupEnvironment( builder :NodeBuilder) :BasicEnvironmentNode.<vec3>` — Overwritten since this type of material uses BasicEnvironmentNode to implement the default environment mapping.
- `.setupLightingModel() :PhongLightingModel` — Setups the lighting model.

## Source