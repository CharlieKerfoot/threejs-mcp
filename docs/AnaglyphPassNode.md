# AnaglyphPassNode
Extends: EventDispatcher→Node→TempNode→PassNode→StereoCompositePassNode→

A render pass node that creates an anaglyph effect using physically-correct
off-axis stereo projection. This implementation uses CameraUtils.frameCorners() to align stereo
camera frustums to a virtual screen plane, providing accurate depth
perception with zero parallax at the plane distance.

## Constructor
`newAnaglyphPassNode( scene :Scene, camera :Camera)`
Constructs a new anaglyph pass node.

## Import

## Properties
- `.algorithm : string` — Gets the current anaglyph algorithm.
- `.algorithm : string` — Sets the anaglyph algorithm.
- `.colorMode : string` — Gets the current color mode.
- `.colorMode : string` — Sets the color mode.
- `.eyeSep : number` — The interpupillary distance (eye separation) in world units.
Typical human IPD is 0.064 meters (64mm). Default is 0.064 .
- `.isAnaglyphPassNode : boolean` — This flag can be used for type testing. Default is true .
- `.planeDistance : number` — The distance in world units from the viewer to the virtual
screen plane where zero parallax (screen depth) occurs.
Objects at this distance appear at the screen surface.
Objects closer appear in fr...

## Methods
- `.setup( builder :NodeBuilder) :PassTextureNode` — This method is used to setup the effect's TSL code.
- `.updateStereoCamera( coordinateSystem :number)` — Updates the internal stereo camera using frameCorners for
physically-correct off-axis projection.

## Source