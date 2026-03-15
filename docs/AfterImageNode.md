# AfterImageNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating an after image effect.

## Constructor
`newAfterImageNode( textureNode :TextureNode, damp :Node.<float>)`
Constructs a new after image node.

## Import

## Properties
- `.damp :Node.<float>` — How quickly the after-image fades. A higher value means the after-image
persists longer, while a lower value means it fades faster. Should be in
the range [0, 1] .
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