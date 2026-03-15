# HDRLoader
Extends: Loader→DataTextureLoader→

A loader for the RGBE HDR texture format.

## Constructor
`newHDRLoader( manager :LoadingManager)`
Constructs a new RGBE/HDR loader.

## Import

## Properties
- `.type :HalfFloatType|FloatType` — The texture type. Default is HalfFloatType .

## Methods
- `.parse( buffer :ArrayBuffer) :DataTextureLoader~TexData` — Parses the given RGBE texture data.
- `.setDataType( value :HalfFloatType|FloatType) :HDRLoader` — Sets the texture type.

## Source