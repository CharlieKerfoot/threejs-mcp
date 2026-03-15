# LUT3dlLoader
Extends: Loader→

A loader for the 3DL LUT format. References: 3D LUTs Format Spec for .3dl

## Constructor
`newLUT3dlLoader( manager :LoadingManager)`
Constructs a new 3DL LUT loader.

## Import

## Classes

## Properties
- `.type :UnsignedByteType|FloatType` — The texture type. Default is UnsignedByteType .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded 3DL LUT asset
to the onLoad() callback.
- `.parse( input :string) : Object` — Parses the given 3DL LUT data and returns the resulting 3D data texture.
- `.setType( type :UnsignedByteType|FloatType) :LUT3dlLoader` — Sets the texture type.

## Source