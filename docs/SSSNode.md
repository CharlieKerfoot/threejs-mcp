# SSSNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for applying Screen-Space Shadows (SSS) to a scene. Screen-Space Shadows (also known as Contact Shadows) should ideally be used to complement
traditional shadow maps. They are best suited for rendering detailed shadows of smaller
objects at a closer scale like intricate shadowing on highly detailed models. In other words:
Use Shadow Maps for the foundation and Screen-Space Shadows for the details. The shadows produced by this implementation might have too hard edges for certain use cases.
Use a box, gaussian or hash blur to soften the edges before doing the composite with the
beauty pass. Code example: Limitations: Ideally the maximum shadow length should not exceed 1 meter. Otherwise the effect gets
computationally very expensive since more samples during the ray marching process are evaluated.
You can mitigate this issue by reducing the quality paramter. The effect can only be used with a single directional light, the main light of your scene.
This main light usually represents the sun or daylight. Like other Screen-Space techniques SSS can only honor objects in the shadowing computation that
are currently visible within the camera's view. References: https://panoskarabelas.com/posts/screen_space_shadows/ . https://www.bendstudio.com/blog/inside-bend-screen-space-shadows/ .

## Constructor
`newSSSNode( depthNode :TextureNode, camera :Camera, mainLight :DirectionalLight)`
Constructs a new SSS node.

## Import

## Properties
- `.depthNode :TextureNode` — A node that represents the beauty pass's depth.
- `.maxDistance :UniformNode.<float>` — Maximum shadow length in world units. Longer shadows result in more computational
overhead. Default is 0.1 .
- `.quality :UniformNode.<float>` — This parameter controls how detailed the raymarching process works.
The value ranges is [0,1] where 1 means best quality (the maximum number
of raymarching iterations/samples) and 0 means no sample...
- `.resolutionScale : number` — The resolution scale. Valid values are in the range [0,1] . 1 means best quality but also results in
more computational overhead. Setting to 0.5 means
the effect is computed in half-resolution. Def...
- `.shadowIntensity :UniformNode.<float>` — Shadow intensity. Must be in the range [0, 1] . Default is 1.0 .
- `.thickness :UniformNode.<float>` — Depth testing thickness. Default is 0.01 .
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node renders
its effect once per frame in updateBefore() . Default is 'frame' .
- `.useTemporalFiltering : boolean` — Whether to use temporal filtering or not. Setting this property to true requires the usage of TRAANode . This will help to reduce noice
although it introduces typical TAA artifacts like ghosting an...

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.getTextureNode() :PassTextureNode` — Returns the result of the effect as a texture node.
- `.setSize( width :number, height :number)` — Sets the size of the effect.
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the effect once per frame.

## Source