# MeshPhysicalNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→MeshStandardNodeMaterial→

Node material version of MeshPhysicalMaterial .

## Constructor
`newMeshPhysicalNodeMaterial( parameters :Object)`
Constructs a new mesh physical node material.

## Properties
- `.anisotropyNode :Node.<float>` — The anisotropy of physical materials is by default inferred from the anisotropy property. This node property allows to overwrite the default
and define the anisotropy with a node instead. If you do...
- `.attenuationColorNode :Node.<vec3>` — The attenuation color of physical materials is by default inferred from the attenuationColor property. This node property allows to overwrite the default
and define the attenuation color with a nod...
- `.attenuationDistanceNode :Node.<float>` — The attenuation distance of physical materials is by default inferred from the attenuationDistance property. This node property allows to overwrite the default
and define the attenuation distance w...
- `.clearcoatNode :Node.<float>` — The clearcoat of physical materials is by default inferred from the clearcoat and clearcoatMap properties. This node property allows to overwrite the default
and define the clearcoat with a node in...
- `.clearcoatNormalNode :Node.<vec3>` — The clearcoat normal of physical materials is by default inferred from the clearcoatNormalMap property. This node property allows to overwrite the default
and define the clearcoat normal with a nod...
- `.clearcoatRoughnessNode :Node.<float>` — The clearcoat roughness of physical materials is by default inferred from the clearcoatRoughness and clearcoatRoughnessMap properties. This node property allows to overwrite the default
and define ...
- `.dispersionNode :Node.<float>` — The dispersion of physical materials is by default inferred from the dispersion property. This node property allows to overwrite the default
and define the dispersion with a node instead. If you do...
- `.iorNode :Node.<float>` — The ior of physical materials is by default inferred from the ior property. This node property allows to overwrite the default
and define the ior with a node instead. If you don't want to overwrite...
- `.iridescenceIORNode :Node.<float>` — The iridescence IOR of physical materials is by default inferred from the iridescenceIOR property. This node property allows to overwrite the default
and define the iridescence IOR with a node inst...
- `.iridescenceNode :Node.<float>` — The iridescence of physical materials is by default inferred from the iridescence property. This node property allows to overwrite the default
and define the iridescence with a node instead. If you...
- `.iridescenceThicknessNode :Node.<float>` — The iridescence thickness of physical materials is by default inferred from the iridescenceThicknessRange and iridescenceThicknessMap properties. This node property allows to overwrite the default
...
- `.isMeshPhysicalNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.sheenNode :Node.<vec3>` — The sheen of physical materials is by default inferred from the sheen , sheenColor and sheenColorMap properties. This node property allows to overwrite the default
and define the sheen with a node ...
- `.sheenRoughnessNode :Node.<float>` — The sheen roughness of physical materials is by default inferred from the sheenRoughness and sheenRoughnessMap properties. This node property allows to overwrite the default
and define the sheen ro...
- `.specularColorNode :Node.<vec3>` — The specular color of physical materials is by default inferred from the specularColor and specularColorMap properties. This node property allows to overwrite the default
and define the specular co...
- `.specularIntensityNode :Node.<float>` — The specular intensity of physical materials is by default inferred from the specularIntensity and specularIntensityMap properties. This node property allows to overwrite the default
and define the...
- `.thicknessNode :Node.<float>` — The thickness of physical materials is by default inferred from the thickness and thicknessMap properties. This node property allows to overwrite the default
and define the thickness with a node in...
- `.transmissionNode :Node.<float>` — The transmission of physical materials is by default inferred from the transmission and transmissionMap properties. This node property allows to overwrite the default
and define the transmission wi...
- `.useAnisotropy : boolean` — Whether the lighting model should use anisotropy or not. Default is true .
- `.useClearcoat : boolean` — Whether the lighting model should use clearcoat or not. Default is true .
- `.useDispersion : boolean` — Whether the lighting model should use dispersion or not. Default is true .
- `.useIridescence : boolean` — Whether the lighting model should use iridescence or not. Default is true .
- `.useSheen : boolean` — Whether the lighting model should use sheen or not. Default is true .
- `.useTransmission : boolean` — Whether the lighting model should use transmission or not. Default is true .

## Methods
- `.setupClearcoatNormal() :Node.<vec3>` — Setups the clearcoat normal node.
- `.setupLightingModel() :PhysicalLightingModel` — Setups the lighting model.
- `.setupSpecular()` — Setups the specular related node variables.
- `.setupVariants( builder :NodeBuilder)` — Setups the physical specific node variables.

## Source