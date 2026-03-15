# BasicEnvironmentNode
Extends: EventDispatcher→Node→LightingNode→

Represents a basic model for Image-based lighting (IBL). The environment
is defined via environment maps in the equirectangular or cube map format. BasicEnvironmentNode is intended for non-PBR materials like MeshBasicNodeMaterial or MeshPhongNodeMaterial .

## Constructor
`newBasicEnvironmentNode( envNode :Node)`
Constructs a new basic environment node.

## Properties
- `.envNode :Node` — A node representing the environment. Default is null .

## Source