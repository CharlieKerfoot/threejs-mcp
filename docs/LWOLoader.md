# LWOLoader
Extends: Loader→

A loader for the LWO format. LWO3 and LWO2 formats are supported. References: LWO3 format specification LWO2 format specification

## Constructor
`newLWOLoader( manager :LoadingManager)`
Constructs a new LWO loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded LWO asset
to the onLoad() callback.
- `.parse( iffBuffer :ArrayBuffer, path :string, modelName :string) : Object` — Parses the given LWO data and returns the resulting meshes and materials.

## Source