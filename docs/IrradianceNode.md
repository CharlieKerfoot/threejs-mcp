# IrradianceNode
Extends: EventDispatcher→Node→LightingNode→

A generic class that can be used by nodes which contribute
irradiance to the scene. E.g. a light map node can be used
as input for this module. Used in NodeMaterial .

## Constructor
`newIrradianceNode( node :Node.<vec3>)`
Constructs a new irradiance node.

## Properties
- `.node :Node.<vec3>` — A node contributing irradiance.

## Source