# TileShadowNode
Extends: EventDispatcher→Node→ShadowBaseNode→

A class that extends ShadowBaseNode to implement tiled shadow mapping.
This allows splitting a shadow map into multiple tiles, each with its own light and camera,
to improve shadow quality and performance for large scenes. Note: This class does not support VSMShadowMap at the moment.

## Constructor
`newTileShadowNode( light :Light, options :Object)`
Creates an instance of TileShadowNode .

## Import

## Methods
- `.disposeLightsAndNodes()` — Helper method to remove lights and associated nodes/targets.
Used internally during dispose and potential re-initialization.
- `.generateTiles( tilesX :number, tilesY :number) : Array.<Object>` — Generates the tiles for the shadow map based on the specified number of tiles along the X and Y axes.
- `.init( builder :Builder)` — Initializes the tiled shadow node by creating lights, cameras, and shadow maps for each tile.
- `.setup( builder :Builder) :Node` — Sets up the shadow node for rendering.
- `.syncLightTransformation( lwLight :LwLight, sourceLight :Light)` — Synchronizes the transformation of a tile light with the source light.
- `.update()` — Updates the light transformations and shadow cameras for each tile.
- `.updateBefore( frame :NodeFrame)` — The implementation performs the update of the shadow map if necessary.
- `.updateLightDirection()` — Updates the initial light direction based on the light's target position.
- `.updateShadow( frame :NodeFrame)` — Updates the shadow map rendering.

## Source