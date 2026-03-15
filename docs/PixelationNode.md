# PixelationNode
Extends: EventDispatcher→Node→TempNode→

A inner node definition that implements the actual pixelation TSL code.

## Constructor
`newPixelationNode( textureNode :TextureNode, depthNode :TextureNode, normalNode :TextureNode, pixelSize :Node.<float>, normalEdgeStrength :Node.<float>, depthEdgeStrength :Node.<float>)`
Constructs a new pixelation node.

## Properties
- `.depthEdgeStrength :Node.<float>` — The depth edge strength.
- `.depthNode :TextureNode` — The texture that represents the beauty's depth.
- `.normalEdgeStrength :Node.<float>` — The pixel size.
- `.normalNode :TextureNode` — The texture that represents the beauty's normals.
- `.pixelSize :Node.<float>` — The pixel size.
- `.textureNode :TextureNode` — The texture node that represents the beauty pass.
- `.updateType : string` — The updateType is set to NodeUpdateType.FRAME since the node updates
its internal uniforms once per frame in updateBefore() . Default is 'frame' .

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.
- `.update( frame :NodeFrame)` — This method is used to update uniforms once per frame.

## Source