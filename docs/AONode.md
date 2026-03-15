# AONode
Extends: EventDispatcher→Node→LightingNode→

A generic class that can be used by nodes which contribute
ambient occlusion to the scene. E.g. an ambient occlusion map
node can be used as input for this module. Used in NodeMaterial .

## Constructor
`newAONode( aoNode :Node.<float>)`
Constructs a new AO node.

## Properties
- `.aoNode :Node.<float>` — The ambient occlusion node. Default is null .

## Source