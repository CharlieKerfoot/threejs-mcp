# BloomNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating a bloom effect. By default, the node affects the entire image. For a selective bloom,
use the emissive material property to control which objects should
contribute to bloom or not. This can be achieved via MRT. const renderPipeline = new THREE.RenderPipeline( renderer );
const scenePass = pass( scene, camera );
scenePass.setMRT( mrt( {
	output,
	emissive
} ) );
const scenePassColor = scenePass.getTextureNode( 'output' );
const emissivePass = scenePass.getTextureNode( 'emissive' );
const bloomPass = bloom( emissivePass );
renderPipeline.outputNode = scenePassColor.add( bloomPass );

## Constructor
`newBloomNode( inputNode :Node.<vec4>, strength :number, radius :number, threshold :number)`
Constructs a new bloom node.

## Import

## Properties
- `.inputNode :Node.<vec4>` — The node that represents the input of the effect.
- `.radius :UniformNode.<float>` — The radius of the bloom. Must be in the range [0,1] .
- `.smoothWidth :UniformNode.<float>` — Can be used to tweak the extracted luminance from the scene.
- `.strength :UniformNode.<float>` — The strength of the bloom.
- `.threshold :UniformNode.<float>` — The luminance threshold limits which bright areas contribute to the bloom effect.
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