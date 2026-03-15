# KMZLoader
Extends: Loader→

A loader for the KMZ format.

## Constructor
`newKMZLoader( manager :LoadingManager)`
Constructs a new KMZ loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded KMZ asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) : Object` — Parses the given KMZ data and returns an object holding the scene.

## Source