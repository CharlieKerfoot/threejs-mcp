# XRHandPrimitiveModel

Represents one of the hand model types XRHandModelFactory might produce
depending on the selected profile. XRHandPrimitiveModel represents a hand
with sphere or box primitives according to the selected primitive option.

## Constructor
`newXRHandPrimitiveModel( handModel :XRHandModel, controller :Group, path :string, handedness :XRHandedness, options :XRHandPrimitiveModel~Options)`
Constructs a new XR hand primitive model.

## Import

## Properties
- `.controller :Group` — The WebXR controller.
- `.envMap :Texture` — The model's environment map. Default is null .
- `.handModel :XRHandModel` — The hand model.

## Methods
- `.updateMesh()` — Updates the mesh based on the tracked XR joints data.

## Type Definitions
- `.Options` — Constructor options of XRHandPrimitiveModel .

## Source