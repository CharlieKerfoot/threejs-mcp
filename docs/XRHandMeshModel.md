# XRHandMeshModel

Represents one of the hand model types XRHandModelFactory might produce
depending on the selected profile. XRHandMeshModel represents a hand with a
custom asset.

## Constructor
`newXRHandMeshModel( handModel :XRHandModel, controller :Group, path :string, handedness :XRHandedness, loader :Loader, onLoad :function)`
Constructs a new XR hand mesh model.

## Import

## Properties
- `.bones : Array.<Bone>` — An array of bones representing the bones
of the hand skeleton.
- `.controller :Group` — The WebXR controller.
- `.handModel :XRHandModel` — The hand model.

## Methods
- `.updateMesh()` — Updates the mesh based on the tracked XR joints data.

## Source