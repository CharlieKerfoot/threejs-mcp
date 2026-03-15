# MeshSSSNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→MeshStandardNodeMaterial→MeshPhysicalNodeMaterial→

This node material is an experimental extension of MeshPhysicalNodeMaterial that implements a Subsurface scattering (SSS) term.

## Constructor
`newMeshSSSNodeMaterial( parameters :Object)`
Constructs a new mesh SSS node material.

## Properties
- `.thicknessAmbientNode :Node.<float>` — Represents the thickness ambient factor.
- `.thicknessAttenuationNode :Node.<float>` — Represents the thickness attenuation.
- `.thicknessColorNode :Node.<vec3>` — Represents the thickness color. Default is null .
- `.thicknessDistortionNode :Node.<float>` — Represents the distortion factor.
- `.thicknessPowerNode :Node.<float>` — Represents the thickness power.
- `.thicknessScaleNode :Node.<float>` — Represents the thickness scale.
- `.useSSS : boolean` — Whether the lighting model should use SSS or not. Default is true .

## Methods
- `.setupLightingModel() :SSSLightingModel` — Setups the lighting model.

## Source