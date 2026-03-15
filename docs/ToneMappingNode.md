# ToneMappingNode
Extends: EventDispatcher→Node→TempNode→

This node represents a tone mapping operation.

## Constructor
`newToneMappingNode( toneMapping :number, exposureNode :Node, colorNode :Node)`
Constructs a new tone mapping node.

## Properties
- `.colorNode :Node` — Represents the color to process. Default is null .
- `.exposureNode :Node` — The tone mapping exposure. Default is null .

## Methods
- `.customCacheKey() : number` — Overwrites the default customCacheKey() implementation by including the tone
mapping type into the cache key.
- `.getToneMapping() : number` — Gets the tone mapping type.
- `.setToneMapping( value :number) :ToneMappingNode` — Sets the tone mapping type.

## Source