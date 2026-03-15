# PhysicalLightingModel
Extends: LightingModel→

Represents the lighting model for a PBR material.

## Constructor
`newPhysicalLightingModel( clearcoat :boolean, sheen :boolean, iridescence :boolean, anisotropy :boolean, transmission :boolean, dispersion :boolean)`
Constructs a new physical lighting model.

## Properties
- `.anisotropy : boolean` — Whether anisotropy is supported or not. Default is false .
- `.clearcoat : boolean` — Whether clearcoat is supported or not. Default is false .
- `.clearcoatRadiance :Node` — The clear coat radiance. Default is null .
- `.clearcoatSpecularDirect :Node` — The clear coat specular direct. Default is null .
- `.clearcoatSpecularIndirect :Node` — The clear coat specular indirect. Default is null .
- `.dispersion : boolean` — Whether dispersion is supported or not. Default is false .
- `.iridescence : boolean` — Whether iridescence is supported or not. Default is false .
- `.iridescenceF0 :Node` — The iridescence F0. Default is null .
- `.iridescenceF0Dielectric :Node` — The iridescence F0 dielectric. Default is null .
- `.iridescenceF0Metallic :Node` — The iridescence F0 metallic. Default is null .
- `.iridescenceFresnel :Node` — The iridescence Fresnel. Default is null .
- `.sheen : boolean` — Whether sheen is supported or not. Default is false .
- `.sheenSpecularDirect :Node` — The sheen specular direct. Default is null .
- `.sheenSpecularIndirect :Node` — The sheen specular indirect. Default is null .
- `.transmission : boolean` — Whether transmission is supported or not. Default is false .

## Methods
- `.ambientOcclusion( builder :NodeBuilder)` — Implements the ambient occlusion term.
- `.direct( lightData :Object, builder :NodeBuilder)` — Implements the direct light.
- `.directRectArea( input :Object, builder :NodeBuilder)` — This method is intended for implementing the direct light term for
rect area light nodes.
- `.finish( builder :NodeBuilder)` — Used for final lighting accumulations depending on the requested features.
- `.indirect( builder :NodeBuilder)` — Implements the indirect lighting.
- `.indirectDiffuse( builder :NodeBuilder)` — Implements the indirect diffuse term.
- `.indirectSpecular( builder :NodeBuilder)` — Implements the indirect specular term.
- `.start( builder :NodeBuilder)` — Depending on what features are requested, the method prepares certain node variables
which are later used for lighting computations.

## Source