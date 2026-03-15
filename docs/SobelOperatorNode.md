# SobelOperatorNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for detecting edges with a sobel filter.
A sobel filter should be applied after tone mapping and output color
space conversion.

## Constructor
`newSobelOperatorNode( textureNode :TextureNode)`
Constructs a new sobel operator node.

## Import

## Properties
- `.textureNode :TextureNode` — The texture node that represents the input of the effect.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node updates
its internal uniforms once per frame in updateBefore() . Default is 'frame' .

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to update the effect's uniforms once per frame.

## Source