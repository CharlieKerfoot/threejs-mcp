# PMREMNode
Extends: EventDispatcher→Node→TempNode→

This node represents a PMREM which is a special type of preprocessed
environment map intended for PBR materials.

## Constructor
`newPMREMNode( value :Texture, uvNode :Node.<vec2>, levelNode :Node.<float>)`
Constructs a new function overloading node.

## Properties
- `.levelNode :Node.<float>` — The level node.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.RENDER . Default is 'render' .
- `.uvNode :Node.<vec2>` — The uv node.
- `.value :Texture` — The node's texture value.

## Methods
- `.updateFromTexture( texture :Texture)` — Uses the given PMREM texture to update internal values.

## Source