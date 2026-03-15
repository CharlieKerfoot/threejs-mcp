# TDSLoader
Extends: Loader→

A loader for the 3DS format, based on lib3ds. Loads geometry with uv and materials basic properties with texture support.

## Constructor
`newTDSLoader( manager :LoadingManager)`
Constructs a new 3DS loader.

## Import

## Properties
- `.debug : boolean` — Whether debug mode should be enabled or not. Default is false .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded 3DS asset
to the onLoad() callback.
- `.parse( arraybuffer :ArrayBuffer, path :string) :Group` — Parses the given 3DS data and returns the resulting data.

## Source