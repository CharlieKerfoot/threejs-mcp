# TileShadowNodeHelper
Extends: EventDispatcher→Object3D→Group→

Helper class to manage and display debug visuals for TileShadowNode.

## Constructor
`newTileShadowNodeHelper( tileShadowNode :TileShadowNode)`

## Import

## Methods
- `.dispose()` — Removes all debug objects (planes and helpers) from the scene.
- `.init()` — Initializes the debug displays (planes and camera helpers).
Should be called after TileShadowNode has initialized its lights and shadow nodes.
- `.update()` — Updates the debug visuals (specifically camera helpers).
Should be called within TileShadowNode's update method.

## Source