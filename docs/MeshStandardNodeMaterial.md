# MeshStandardNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of MeshStandardMaterial .

## Constructor
`newMeshStandardNodeMaterial( parameters :Object)`
Constructs a new mesh standard node material.

## Properties
- `.emissiveNode :Node.<vec3>` — The emissive color of standard materials is by default inferred from the emissive , emissiveIntensity and emissiveMap properties. This node property allows to
overwrite the default and define the e...
- `.isMeshStandardNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Set to true because standard materials react on lights. Default is true .
- `.metalnessNode :Node.<float>` — The metalness of standard materials is by default inferred from the metalness ,
and metalnessMap properties. This node property allows to
overwrite the default and define the metalness with a node ...
- `.roughnessNode :Node.<float>` — The roughness of standard materials is by default inferred from the roughness ,
and roughnessMap properties. This node property allows to
overwrite the default and define the roughness with a node ...

## Methods
- `.setupEnvironment( builder :NodeBuilder) :EnvironmentNode.<vec3>` — Overwritten since this type of material uses EnvironmentNode to implement the PBR (PMREM based) environment mapping. Besides, the
method honors Scene.environment .
- `.setupLightingModel() :PhysicalLightingModel` — Setups the lighting model.
- `.setupSpecular()` — Setups the specular related node variables.
- `.setupVariants( builder :NodeBuilder)` — Setups the standard specific node variables.

## Source