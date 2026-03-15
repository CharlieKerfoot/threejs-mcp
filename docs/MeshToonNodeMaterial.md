# MeshToonNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of MeshToonMaterial .

## Constructor
`newMeshToonNodeMaterial( parameters :Object)`
Constructs a new mesh toon node material.

## Properties
- `.isMeshToonNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Set to true because toon materials react on lights. Default is true .

## Methods
- `.setupLightingModel() :ToonLightingModel` — Setups the lighting model.

## Source