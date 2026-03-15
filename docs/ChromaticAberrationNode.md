# ChromaticAberrationNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for applying chromatic aberration effect.
This effect simulates the color fringing that occurs in real camera lenses
by separating and offsetting the red, green, and blue channels.

## Constructor
`newChromaticAberrationNode( textureNode :TextureNode, strengthNode :Node, centerNode :Node, scaleNode :Node)`
Constructs a new chromatic aberration node.

## Import

## Properties
- `.centerNode :Node` — A node holding the center point of the effect.
- `.scaleNode :Node` — A node holding the scale factor for stepped scaling.
- `.strengthNode :Node` — A node holding the strength of the effect.
- `.textureNode :texture` — The texture node that represents the input of the effect.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node updates
its internal uniforms once per frame in updateBefore() . Default is 'frame' .

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.
- `.updateBefore( frame :NodeFrame)` — This method is used to update the effect's uniforms once per frame.

## Source