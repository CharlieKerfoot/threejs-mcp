# MapControls
Extends: EventDispatcher→Controls→OrbitControls→

This class is intended for transforming a camera over a map from bird's eye perspective.
The class shares its implementation with OrbitControls but uses a specific preset
for mouse/touch interaction and disables screen space panning by default. Orbit: Right mouse, or left mouse + ctrl/meta/shiftKey / touch: two-finger rotate. Zoom: Middle mouse, or mousewheel / touch: two-finger spread or squish. Pan: Left mouse, or arrow keys / touch: one-finger move.

## Constructor
`newMapControls()`

## Import

## Properties
- `.mouseButtons : Object` — This object contains references to the mouse actions used by the controls. controls.mouseButtons = {
	LEFT: THREE.MOUSE.PAN,
	MIDDLE: THREE.MOUSE.DOLLY,
	RIGHT: THREE.MOUSE.ROTATE
}
- `.screenSpacePanning : boolean` — Overwritten and set to false to pan orthogonal to world-space direction camera.up . Default is false .
- `.touches : Object` — This object contains references to the touch actions used by the controls. controls.mouseButtons = {
	ONE: THREE.TOUCH.PAN,
	TWO: THREE.TOUCH.DOLLY_ROTATE
}

## Source