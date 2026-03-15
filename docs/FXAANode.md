# FXAANode
Extends: EventDispatcher→Node→TempNode→

Post processing node for applying FXAA. This node requires sRGB input
so tone mapping and color space conversion must happen before the anti-aliasing.

## Constructor
`newFXAANode( textureNode :TextureNode)`
Constructs a new FXAA node.

## Import

## Properties
- `.textureNode :TextureNode` — The texture node that represents the input of the effect.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node updates
its internal uniforms once per frame in updateBefore() . Default is 'frame' .

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to update the effect's uniforms once per frame.

## Source