# Sprite
Extends: EventDispatcher→Object3D→

A sprite is a plane that always faces towards the camera, generally with a
partially transparent texture applied. Sprites do not cast shadows, setting Object3D#castShadow to true will
have no effect.

## Constructor
`newSprite( material :SpriteMaterial|SpriteNodeMaterial)`
Constructs a new sprite.

## Properties
- `.center :Vector2` — The sprite's anchor point, and the point around which the sprite rotates.
A value of (0.5, 0.5) corresponds to the midpoint of the sprite. A value
of (0, 0) corresponds to the lower left corner of ...
- `.count : number` — The number of instances of this sprite.
Can only be used with WebGPURenderer . Default is 1 .
- `.geometry :BufferGeometry` — The sprite geometry.
- `.isSprite : boolean` — This flag can be used for type testing. Default is true .
- `.material :SpriteMaterial|SpriteNodeMaterial` — The sprite material.

## Methods
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>)` — Computes intersection points between a casted ray and this sprite.

## Source