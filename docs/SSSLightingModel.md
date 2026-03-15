# SSSLightingModel
Extends: LightingModel→PhysicalLightingModel→

Represents the lighting model for MeshSSSNodeMaterial .

## Constructor
`newSSSLightingModel( clearcoat :boolean, sheen :boolean, iridescence :boolean, anisotropy :boolean, transmission :boolean, dispersion :boolean, sss :boolean)`
Constructs a new physical lighting model.

## Properties
- `.useSSS : boolean` — Whether the lighting model should use SSS or not. Default is false .

## Methods
- `.direct( input :Object, builder :NodeBuilder)` — Extends the default implementation with a SSS term. Reference: Approximating Translucency for a Fast, Cheap and Convincing Subsurface Scattering Look

## Source