# ParallaxBarrierPassNode
Extends: EventDispatcher→Node→TempNode→PassNode→StereoCompositePassNode→

A render pass node that creates a parallax barrier effect.

## Constructor
`newParallaxBarrierPassNode( scene :Scene, camera :Camera)`
Constructs a new parallax barrier pass node.

## Import

## Properties
- `.isParallaxBarrierPassNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's TSL code.

## Source