# RapierHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

This class displays all Rapier Colliders in outline.

## Constructor
`newRapierHelper( world :RAPIER.world)`
Constructs a new Rapier debug helper.

## Import

## Properties
- `.world : RAPIER.world` — The Rapier world to visualize.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Call this in the render loop to update the outlines.

## Source