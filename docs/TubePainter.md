# TubePainter

This module can be used to paint tube-like meshes
along a sequence of points. This module is used in a XR
painter demo.

## Constructor
`newTubePainter()`

## Import

## Properties
- `.mesh :Mesh` — The "painted" tube mesh. Must be added to the scene.

## Methods
- `.lineTo( position :Vector3)` — Draw a stroke from the current position to the given one.
This method extends the tube while drawing with the XR
controllers.
- `.moveTo( position :Vector3)` — Moves the current painting position to the given value.
- `.setColor( color :Color)` — Sets the color of newly rendered tube segments.
- `.setSize( size :number)` — Sets the size of newly rendered tube segments.
- `.update()` — Updates the internal geometry buffers so the new painted
segments are rendered.

## Source