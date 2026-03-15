# EXRLoader
Extends: Loader→DataTextureLoader→

A loader for the OpenEXR texture format. EXRLoader currently supports uncompressed, ZIP(S), RLE, PIZ and DWA/B compression.
Supports reading as UnsignedByte, HalfFloat and Float type data texture.

## Constructor
`newEXRLoader( manager :LoadingManager)`
Constructs a new EXR loader.

## Import

## Properties
- `.outputFormat :RGBAFormat|RGFormat|RedFormat` — Texture output format. Default is RGBAFormat .
- `.type :HalfFloatType|FloatType` — The texture type. Default is HalfFloatType .

## Methods
- `.parse( buffer :ArrayBuffer) :DataTextureLoader~TexData` — Parses the given EXR texture data.
- `.setDataType( value :HalfFloatType|FloatType) :EXRLoader` — Sets the texture type.
- `.setOutputFormat( value :RGBAFormat|RGFormat|RedFormat) :EXRLoader` — Sets texture output format. Defaults to RGBAFormat .

## Source