# LUTImageLoader
Extends: Loader→

A loader for loading LUT images.

## Constructor
`newLUTImageLoader( manager :LoadingManager)`
Constructs a new LUT loader.

## Import

## Classes

## Properties
- `.flip : boolean` — Whether to vertically flip the LUT or not. Depending on the LUT's origin, the texture has green at the bottom (e.g. for Unreal)
or green at the top (e.g. for Unity URP Color Lookup). If you're usin...

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded LUT
to the onLoad() callback.
- `.parse( dataArray :Uint8ClampedArray, size :number) : Object` — Parses the given LUT data and returns the resulting 3D data texture.

## Source