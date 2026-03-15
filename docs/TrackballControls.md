# TrackballControls
Extends: EventDispatcher→Controls→

This class is similar to OrbitControls . However, it does not maintain a constant camera up vector. That means if the camera orbits over the “north” and “south” poles, it does not flip
to stay "right side up".

## Constructor
`newTrackballControls( object :Object3D, domElement :HTMLElement)`
Constructs a new controls instance.

## Import

## Properties
- `.dynamicDampingFactor : number` — Defines the intensity of damping. Only considered if staticMoving is set to false . Default is 0.2 .
- `.keys : Array.<string>` — This array holds keycodes for controlling interactions. When the first defined key is pressed, all mouse interactions (left, middle, right) performs orbiting. When the second defined key is pressed...
- `.maxDistance : number` — How far you can dolly out (perspective camera only). Default is Infinity .
- `.maxZoom : number` — How far you can zoom out (orthographic camera only). Default is Infinity .
- `.minDistance : number` — How far you can dolly in (perspective camera only). Default is 0 .
- `.minZoom : number` — How far you can zoom in (orthographic camera only). Default is 0 .
- `.mouseButtons : Object` — This object contains references to the mouse actions used by the controls. controls.mouseButtons = {
	LEFT: THREE.MOUSE.ROTATE,
	MIDDLE: THREE.MOUSE.DOLLY,
	RIGHT: THREE.MOUSE.PAN
}
- `.noPan : boolean` — Whether panning is disabled or not. Default is false .
- `.noRotate : boolean` — Whether rotation is disabled or not. Default is false .
- `.noZoom : boolean` — Whether zooming is disabled or not. Default is false .
- `.panSpeed : number` — The pan speed. Default is 0.3 .
- `.rotateSpeed : number` — The rotation speed. Default is 1 .
- `.screen : Object` — Represents the properties of the screen. Automatically set when handleResize() is called.
- `.staticMoving : boolean` — Whether damping is disabled or not. Default is false .
- `.target :Vector3` — The focus point of the controls.
- `.zoomSpeed : number` — The zoom speed. Default is 1.2 .

## Methods
- `.handleResize()` — Must be called if the application window is resized.
- `.reset()` — Resets the controls to its initial state.

## Events
- `.change` — Fires when the camera has been transformed by the controls.
- `.end` — Fires when an interaction has finished.
- `.start` — Fires when an interaction was initiated.

## Source