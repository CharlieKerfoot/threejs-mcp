# SMAANode
Extends: EventDispatcher→Node→TempNode→

Post processing node for applying SMAA. Unlike FXAA, this node
should be applied before converting colors to sRGB. SMAA should produce
better results than FXAA but is also more expensive to execute. Used Preset: SMAA 1x Medium (with color edge detection)
Reference: https://github.com/iryoku/smaa/releases/tag/v2.8 .

## Constructor
`newSMAANode( textureNode :TextureNode)`
Constructs a new SMAA node.

## Import

## Properties
- `.textureNode :TextureNode` — The texture node that represents the input of the effect.
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