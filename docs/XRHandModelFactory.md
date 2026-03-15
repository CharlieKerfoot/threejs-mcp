# XRHandModelFactory

Similar to XRControllerModelFactory , this class allows to create hand models
for WebXR controllers that can be added as a visual representation to your scene.

## Constructor
`newXRHandModelFactory( gltfLoader :GLTFLoader, onLoad :function)`
Constructs a new XR hand model factory.

## Import

## Properties
- `.gltfLoader :GLTFLoader` — A glTF loader that is used to load hand models. Default is null .
- `.onLoad : function` — A callback that is executed when a hand model has been loaded. Default is null .
- `.path : string` — The path to the model repository. Default is null .

## Methods
- `.createHandModel( controller :Group, profile :'spheres' | 'boxes' | 'mesh') :XRHandModel` — Creates a controller model for the given WebXR hand controller.
- `.setPath( path :string) :XRHandModelFactory` — Sets the path to the hand model repository.

## Source