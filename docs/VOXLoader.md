# VOXLoader
Extends: Loader→

A loader for the VOX format.

## Constructor
`newVOXLoader()`

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded VOX asset
to the onLoad() callback.
- `.parse( buffer :ArrayBuffer) : Object` — Parses the given VOX data and returns the result object.

## Source