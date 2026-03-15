# ToonOutlinePassNode
Extends: EventDispatcher→Node→TempNode→PassNode→

Represents a render pass for producing a toon outline effect on compatible objects.
Only 3D objects with materials of type MeshToonMaterial and MeshToonNodeMaterial will receive the outline.

## Constructor
`newToonOutlinePassNode( scene :Scene, camera :Camera, colorNode :Node, thicknessNode :Node, alphaNode :Node)`
Constructs a new outline pass node.

## Properties
- `.alphaNode :Node` — Defines the outline's alpha.
- `.colorNode :Node` — Defines the outline's color.
- `.name : string` — The name of this pass. Default is 'Outline Pass' .
- `.thicknessNode :Node` — Defines the outline's thickness.

## Source