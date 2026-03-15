# DotScreenNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating dot-screen effect.

## Constructor
`newDotScreenNode( inputNode :Node, angle :number, scale :number)`
Constructs a new dot screen node.

## Import

## Properties
- `.angle :UniformNode.<float>` — A uniform node that represents the rotation of the effect in radians.
- `.inputNode :Node` — The node that represents the input of the effect.
- `.scale :UniformNode.<float>` — A uniform node that represents the scale of the effect. A higher value means smaller dots.

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.

## Source