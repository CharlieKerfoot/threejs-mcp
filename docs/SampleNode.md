# SampleNode
Extends: EventDispatcher→Node→

Class representing a node that samples a value using a provided callback function.

## Constructor
`newSampleNode( callback :function, uvNode :Node.<vec2>)`
Creates an instance of SampleNode.

## Properties
- `.isSampleNode : boolean` — This flag can be used for type testing. Default is true .
- `.uvNode :Node.<(vec2|vec3)>` — Represents the texture coordinates. Default is null .
- `.type : string` — Returns the type of the node.

## Methods
- `.sample( uv :Node.<vec2>) :Node` — Calls the callback function with the provided UV node.
- `.setup() :Node` — Sets up the node by sampling with the default UV accessor.

## Source