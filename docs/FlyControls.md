# FlyControls
Extends: EventDispatcher→Controls→

This class enables a navigation similar to fly modes in DCC tools like Blender.
You can arbitrarily transform the camera in 3D space without any limitations
(e.g. focus on a specific target).

## Constructor
`newFlyControls( object :Object3D, domElement :HTMLElement)`
Constructs a new controls instance.

## Import

## Properties
- `.autoForward : boolean` — If set to true , the camera automatically moves forward (and does not stop) when initially translated. Default is false .
- `.dragToLook : boolean` — If set to true , you can only look around by performing a drag interaction. Default is false .
- `.movementSpeed : number` — The movement speed. Default is 1 .
- `.rollSpeed : number` — The rotation speed. Default is 0.005 .

## Events
- `.change` — Fires when the camera has been transformed by the controls.

## Source