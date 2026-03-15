# DepthOfFieldNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating depth of field (DOF) effect. References: https://pixelmischiefblog.wordpress.com/2016/11/25/bokeh-depth-of-field/ https://www.adriancourreges.com/blog/2016/09/09/doom-2016-graphics-study/

## Constructor
`newDepthOfFieldNode( textureNode :TextureNode, viewZNode :Node.<float>, focusDistanceNode :Node.<float>, focalLengthNode :Node.<float>, bokehScaleNode :Node.<float>)`
Constructs a new DOF node.

## Import

## Properties
- `.bokehScaleNode :Node.<float>` — A unitless value for artistic purposes to adjust the size of the bokeh.
- `.focalLengthNode :Node.<float>` — How far an object can be from the focal plane before it goes completely out-of-focus in world units.
- `.focusDistanceNode :Node.<float>` — Defines the effect's focus which is the distance along the camera's look direction in world units.
- `.textureNode :TextureNode` — The texture node that represents the input of the effect.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node updates
its internal uniforms once per frame in updateBefore() . Default is 'frame' .
- `.viewZNode :Node.<float>` — Represents the viewZ depth values of the scene.

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.getTextureNode() :PassTextureNode` — Returns the result of the effect as a texture node.
- `.setSize( width :number, height :number)` — Sets the size of the effect.
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to update the effect's uniforms once per frame.

## Source