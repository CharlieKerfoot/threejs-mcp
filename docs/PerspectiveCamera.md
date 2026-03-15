# PerspectiveCamera
Extends: EventDispatcher→Object3D→Camera→

Camera that uses perspective projection . This projection mode is designed to mimic the way the human eye sees. It
is the most common projection mode used for rendering a 3D scene.

## Constructor
`newPerspectiveCamera( fov :number, aspect :number, near :number, far :number)`
Constructs a new perspective camera.

## Properties
- `.aspect : number` — The aspect ratio, usually the canvas width / canvas height. Default is 1 .
- `.far : number` — The camera's far plane. Must be greater than the
current value of PerspectiveCamera#near . Default is 2000 .
- `.filmGauge : number` — Film size used for the larger axis. Default is 35 (millimeters). This
parameter does not influence the projection matrix unless PerspectiveCamera#filmOffset is set to a nonzero value. Default is 35 .
- `.filmOffset : number` — Horizontal off-center offset in the same unit as PerspectiveCamera#filmGauge . Default is 0 .
- `.focus : number` — Object distance used for stereoscopy and depth-of-field effects. This
parameter does not influence the projection matrix unless a StereoCamera is being used. Default is 10 .
- `.fov : number` — The vertical field of view, from bottom to top of view,
in degrees. Default is 50 .
- `.isPerspectiveCamera : boolean` — This flag can be used for type testing. Default is true .
- `.near : number` — The camera's near plane. The valid range is greater than 0 and less than the current value of PerspectiveCamera#far . Note that, unlike for the OrthographicCamera , 0 is not a
valid value for a per...
- `.view : Object` — Represents the frustum window specification. This property should not be edited
directly but via PerspectiveCamera#setViewOffset and PerspectiveCamera#clearViewOffset . Default is null .
- `.zoom : number` — The zoom factor of the camera. Default is 1 .

## Methods
- `.clearViewOffset()` — Removes the view offset from the projection matrix.
- `.getEffectiveFOV() : number` — Returns the current vertical field of view angle in degrees considering PerspectiveCamera#zoom .
- `.getFilmHeight() : number` — Returns the height of the image on the film. If PerspectiveCamera#aspect is greater than or
equal to one (landscape format), the result equals PerspectiveCamera#filmGauge .
- `.getFilmWidth() : number` — Returns the width of the image on the film. If PerspectiveCamera#aspect is greater than or
equal to one (landscape format), the result equals PerspectiveCamera#filmGauge .
- `.getFocalLength() : number` — Returns the focal length from the current PerspectiveCamera#fov and PerspectiveCamera#filmGauge .
- `.getViewBounds( distance :number, minTarget :Vector2, maxTarget :Vector2)` — Computes the 2D bounds of the camera's viewable rectangle at a given distance along the viewing direction.
Sets minTarget and maxTarget to the coordinates of the lower-left and upper-right corners ...
- `.getViewSize( distance :number, target :Vector2) :Vector2` — Computes the width and height of the camera's viewable rectangle at a given distance along the viewing direction.
- `.setFocalLength( focalLength :number)` — Sets the FOV by focal length in respect to the current PerspectiveCamera#filmGauge . The default film gauge is 35, so that the focal length can be specified for
a 35mm (full frame) camera.
- `.setViewOffset( fullWidth :number, fullHeight :number, x :number, y :number, width :number, height :number)` — Sets an offset in a larger frustum. This is useful for multi-window or
multi-monitor/multi-machine setups. For example, if you have 3x2 monitors and each monitor is 1920x1080 and
the monitors are i...
- `.updateProjectionMatrix()` — Updates the camera's projection matrix. Must be called after any change of
camera properties.

## Source