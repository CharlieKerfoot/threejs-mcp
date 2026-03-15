# InteractiveGroup
Extends: EventDispatcher→Object3D→Group→

This class can be used to group 3D objects in an interactive group.
The group itself can listen to Pointer, Mouse or XR controller events to
detect selections of descendant 3D objects. If a 3D object is selected,
the respective event is going to dispatched to it.

## Constructor
`newInteractiveGroup()`

## Import

## Properties
- `.camera :Camera` — The camera used for raycasting. Default is null .
- `.controllers : Array.<Group>` — An array of XR controllers.
- `.element : HTMLElement` — The internal raycaster. Default is null .
- `.raycaster :Raycaster` — The internal raycaster.

## Methods
- `.disconnect()` — Disconnects this interactive group from the DOM and all XR controllers.
- `.disconnectXrControllerEvents()` — Disconnects this interactive group from all XR controllers.
- `.disconnectionPointerEvents()` — Disconnects this interactive group from all Pointer and Mouse Events.
- `.listenToPointerEvents( renderer :WebGPURenderer|WebGLRenderer, camera :Camera)` — Calling this method makes sure the interactive group listens to Pointer and Mouse events.
The target is the domElement of the given renderer. The camera is required for the internal
raycasting so 3...
- `.listenToXRControllerEvents( controller :Group)` — Calling this method makes sure the interactive group listens to events of
the given XR controller.

## Source