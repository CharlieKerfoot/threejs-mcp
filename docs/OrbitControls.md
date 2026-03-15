# OrbitControls
Extends: EventDispatcher→Controls→

Orbit controls allow the camera to orbit around a target. OrbitControls performs orbiting, dollying (zooming), and panning. Unlike TrackballControls ,
it maintains the "up" direction object.up (+Y by default). Orbit: Left mouse / touch: one-finger move. Zoom: Middle mouse, or mousewheel / touch: two-finger spread or squish. Pan: Right mouse, or left mouse + ctrl/meta/shiftKey, or arrow keys / touch: two-finger move.

## Constructor
`newOrbitControls( object :Object3D, domElement :HTMLElement)`
Constructs a new controls instance.

## Import

## Properties
- `.autoRotate : boolean` — Set to true to automatically rotate around the target Note that if this is enabled, you must call update() in your animation loop.
If you want the auto-rotate speed to be independent of the frame r...
- `.autoRotateSpeed : number` — How fast to rotate around the target if autoRotate is true . The default  equates to 30 seconds
per orbit at 60fps. Note that if autoRotate is enabled, you must call update() in your animation loop...
- `.cursor :Vector3` — The focus point of the minTargetRadius and maxTargetRadius limits.
It can be updated manually at any point to change the center of interest
for the target .
- `.cursorStyle : 'auto' | 'grab'` — Defines the visual representation of the cursor. Default is 'auto' .
- `.dampingFactor : number` — The damping inertia used if enableDamping is set to true . Note that for this to work, you must call update() in your animation loop. Default is 0.05 .
- `.enableDamping : boolean` — Set to true to enable damping (inertia), which can be used to give a sense of weight
to the controls. Note that if this is enabled, you must call update() in your animation
loop. Default is false .
- `.enablePan : boolean` — Enable or disable camera panning. Default is true .
- `.enableRotate : boolean` — Enable or disable horizontal and vertical rotation of the camera. Note that it is possible to disable a single axis by setting the min and max of the minPolarAngle or minAzimuthAngle to the same va...
- `.enableZoom : boolean` — Enable or disable zooming (dollying) of the camera. Default is true .
- `.keyPanSpeed : number` — How fast to pan the camera when the keyboard is used in
pixels per keypress. Default is 7 .
- `.keyRotateSpeed : number` — How fast to rotate the camera when the keyboard is used. Default is 1 .
- `.keys : Object` — This object contains references to the keycodes for controlling camera panning. controls.keys = {
	LEFT: 'ArrowLeft', //left arrow
	UP: 'ArrowUp', // up arrow
	RIGHT: 'ArrowRight', // right arrow
	...
- `.maxAzimuthAngle : number` — How far you can orbit horizontally, upper limit. If set, the interval [ min, max ] must be a sub-interval of [ - 2 PI, 2 PI ] , with ( max - min < 2 PI ) . Default is -Infinity .
- `.maxDistance : number` — How far you can dolly out (perspective camera only). Default is Infinity .
- `.maxPolarAngle : number` — How far you can orbit vertically, upper limit. Range is [0, Math.PI] radians. Default is Math.PI .
- `.maxTargetRadius : number` — How far you can move the target from the 3D cursor . Default is Infinity .
- `.maxZoom : number` — How far you can zoom out (orthographic camera only). Default is Infinity .
- `.minAzimuthAngle : number` — How far you can orbit horizontally, lower limit. If set, the interval [ min, max ] must be a sub-interval of [ - 2 PI, 2 PI ] , with ( max - min < 2 PI ) . Default is -Infinity .
- `.minDistance : number` — How far you can dolly in (perspective camera only). Default is 0 .
- `.minPolarAngle : number` — How far you can orbit vertically, lower limit. Range is [0, Math.PI] radians. Default is 0 .
- `.minTargetRadius : number` — How close you can get the target to the 3D cursor . Default is 0 .
- `.minZoom : number` — How far you can zoom in (orthographic camera only). Default is 0 .
- `.mouseButtons : Object` — This object contains references to the mouse actions used by the controls. controls.mouseButtons = {
	LEFT: THREE.MOUSE.ROTATE,
	MIDDLE: THREE.MOUSE.DOLLY,
	RIGHT: THREE.MOUSE.PAN
}
- `.panSpeed : number` — Speed of panning. Default is 1 .
- `.position0 :Vector3` — Used internally by saveState() and reset() .
- `.rotateSpeed : number` — Speed of rotation. Default is 1 .
- `.screenSpacePanning : boolean` — Defines how the camera's position is translated when panning. If true , the camera pans
in screen space. Otherwise, the camera pans in the plane orthogonal to the camera's up
direction. Default is ...
- `.target :Vector3` — The focus point of the controls, the object orbits around this.
It can be updated manually at any point to change the focus of the controls.
- `.target0 :Vector3` — Used internally by saveState() and reset() .
- `.touches : Object` — This object contains references to the touch actions used by the controls. controls.mouseButtons = {
	ONE: THREE.TOUCH.ROTATE,
	TWO: THREE.TOUCH.DOLLY_PAN
}
- `.zoom0 : number` — Used internally by saveState() and reset() .
- `.zoomSpeed : number` — Speed of zooming / dollying. Default is 1 .
- `.zoomToCursor : boolean` — Setting this property to true allows to zoom to the cursor's position. Default is false .

## Methods
- `.dollyIn( dollyScale :number)` — Programmatically dolly in (zoom in for perspective camera).
- `.dollyOut( dollyScale :number)` — Programmatically dolly out (zoom out for perspective camera).
- `.getAzimuthalAngle() : number` — Get the current horizontal rotation, in radians.
- `.getDistance() : number` — Returns the distance from the camera to the target.
- `.getPolarAngle() : number` — Get the current vertical rotation, in radians.
- `.listenToKeyEvents( domElement :HTMLElement)` — Adds key event listeners to the given DOM element. window is a recommended argument for using this method.
- `.pan( deltaX :number, deltaY :number)` — Programmatically pan the camera.
- `.reset()` — Reset the controls to their state from either the last time the saveState() was called, or the initial state.
- `.rotateLeft( angle :number)` — Programmatically rotate the camera left (around the vertical axis).
- `.rotateUp( angle :number)` — Programmatically rotate the camera up (around the horizontal axis).
- `.saveState()` — Save the current state of the controls. This can later be recovered with reset() .
- `.stopListenToKeyEvents()` — Removes the key event listener previously defined with listenToKeyEvents() .

## Events
- `.change` — Fires when the camera has been transformed by the controls.
- `.end` — Fires when an interaction has finished.
- `.start` — Fires when an interaction was initiated.

## Source