# USDLoader
Extends: Loader→

A loader for the USD format (USD, USDA, USDC, USDZ). Supports both ASCII (USDA) and binary (USDC) USD files, as well as
USDZ archives containing either format.

## Constructor
`newUSDLoader( manager :LoadingManager)`
Constructs a new USDZ loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded USDZ asset
to the onLoad() callback.
- `.parse( buffer :ArrayBuffer | string) :Group` — Parses the given USDZ data and returns the resulting group.

## Source