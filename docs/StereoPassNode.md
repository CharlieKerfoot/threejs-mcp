# StereoPassNode
Extends: EventDispatcher→Node→TempNode→PassNode→

A special render pass node that renders the scene as a stereoscopic image.

## Constructor
`newStereoPassNode( scene :Scene, camera :Camera)`
Constructs a new stereo pass node.

## Import

## Properties
- `.isStereoPassNode : boolean` — This flag can be used for type testing. Default is true .
- `.stereo :StereoCamera` — The internal stereo camera that is used to render the scene.

## Methods
- `.updateBefore( frame :NodeFrame)` — This method is used to render the stereo effect once per frame.

## Source