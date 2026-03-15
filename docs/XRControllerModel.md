# XRControllerModel
Extends: EventDispatcher→Object3D→

Represents a XR controller model.

## Constructor
`newXRControllerModel()`
Constructs a new XR controller model.

## Properties
- `.envMap :Texture` — The controller's environment map. Default is null .
- `.motionController : MotionController` — The motion controller. Default is null .

## Methods
- `.setEnvironmentMap( envMap :Texture) :XRControllerModel` — Sets an environment map that is applied to the controller model.
- `.updateMatrixWorld( force :boolean)` — Overwritten with a custom implementation. Polls data from the XRInputSource and updates the
model's components to match the real world data.

## Source