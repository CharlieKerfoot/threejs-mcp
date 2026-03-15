# BilateralBlurNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating a bilateral blur effect. Bilateral blur smooths an image while preserving sharp edges. Unlike a
standard Gaussian blur which blurs everything equally, bilateral blur
analyzes the intensity/color of neighboring pixels. If a neighbor is too
different from the center pixel (indicating an edge), it is excluded
from the blurring process. Reference: https://en.wikipedia.org/wiki/Bilateral_filter

## Constructor
`newBilateralBlurNode( textureNode :TextureNode, directionNode :Node.<(vec2|float)>, sigma :number, sigmaColor :number)`
Constructs a new bilateral blur node.

## Import

## Properties
- `.directionNode :Node.<(vec2|float)>` — Defines the direction and radius of the blur.
- `.resolutionScale : number` — The resolution scale. Default is 1 .
- `.sigma : number` — Controls the spatial kernel of the blur filter. Higher values mean a wider blur radius.
- `.sigmaColor : number` — Controls the color/intensity kernel. Higher values allow more color difference
to be blurred together. Lower values preserve edges more strictly.
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