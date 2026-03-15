# NRRDLoader
Extends: Loader→

A loader for the NRRD format.

## Constructor
`newNRRDLoader( manager :LoadingManager)`
Constructs a new NRRD loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded NRRD asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :Volume` — Parses the given NRRD data and returns the resulting volume data.
- `.setSegmentation( segmentation :boolean)` — Toggles the segmentation mode.

## Source