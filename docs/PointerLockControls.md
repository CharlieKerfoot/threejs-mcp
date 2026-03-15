# PointerLockControls
Extends: EventDispatcher→Controls→

The implementation of this class is based on the Pointer Lock API . PointerLockControls is a perfect choice for first person 3D games.

## Constructor
`newPointerLockControls( camera :Camera, domElement :HTMLElement)`
Constructs a new controls instance.

## Import

## Properties
- `.isLocked : boolean` — Whether the controls are locked or not. Default is false .
- `.maxPolarAngle : number` — Camera pitch, upper limit. Range is '[0, Math.PI]' in radians. Default is Math.PI .
- `.minPolarAngle : number` — Camera pitch, lower limit. Range is '[0, Math.PI]' in radians. Default is 0 .
- `.pointerSpeed : number` — Multiplier for how much the pointer movement influences the camera rotation. Default is 1 .

## Methods
- `.getDirection( v :Vector3) :Vector3` — Returns the look direction of the camera.
- `.lock( unadjustedMovement :boolean)` — Activates the pointer lock.
- `.moveForward( distance :number)` — Moves the camera forward parallel to the xz-plane. Assumes camera.up is y-up.
- `.moveRight( distance :number)` — Moves the camera sidewards parallel to the xz-plane.
- `.unlock()` — Exits the pointer lock.

## Events
- `.change` — Fires when the user moves the mouse.
- `.lock` — Fires when the pointer lock status is "locked" (in other words: the mouse is captured).
- `.unlock` — Fires when the pointer lock status is "unlocked" (in other words: the mouse is not captured anymore).

## Source