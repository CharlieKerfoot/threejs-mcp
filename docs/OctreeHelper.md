# OctreeHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

A helper for visualizing an Octree.

## Constructor
`newOctreeHelper( octree :Octree, color :number |Color| string)`
Constructs a new Octree helper.

## Import

## Properties
- `.color : number |Color| string` — The helper's color.
- `.octree :Octree` — The octree to visualize.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the helper. This method must be called whenever the Octree's
structure is changed.

## Source