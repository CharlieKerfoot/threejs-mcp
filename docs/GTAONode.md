# GTAONode
Extends: EventDispatcher→Node→TempNode→

Post processing node for applying Ground Truth Ambient Occlusion (GTAO) to a scene. Reference: Practical Real-Time Strategies for Accurate Indirect Occlusion .

## Constructor
`newGTAONode( depthNode :Node.<float>, normalNode :Node.<vec3>, camera :Camera)`
Constructs a new GTAO node.

## Import

## Properties
- `.depthNode :Node.<float>` — A node that represents the scene's depth.
- `.distanceExponent :UniformNode.<float>` — Another option to tweak the occlusion. The recommended range is [1,2] for attenuating the AO.
- `.distanceFallOff :UniformNode.<float>` — The distance fall off value of the ambient occlusion.
A lower value leads to a larger AO effect. The value
should lie in the range [0,1] .
- `.normalNode :Node.<vec3>` — A node that represents the scene's normals. If no normals are passed to the
constructor (because MRT is not available), normals can be automatically
reconstructed from depth values in the shader.
- `.radius :UniformNode.<float>` — The radius of the ambient occlusion.
- `.resolution :UniformNode.<vec2>` — The resolution of the effect. Can be scaled via resolutionScale .
- `.resolutionScale : number` — The resolution scale. By default the effect is rendered in full resolution
for best quality but a value of 0.5 should be sufficient for most scenes. Default is 1 .
- `.samples :UniformNode.<float>` — How many samples are used to compute the AO.
A higher value results in better quality but also
in a more expensive runtime behavior.
- `.scale :UniformNode.<float>` — The scale of the ambient occlusion.
- `.thickness :UniformNode.<float>` — The thickness of the ambient occlusion.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node renders
its effect once per frame in updateBefore() . Default is 'frame' .
- `.useTemporalFiltering : boolean` — Whether to use temporal filtering or not. Setting this property to true requires the usage of TRAANode . This will help to reduce noise
although it introduces typical TAA artifacts like ghosting an...

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.getTextureNode() :PassTextureNode` — Returns the result of the effect as a texture node.
- `.setSize( width :number, height :number)` — Sets the size of the effect.
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the effect once per frame.

## Source