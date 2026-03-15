# BumpMapNode
Extends: EventDispatcher→Node→TempNode→

This class can be used for applying bump maps to materials.

## Constructor
`newBumpMapNode( textureNode :Node.<float>, scaleNode :Node.<float>)`
Constructs a new bump map node.

## Properties
- `.scaleNode :Node.<float>` — Controls the intensity of the bump effect. Default is null .
- `.textureNode :Node.<float>` — Represents the bump map data.

## Source