# MeshNormalNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of MeshNormalMaterial .

## Constructor
`newMeshNormalNodeMaterial( parameters :Object)`
Constructs a new mesh normal node material.

## Properties
- `.isMeshNormalNodeMaterial : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.setupDiffuseColor()` — Overwrites the default implementation by computing the diffuse color
based on the normal data.

## Source