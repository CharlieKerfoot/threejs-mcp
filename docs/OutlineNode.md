# OutlineNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for rendering outlines around selected objects. The node
gives you great flexibility in composing the final outline look depending on
your requirements.

## Constructor
`newOutlineNode( scene :Scene, camera :Camera, params :Object)`
Constructs a new outline node.

## Import

## Properties
- `.camera :Camera` — The camera the scene is rendered with.
- `.downSampleRatio : number` — The downsample ratio. Default is 2 .
- `.edgeGlowNode :Node.<float>` — Can be used for an animated glow/pulse effect.
- `.edgeThicknessNode :Node.<float>` — The thickness of the edges.
- `.hiddenEdge` — A mask value that represents the hidden edge.
- `.scene :Scene` — A reference to the scene.
- `.selectedObjects : Array.<Object3D>` — An array of selected objects.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node renders
its effect once per frame in updateBefore() . Default is 'frame' .
- `.visibleEdge` — A mask value that represents the visible edge.

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.getTextureNode() :PassTextureNode` — Returns the result of the effect as a texture node.
- `.setSize( width :number, height :number)` — Sets the size of the effect.
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the effect once per frame.

## Source