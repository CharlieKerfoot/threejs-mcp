# IESLoader
Extends: Loader→

A loader for the IES format. The loaded texture should be assigned to IESSpotLight#map .

## Constructor
`newIESLoader( manager :LoadingManager)`
Constructs a new IES loader.

## Import

## Properties
- `.type :HalfFloatType|FloatType` — The texture type. Default is HalfFloatType .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded IES texture
to the onLoad() callback.
- `.parse( text :string) :DataTexture` — Parses the given IES data.

## Source