# StereoCompositePassNode
Extends: EventDispatcher→Node→TempNode→PassNode→

A special (abstract) render pass node that renders the scene
as a stereoscopic image. Unlike StereoPassNode , this
node merges the image for the left and right eye
into a single one. That is required for effects like
anaglyph or parallax barrier.

## Constructor
`newStereoCompositePassNode( scene :Scene, camera :Camera)(abstract)`
Constructs a new stereo composite pass node.

## Import

## Properties
- `.isStereoCompositePassNode : boolean` — This flag can be used for type testing. Default is true .
- `.stereo :StereoCamera` — The internal stereo camera that is used to render the scene.

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the pass is no longer required.
- `.setSize( width :number, height :number)` — Sets the size of the pass.
- `.updateBefore( frame :NodeFrame)` — This method is used to render the effect once per frame.
- `.updateStereoCamera( coordinateSystem :number)` — Updates the internal stereo camera.

## Source