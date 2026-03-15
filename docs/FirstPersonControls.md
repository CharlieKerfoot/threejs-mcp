# FirstPersonControls
Extends: EventDispatcher→Controls→

This class is an alternative implementation of FlyControls .

## Constructor
`newFirstPersonControls( object :Object3D, domElement :HTMLElement)`
Constructs a new controls instance.

## Import

## Properties
- `.activeLook : boolean` — Whether it's possible to look around or not. Default is true .
- `.autoForward : boolean` — Whether the camera is automatically moved forward or not. Default is false .
- `.constrainVertical : boolean` — Whether or not looking around is vertically constrained by verticalMin and verticalMax . Default is false .
- `.heightCoef : number` — Determines how much faster the camera moves when it's y-component is near heightMax . Default is 1 .
- `.heightMax : number` — Upper camera height limit used for movement speed adjustment. Default is 1 .
- `.heightMin : number` — Lower camera height limit used for movement speed adjustment. Default is 0 .
- `.heightSpeed : boolean` — Whether or not the camera's height influences the forward movement speed.
Use the properties heightCoef , heightMin and heightMax for configuration. Default is false .
- `.lookSpeed : number` — The look around speed. Default is 0.005 .
- `.lookVertical : boolean` — Whether it's possible to vertically look around or not. Default is true .
- `.mouseDragOn : boolean` — Whether the mouse is pressed down or not. Default is false .
- `.movementSpeed : number` — The movement speed. Default is 1 .
- `.verticalMax : number` — How far you can vertically look around, upper limit. Range is 0 to Math.PI in radians. Default is 0 .
- `.verticalMin : number` — How far you can vertically look around, lower limit. Range is 0 to Math.PI in radians. Default is 0 .

## Methods
- `.handleResize()` — Must be called if the application window is resized.
- `.lookAt( x :number |Vector3, y :number, z :number) :FirstPersonControls` — Rotates the camera towards the defined target position.

## Source