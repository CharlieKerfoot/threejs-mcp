# MeshPhongNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of MeshPhongMaterial .

## Constructor
`newMeshPhongNodeMaterial( parameters :Object)`
Constructs a new mesh lambert node material.

## Properties
- `.isMeshPhongNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Set to true because phong materials react on lights. Default is true .
- `.shininessNode :Node.<float>` — The shininess of phong materials is by default inferred from the shininess property. This node property allows to overwrite the default
and define the shininess with a node instead. If you don't wa...
- `.specularNode :Node.<vec3>` — The specular color of phong materials is by default inferred from the specular property. This node property allows to overwrite the default
and define the specular color with a node instead. If you...

## Methods
- `.setupEnvironment( builder :NodeBuilder) :BasicEnvironmentNode.<vec3>` — Overwritten since this type of material uses BasicEnvironmentNode to implement the default environment mapping.
- `.setupLightingModel() :PhongLightingModel` — Setups the lighting model.
- `.setupVariants( builder :NodeBuilder)` — Setups the phong specific node variables.

## Source