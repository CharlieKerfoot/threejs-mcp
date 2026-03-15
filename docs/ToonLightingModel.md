# ToonLightingModel
Extends: LightingModel→

Represents the lighting model for a toon material. Used in MeshToonNodeMaterial .

## Constructor
`newToonLightingModel()`

## Methods
- `.direct( lightData :Object, builder :NodeBuilder)` — Implements the direct lighting. Instead of using a conventional smooth irradiance, the irradiance is
reduced to a small number of discrete shades to create a comic-like, flat look.
- `.indirect( builder :NodeBuilder)` — Implements the indirect lighting.

## Source