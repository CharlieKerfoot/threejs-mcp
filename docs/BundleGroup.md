# BundleGroup
Extends: EventDispatcher→Object3D→Group→

A specialized group which enables applications access to the
Render Bundle API of WebGPU. The group with all its descendant nodes
are considered as one render bundle and processed as such by
the renderer. This module is only fully supported by WebGPURenderer with a WebGPU backend.
With a WebGL backend, the group can technically be rendered but without
any performance improvements.

## Constructor
`newBundleGroup()`
Constructs a new bundle group.

## Properties
- `.isBundleGroup : boolean` — This flag can be used for type testing. Default is true .
- `.needsUpdate : boolean` — Set this property to true when the bundle group has changed. Default is false .
- `.static : boolean` — Whether the bundle is static or not. When set to true , the structure
is assumed to be static and does not change. E.g. no new objects are
added to the group. If a change is required, an update can...
- `.type : string` — This property is only relevant for detecting types
during serialization/deserialization. It should always
match the class name. Default is 'BundleGroup' .
- `.version : number` — The bundle group's version. Default is 0 .

## Source