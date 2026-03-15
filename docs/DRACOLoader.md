# DRACOLoader
Extends: Loader→

A loader for the Draco format. Draco is an open source library for compressing
and decompressing 3D meshes and point clouds. Compressed geometry can be significantly smaller,
at the cost of additional decoding time on the client device. Standalone Draco files have a .drc extension, and contain vertex positions, normals, colors,
and other attributes. Draco files do not contain materials, textures, animation, or node hierarchies –
to use these features, embed Draco geometry inside of a glTF file. A normal glTF file can be converted
to a Draco-compressed glTF file using glTF-Pipeline .
When using Draco with glTF, an instance of DRACOLoader will be used internally by GLTFLoader . It is recommended to create one DRACOLoader instance and reuse it to avoid loading and creating
multiple decoder instances. DRACOLoader will automatically use either the JS or the WASM decoding library, based on
browser capabilities.

## Constructor
`newDRACOLoader( manager :LoadingManager)`
Constructs a new Draco loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded Draco asset
to the onLoad() callback.
- `.parse( buffer :ArrayBuffer, onLoad :function, onError :onErrorCallback)` — Parses the given Draco data.
- `.setDecoderConfig( config :Object) :DRACOLoader` — Provides configuration for the decoder libraries. Configuration cannot be changed after decoding begins.
- `.setDecoderPath( path :string) :DRACOLoader` — Provides configuration for the decoder libraries. Configuration cannot be changed after decoding begins.
- `.setWorkerLimit( workerLimit :number) :DRACOLoader` — Sets the maximum number of Web Workers to be used during decoding.
A lower limit may be preferable if workers are also for other tasks in the application.

## Source