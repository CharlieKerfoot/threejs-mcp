# VRMLLoader
Extends: Loader→

A loader for the VRML format.

## Constructor
`newVRMLLoader( manager :LoadingManager)`
Constructs a new VRML loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded VRML asset
to the onLoad() callback.
- `.parse( data :string, path :string) :Scene` — Parses the given VRML data and returns the resulting scene.

## Source