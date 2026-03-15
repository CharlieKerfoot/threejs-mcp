# FBXLoader
Extends: Loader→

A loader for the FBX format. Requires FBX file to be >= 7.0 and in ASCII or >= 6400 in Binary format.
Versions lower than this may load but will probably have errors. Needs Support: Morph normals / blend shape normals FBX format references: C++ SDK reference Binary format specification: FBX binary file format specification

## Constructor
`newFBXLoader( manager :LoadingManager)`
Constructs a new FBX loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded FBX asset
to the onLoad() callback.
- `.parse( FBXBuffer :ArrayBuffer, path :string) :Group` — Parses the given FBX data and returns the resulting group.

## Source