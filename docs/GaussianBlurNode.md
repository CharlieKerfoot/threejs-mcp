# GaussianBlurNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating a gaussian blur effect.

## Constructor
`newGaussianBlurNode( textureNode :TextureNode, directionNode :Node.<(vec2|float)>, sigma :number, options :Object)`
Constructs a new gaussian blur node.

## Import

## Properties
- `.directionNode :Node.<(vec2|float)>` — Defines the direction and radius of the blur.
- `.isGaussianBlurNode : boolean` — This flag can be used for type testing. Default is true .
- `.premultipliedAlpha : boolean` — Whether the effect should use premultiplied alpha or not. Set this to true if you are going to blur texture input with transparency. Default is false .
- `.resolution :Vector2` — The resolution scale. Default is {(1,1)} .
- `.resolutionScale : number` — The resolution scale. Default is (1) .
- `.sigma : number` — Controls the kernel of the blur filter. Higher values mean a wider blur radius.
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