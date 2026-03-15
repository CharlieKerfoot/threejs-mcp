# LUTCubeLoader
Extends: Loader→

A loader for the Cube LUT format. References: Cube LUT Specification

## Constructor
`newLUTCubeLoader( manager :LoadingManager)`
Constructs a new Cube LUT loader.

## Import

## Classes

## Properties
- `.type :UnsignedByteType|FloatType` — The texture type. Default is UnsignedByteType .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded Cube LUT asset
to the onLoad() callback.
- `.parse( input :string) : Object` — Parses the given Cube LUT data and returns the resulting 3D data texture.
- `.setType( type :UnsignedByteType|FloatType) :LUTCubeLoader` — Sets the texture type.

## Source