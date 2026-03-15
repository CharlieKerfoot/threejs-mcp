# FilmNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating a film grain effect.

## Constructor
`newFilmNode( inputNode :Node, intensityNode :Node.<float>, uvNode :Node.<vec2>)`
Constructs a new film node.

## Import

## Properties
- `.inputNode :Node` — The node that represents the input of the effect.
- `.intensityNode :Node.<float>` — A node that represents the effect's intensity. Default is null .
- `.uvNode :Node.<vec2>` — A node that allows to pass custom (e.g. animated) uv data. Default is null .

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.

## Source