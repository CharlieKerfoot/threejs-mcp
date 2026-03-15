# LensflareNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for adding a bloom-based lens flare effect. This effect
requires that you extract the bloom of the scene via a bloom pass first. References: https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html . https://john-chapman.github.io/2017/11/05/pseudo-lens-flare.html .

## Constructor
`newLensflareNode( textureNode :TextureNode, params :Object)`
Constructs a new lens flare node.

## Import

## Properties
- `.downSampleRatio : number` — Defines how downsampling since the effect is usually not rendered at full resolution.
- `.ghostAttenuationFactorNode :Node.<float>` — Defines the attenuation factor of flares/ghosts.
- `.ghostSamplesNode :Node.<float>` — Represents the number of flares/ghosts per bright spot which pivot around the center.
- `.ghostSpacingNode :Node.<float>` — Defines the spacing of the flares/ghosts.
- `.ghostTintNode :Node.<vec3>` — Defines the tint of the flare/ghosts.
- `.textureNode :TextureNode` — The texture node that represents the scene's bloom.
- `.thresholdNode :Node.<float>` — Controls the size and strength of the effect. A higher threshold results in smaller flares.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node renders
its effect once per frame in updateBefore() . Default is 'frame' .

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.getTextureNode() :PassTextureNode` — Returns the result of the effect as a texture node.
- `.setSize( width :number, height :number)` — Sets the size of the effect.
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the effect once per frame.

## Source