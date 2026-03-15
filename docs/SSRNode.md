# SSRNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for computing screen space reflections (SSR). Reference: https://lettier.github.io/3d-game-shaders-for-beginners/screen-space-reflection.html

## Constructor
`newSSRNode( colorNode :Node.<vec4>, depthNode :Node.<float>, normalNode :Node.<vec3>, metalnessNode :Node.<float>, roughnessNode :Node.<float>, camera :Camera)`
Constructs a new SSR node.

## Import

## Properties
- `.blurQuality :UniformNode.<int>` — The quality of the blur. Must be an integer in the range [1,3] .
- `.camera :Camera` — The camera the scene is rendered with.
- `.colorNode :Node.<vec4>` — The node that represents the beauty pass.
- `.depthNode :Node.<float>` — A node that represents the beauty pass's depth.
- `.maxDistance :UniformNode.<float>` — Controls how far a fragment can reflect. Increasing this value result in more
computational overhead but also increases the reflection distance.
- `.metalnessNode :Node.<float>` — A node that represents the beauty pass's metalness.
- `.normalNode :Node.<vec3>` — A node that represents the beauty pass's normals.
- `.opacity :UniformNode.<float>` — Controls how the SSR reflections are blended with the beauty pass.
- `.quality :UniformNode.<float>` — This parameter controls how detailed the raymarching process works.
The value ranges is [0,1] where 1 means best quality (the maximum number
of raymarching iterations/samples) and 0 means no sample...
- `.resolutionScale : number` — The resolution scale. Valid values are in the range [0,1] . 1 means best quality but also results in
more computational overhead. Setting to 0.5 means
the effect is computed in half-resolution. Def...
- `.thickness :UniformNode.<float>` — Controls the cutoff between what counts as a possible reflection hit and what does not.
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