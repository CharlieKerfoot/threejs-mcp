# BasicLightingModel
Extends: LightingModel→

Represents the lighting model for unlit materials. The only light contribution
is baked indirect lighting modulated with ambient occlusion and the material's
diffuse color. Environment mapping is supported. Used in MeshBasicNodeMaterial .

## Constructor
`newBasicLightingModel()`
Constructs a new basic lighting model.

## Methods
- `.finish( builder :NodeBuilder)` — Implements the environment mapping.
- `.indirect( builder :NodeBuilder)` — Implements the baked indirect lighting with its modulation.

## Source