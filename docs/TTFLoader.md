# TTFLoader
Extends: Loader→

A loader for the TTF format. Loads TTF files and converts them into typeface JSON that can be used directly
to create THREE.Font objects.

## Constructor
`newTTFLoader( manager :LoadingManager)`
Constructs a new TTF loader.

## Import

## Properties
- `.reversed : boolean` — Whether the TTF commands should be reversed or not. Default is false .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded TTF asset
to the onLoad() callback.
- `.parse( arraybuffer :ArrayBuffer) : Object` — Parses the given TTF data and returns a JSON for creating a font.

## Source