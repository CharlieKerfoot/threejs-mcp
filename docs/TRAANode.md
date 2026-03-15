# TRAANode
Extends: EventDispatcher→Node→TempNode→

A special node that applies TRAA (Temporal Reprojection Anti-Aliasing). References: https://alextardif.com/TAA.html https://www.elopezr.com/temporal-aa-and-the-quest-for-the-holy-trail/

## Constructor
`newTRAANode( beautyNode :TextureNode, depthNode :TextureNode, velocityNode :TextureNode, camera :Camera)`
Constructs a new TRAA node.

## Import

## Properties
- `.beautyNode :TextureNode` — The texture node that represents the input of the effect.
- `.camera :Camera` — The camera the scene is rendered with.
- `.depthNode :TextureNode` — A node that represents the scene's velocity.
- `.depthThreshold : number` — When the difference between the current and previous depth goes above this threshold,
the history is considered invalid. Default is 0.0005 .
- `.edgeDepthDiff : number` — The depth difference within the 3×3 neighborhood to consider a pixel as an edge. Default is 0.001 .
- `.isTRAANode : boolean` — This flag can be used for type testing. Default is true .
- `.maxVelocityLength : number` — The history becomes invalid as the pixel length of the velocity approaches this value. Default is 128 .
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node renders
its effect once per frame in updateBefore() . Default is 'frame' .
- `.useSubpixelCorrection : boolean` — Whether to decrease the weight on the current frame when the velocity is more subpixel.
This reduces blurriness under motion, but can introduce a square pattern artifact. Default is true .
- `.velocityNode :TextureNode` — A node that represents the scene's velocity.

## Methods
- `.clearViewOffset()` — Clears the view offset from the scene's camera.
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.getTextureNode() :PassTextureNode` — Returns the result of the effect as a texture node.
- `.setSize( width :number, height :number)` — Sets the size of the effect.
- `.setViewOffset( width :number, height :number)` — Defines the TRAA's current jitter as a view offset
to the scene's camera.
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's render targets and TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the effect once per frame.

## Source