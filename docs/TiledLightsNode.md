# TiledLightsNode
Extends: EventDispatcher→Node→LightsNode→

A custom version of LightsNode implementing tiled lighting. This node is used in TiledLighting to overwrite the renderer's default lighting with
a custom implementation.

## Constructor
`newTiledLightsNode( maxLights :number, tileSize :number)`
Constructs a new tiled lights node.

## Import

## Properties
- `.maxLights : number` — The maximum number of lights. Default is 1024 .
- `.tileSize : number` — The tile size. Default is 32 .

## Source