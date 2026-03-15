# ShadowNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of ShadowMaterial .

## Constructor
`newShadowNodeMaterial( parameters :Object)`
Constructs a new shadow node material.

## Properties
- `.isShadowNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Set to true because so it's possible to implement
the shadow mask effect. Default is true .
- `.transparent : boolean` — Overwritten since shadow materials are transparent
by default. Default is true .

## Methods
- `.setupLightingModel() :ShadowMaskModel` — Setups the lighting model.

## Source