# Projector

This class can project a given scene in 3D space into a 2D representation
used for rendering with a 2D API. Projector is currently used by SVGRenderer and was previously used by the legacy CanvasRenderer .

## Constructor
`newProjector()`
Constructs a new projector.

## Import

## Methods
- `.projectScene( scene :Object3D, camera :Camera, sortObjects :boolean, sortElements :boolean) : Object` — Projects the given scene in 3D space into a 2D representation. The result
is an object with renderable items.

## Source