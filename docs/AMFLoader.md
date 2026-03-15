# AMFLoader
Extends: Loader→

A loader for the AMF format. The loader supports materials, color and ZIP compressed files.
No constellation support (yet).

## Constructor
`newAMFLoader( manager :LoadingManager)`
Constructs a new AMF loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded AMF asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :Group` — Parses the given AMF data and returns the resulting group.

## Source