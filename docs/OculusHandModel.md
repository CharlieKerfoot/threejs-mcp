# OculusHandModel
Extends: EventDispatcher→Object3D→

Represents an Oculus hand model.

## Constructor
`newOculusHandModel( controller :Group, loader :Loader, onLoad :function)`
Constructs a new Oculus hand model.

## Import

## Properties
- `.controller :Group` — The hand controller.
- `.envMap :Texture` — The model's environment map. Default is null .
- `.loader :Loader` — A loader that is used to load hand models. Default is null .
- `.mesh :Mesh` — The model mesh. Default is null .
- `.motionController : MotionController` — The motion controller. Default is null .
- `.onLoad : function` — A callback that is executed when a hand model has been loaded. Default is null .
- `.path : string` — The path to the model repository. Default is null .

## Methods
- `.checkButton( button :Object)` — Executed actions depending on the interaction state with
the given button.
- `.getPointerPosition() :Vector3` — Returns the pointer position which is the position of the index finger tip.
- `.intersectBoxObject( boxObject :Mesh) : boolean` — Returns true if the current pointer position (the index finger tip) intersections
with the given box object.
- `.updateMatrixWorld( force :boolean)` — Overwritten with a custom implementation. Makes sure the motion controller updates the mesh.

## Source