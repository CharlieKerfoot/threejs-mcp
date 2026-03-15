# DragControls
Extends: EventDispatcher→Controls→

This class can be used to provide a drag'n'drop interaction.

## Constructor
`newDragControls( objects :Array.<Object3D>, camera :Camera, domElement :HTMLElement)`
Constructs a new controls instance.

## Import

## Properties
- `.objects : Array.<Object3D>` — An array of draggable 3D objects.
- `.raycaster :Raycaster` — The raycaster used for detecting 3D objects.
- `.recursive : boolean` — Whether children of draggable objects can be dragged independently from their parent. Default is true .
- `.rotateSpeed : number` — The speed at which the object will rotate when dragged in rotate mode.
The higher the number the faster the rotation. Default is 1 .
- `.transformGroup : boolean` — This option only works if the objects array contains a single draggable  group object.
If set to true , the controls does not transform individual objects but the entire group. Default is false .

## Events
- `.drag` — Fires when the user drags a 3D object.
- `.dragend` — Fires when the user has finished dragging a 3D object.
- `.hoveroff` — Fires when the pointer is moved out of a 3D object.
- `.hoveron` — Fires when the pointer is moved onto a 3D object, or onto one of its children.

## Source