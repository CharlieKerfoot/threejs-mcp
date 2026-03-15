# RGBShiftNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for shifting/splitting RGB color channels. The effect
separates color channels and offsets them from each other.

## Constructor
`newRGBShiftNode( textureNode :TextureNode, amount :number, angle :number)`
Constructs a new RGB shift node.

## Import

## Properties
- `.amount :UniformNode.<float>` — The amount of the RGB shift.
- `.angle :UniformNode.<float>` — Defines in which direction colors are shifted.
- `.textureNode :TextureNode` — The texture node that represents the input of the effect.

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.

## Source