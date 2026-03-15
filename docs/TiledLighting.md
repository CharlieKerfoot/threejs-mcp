# TiledLighting
Extends: Lighting→

A custom lighting implementation based on Tiled-Lighting that overwrites the default
implementation in WebGPURenderer .

## Constructor
`newTiledLighting()`
Constructs a new lighting system.

## Import

## Classes

## Methods
- `.createNode( lights :Array.<Light>) :TiledLightsNode` — Creates a new tiled lights node for the given array of lights. This method is called internally by the renderer and must be overwritten by
all custom lighting implementations.

## Source