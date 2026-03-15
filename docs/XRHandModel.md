# XRHandModel
Extends: EventDispatcher→Object3D→

Represents a XR hand model.

## Constructor
`newXRHandModel( controller :Group)`
Constructs a new XR hand model.

## Properties
- `.controller :Group` — The hand controller.
- `.envMap :Texture` — The controller's environment map. Default is null .
- `.mesh :Mesh` — The model mesh. Default is null .
- `.motionController : MotionController` — The motion controller. Default is null .

## Methods
- `.updateMatrixWorld( force :boolean)` — Overwritten with a custom implementation. Makes sure the motion controller updates the mesh.

## Source