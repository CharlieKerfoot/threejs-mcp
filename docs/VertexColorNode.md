# VertexColorNode
Extends: EventDispatcher→Node→AttributeNode→

An attribute node for representing vertex colors.

## Constructor
`newVertexColorNode( index :number)`
Constructs a new vertex color node.

## Properties
- `.index : number` — The attribute index to enable more than one sets of vertex colors. Default is 0 .
- `.isVertexColorNode : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.getAttributeName( builder :NodeBuilder) : string` — Overwrites the default implementation by honoring the attribute index.

## Source