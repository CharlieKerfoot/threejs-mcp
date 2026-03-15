# ColladaLoader
Extends: Loader→

A loader for the Collada format. The Collada format is very complex so this loader only supports a subset of what
is defined in the official specification . Assets with a Z-UP coordinate system are transformed it into Y-UP by a simple rotation.
The vertex data are not converted.

## Constructor
`newColladaLoader()`

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded Collada asset
to the onLoad() callback.
- `.parse( text :string, path :string) : Object` — Parses the given Collada data and returns a result object holding the parsed scene,
an array of animation clips and kinematics.

## Source