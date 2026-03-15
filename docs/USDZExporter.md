# USDZExporter

An exporter for USDZ.

## Constructor
`newUSDZExporter()`
Constructs a new USDZ exporter.

## Import

## Properties
- `.textureUtils :WebGLTextureUtils|WebGPUTextureUtils` — A reference to a texture utils module. Default is null .

## Methods
- `.parse( scene :Object3D, onDone :USDZExporter~OnDone, onError :USDZExporter~OnError, options :USDZExporter~Options)` — Parse the given 3D object and generates the USDZ output.
- `.parseAsync( scene :Object3D, options :USDZExporter~Options) : Promise.<ArrayBuffer>` — Async version of USDZExporter#parse .
- `.setTextureUtils( utils :WebGLTextureUtils|WebGPUTextureUtils)` — Sets the texture utils for this exporter. Only relevant when compressed textures have to be exported. Depending on whether you use WebGLRenderer or WebGPURenderer , you must inject the
correspondin...

## Type Definitions
- `.OnDone( result :ArrayBuffer)` — onDone callback of USDZExporter .
- `.OnError( error :Error)` — onError callback of USDZExporter .
- `.Options` — Export options of USDZExporter .

## Source