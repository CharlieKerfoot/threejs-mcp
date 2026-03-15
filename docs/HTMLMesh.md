# HTMLMesh
Extends: EventDispatcher→Object3D→Mesh→

This class can be used to render a DOM element onto a canvas and use it as a texture
for a plane mesh. A typical use case for this class is to render the GUI of lil-gui as a texture so it
is compatible for VR.

## Constructor
`newHTMLMesh( dom :HTMLElement)`
Constructs a new HTML mesh.

## Import

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance and removes all event listeners.
Call this method whenever this instance is no longer used in your app.

## Source