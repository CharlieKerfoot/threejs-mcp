# UltraHDRLoader
Extends: Loader→

A loader for the Ultra HDR Image Format. Existing HDR or EXR textures can be converted to Ultra HDR with this tool . Current feature set: JPEG headers (required) XMP metadata (legacy format, supported) ISO 21496-1 metadata (current standard, supported) XMP validation (not implemented) EXIF profile (not implemented) ICC profile (not implemented) Binary storage for SDR & HDR images (required) Gainmap metadata (required) Non-JPEG image formats (not implemented) Primary image as an HDR image (not implemented)

## Constructor
`newUltraHDRLoader( manager :LoadingManager)`
Constructs a new Ultra HDR loader.

## Import

## Properties
- `.type :HalfFloatType|FloatType` — The texture type. Default is HalfFloatType .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :DataTexture` — Starts loading from the given URL and passes the loaded Ultra HDR texture
to the onLoad() callback.
- `.parse( buffer :ArrayBuffer, onLoad :function)` — Parses the given Ultra HDR texture data.
- `.setDataType( value :HalfFloatType|FloatType) :UltraHDRLoader` — Sets the texture type.

## Source