# ShadowMaskModel
Extends: LightingModel→

Represents lighting model for a shadow material. Used in ShadowNodeMaterial .

## Constructor
`newShadowMaskModel()`
Constructs a new shadow mask model.

## Properties
- `.shadowNode :Node` — The shadow mask node.

## Methods
- `.direct( input :Object)` — Only used to save the shadow mask.
- `.finish( builder :NodeBuilder)` — Uses the shadow mask to produce the final color.

## Source