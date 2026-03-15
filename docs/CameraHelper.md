# CameraHelper
Extends: EventDispatcher→Object3D→Line→LineSegments→

This helps with visualizing what a camera contains in its frustum. It
visualizes the frustum of a camera using a line segments. Based on frustum visualization in lightgl.js shadowmap example . CameraHelper must be a child of the scene. When the camera is transformed or its projection matrix is changed, it's necessary
to call the update() method of the respective helper.

## Constructor
`newCameraHelper( camera :Camera)`
Constructs a new arrow helper.

## Properties
- `.camera :Camera` — The camera being visualized.
- `.pointMap : Object.<string, Array.<number>>` — This contains the points used to visualize the camera.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setColors( frustum :Color, cone :Color, up :Color, target :Color, cross :Color) :CameraHelper` — Defines the colors of the helper.
- `.update()` — Updates the helper based on the projection matrix of the camera.

## Source