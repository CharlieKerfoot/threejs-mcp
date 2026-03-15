# GodraysNode
Extends: EventDispatcher→Node→TempNode→

Post-Processing node for apply Screen-space raymarched godrays to a scene. After the godrays have been computed, it's recommened to apply a Bilateral
Blur to the result to mitigate raymarching and noise artifacts. The composite with the scene pass is ideally done with depthAwareBlend() ,
which mitigates aliasing and light leaking. Limitations: Only point and directional lights are currently supported. The effect requires a full shadow setup. Meaning shadows must be enabled in the renderer,
3D objects must cast and receive shadows and the main light must cast shadows. Reference: This Node is a part of three-good-godrays .

## Constructor
`newGodraysNode( depthNode :TextureNode, camera :Camera, light :DirectionalLight|PointLight)`
Constructs a new Godrays node.

## Import

## Properties
- `.density :UniformNode.<float>` — The rate of accumulation for the godrays.  Higher values roughly equate to more humid air/denser fog. Default is 0.7 .
- `.depthNode :TextureNode` — A node that represents the beauty pass's depth.
- `.distanceAttenuation :UniformNode.<float>` — Higher values decrease the accumulation of godrays the further away they are from the light source. Default is 2 .
- `.maxDensity :UniformNode.<float>` — The maximum density of the godrays.  Limits the maximum brightness of the godrays. Default is 0.5 .
- `.raymarchSteps :UniformNode.<uint>` — The number of raymarching steps Default is 60 .
- `.resolutionScale : number` — The resolution scale.
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