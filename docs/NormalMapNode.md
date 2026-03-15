# NormalMapNode
Extends: EventDispatcher→Node→TempNode→

This class can be used for applying normals maps to materials.

## Constructor
`newNormalMapNode( node :Node.<vec3>, scaleNode :Node.<vec2>)`
Constructs a new normal map node.

## Properties
- `.node :Node.<vec3>` — Represents the normal map data.
- `.normalMapType :TangentSpaceNormalMap|ObjectSpaceNormalMap` — The normal map type. Default is TangentSpaceNormalMap .
- `.scaleNode :Node.<vec2>` — Controls the intensity of the effect. Default is null .
- `.unpackNormalMode : string` — Controls how to unpack the sampled normal map values. Default is NoNormalPacking .

## Source