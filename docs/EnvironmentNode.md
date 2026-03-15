# EnvironmentNode
Extends: EventDispatcher→Node→LightingNode→

Represents a physical model for Image-based lighting (IBL). The environment
is defined via environment maps in the equirectangular, cube map or cubeUV (PMREM) format. EnvironmentNode is intended for PBR materials like MeshStandardNodeMaterial .

## Constructor
`newEnvironmentNode( envNode :Node)`
Constructs a new environment node.

## Properties
- `.envNode :Node` — A node representing the environment. Default is null .

## Source