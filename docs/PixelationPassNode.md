# PixelationPassNode
Extends: EventDispatcher→Node→TempNode→PassNode→

A special render pass node that renders the scene with a pixelation effect.

## Constructor
`newPixelationPassNode( scene :Scene, camera :Camera, pixelSize :Node.<float> | number, normalEdgeStrength :Node.<float> | number, depthEdgeStrength :Node.<float> | number)`
Constructs a new pixelation pass node.

## Import

## Properties
- `.depthEdgeStrength : number` — The depth edge strength. Default is 0.4 .
- `.isPixelationPassNode : boolean` — This flag can be used for type testing. Default is true .
- `.normalEdgeStrength : number` — The normal edge strength. Default is 0.3 .
- `.pixelSize : number` — The pixel size. Default is 6 .

## Methods
- `.setSize( width :number, height :number)` — Sets the size of the pass.
- `.setup( builder :NodeBuilder) :PixelationNode` — This method is used to setup the effect's TSL code.

## Source