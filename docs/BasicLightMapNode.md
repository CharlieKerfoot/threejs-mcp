# BasicLightMapNode
Extends: EventDispatcher→Node→LightingNode→

A specific version of IrradianceNode that is only relevant
for MeshBasicNodeMaterial . Since the material is unlit, it
requires a special scaling factor for the light map.

## Constructor
`newBasicLightMapNode( lightMapNode :Node.<vec3>)`
Constructs a new basic light map node.

## Properties
- `.lightMapNode :Node.<vec3>` — The light map node.

## Source