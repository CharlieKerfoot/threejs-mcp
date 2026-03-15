# XRControllerModelFactory

Allows to create controller models for WebXR controllers that can be added as a visual
representation to your scene. XRControllerModelFactory will automatically fetch controller
models that match what the user is holding as closely as possible. The models should be
attached to the object returned from getControllerGrip in order to match the orientation of
the held device. This module depends on the motion-controllers third-part library.

## Constructor
`newXRControllerModelFactory( gltfLoader :GLTFLoader, onLoad :function)`
Constructs a new XR controller model factory.

## Import

## Properties
- `.gltfLoader :GLTFLoader` — A glTF loader that is used to load controller models. Default is null .
- `.onLoad : function` — A callback that is executed when a controller model has been loaded. Default is null .
- `.path : string` — The path to the model repository.

## Methods
- `.createControllerModel( controller :Group) :XRControllerModel` — Creates a controller model for the given WebXR controller.
- `.setPath( path :string) :XRControllerModelFactory` — Sets the path to the model repository.

## Source