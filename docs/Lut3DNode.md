# Lut3DNode
Extends: EventDispatcher→Node→TempNode→

A post processing node for color grading via lookup tables.

## Constructor
`newLut3DNode( inputNode :Node, lutNode :TextureNode, size :number, intensityNode :Node.<float>)`
Constructs a new LUT node.

## Import

## Properties
- `.inputNode :Node` — The node that represents the input of the effect.
- `.intensityNode :Node.<float>` — Controls the intensity of the effect.
- `.lutNode :TextureNode` — A texture node that represents the lookup table.
- `.size :UniformNode.<float>` — The size of the lookup table.

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.

## Source