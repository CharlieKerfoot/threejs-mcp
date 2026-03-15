# AnamorphicNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for adding an anamorphic flare effect.

## Constructor
`newAnamorphicNode( textureNode :TextureNode, thresholdNode :Node.<float>, scaleNode :Node.<float>, samples :number)`
Constructs a new anamorphic node.

## Import

## Properties
- `.colorNode :Node.<vec3>` — The color of the flares.
- `.resolution :Vector2` — The resolution scale. Default is {(1,1)} .
- `.resolutionScale : number` — The resolution scale.
- `.samples :Node.<float>` — More samples result in larger flares and a more expensive runtime behavior.
- `.scaleNode :Node.<float>` — Defines the vertical scale of the flares.
- `.textureNode :TextureNode` — The texture node that represents the input of the effect.
- `.thresholdNode :Node.<float>` — The threshold is one option to control the intensity and size of the effect.
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