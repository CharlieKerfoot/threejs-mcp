# OrthographicCamera
Extends: EventDispatcher→Object3D→Camera→

Camera that uses orthographic projection . In this projection mode, an object's size in the rendered image stays
constant regardless of its distance from the camera. This can be useful
for rendering 2D scenes and UI elements, amongst other things.

## Constructor
`newOrthographicCamera( left :number, right :number, top :number, bottom :number, near :number, far :number)`
Constructs a new orthographic camera.

## Properties
- `.bottom : number` — The bottom plane of the camera's frustum. Default is -1 .
- `.far : number` — The camera's far plane. Must be greater than the
current value of OrthographicCamera#near . Default is 2000 .
- `.isOrthographicCamera : boolean` — This flag can be used for type testing. Default is true .
- `.left : number` — The left plane of the camera's frustum. Default is -1 .
- `.near : number` — The camera's near plane. The valid range is greater than 0 and less than the current value of OrthographicCamera#far . Note that, unlike for the PerspectiveCamera , 0 is a
valid value for an orthog...
- `.right : number` — The right plane of the camera's frustum. Default is 1 .
- `.top : number` — The top plane of the camera's frustum. Default is 1 .
- `.view : Object` — Represents the frustum window specification. This property should not be edited
directly but via PerspectiveCamera#setViewOffset and PerspectiveCamera#clearViewOffset . Default is null .
- `.zoom : number` — The zoom factor of the camera. Default is 1 .

## Methods
- `.clearViewOffset()` — Removes the view offset from the projection matrix.
- `.setViewOffset( fullWidth :number, fullHeight :number, x :number, y :number, width :number, height :number)` — Sets an offset in a larger frustum. This is useful for multi-window or
multi-monitor/multi-machine setups.
- `.updateProjectionMatrix()` — Updates the camera's projection matrix. Must be called after any change of
camera properties.

## Source