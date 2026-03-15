# KTX2Loader
Extends: Loader→

A loader for KTX 2.0 GPU Texture containers. KTX 2.0 is a container format for various GPU texture formats. The loader supports Basis Universal GPU textures,
which can be quickly transcoded to a wide variety of GPU texture compression formats. While KTX 2.0 also allows
other hardware-specific formats, this loader does not yet parse them. This loader parses the KTX 2.0 container and transcodes to a supported GPU compressed texture format.
The required WASM transcoder and JS wrapper are available from the examples/jsm/libs/basis directory. This loader relies on Web Assembly which is not supported in older browsers. References: KTX specification DFD BasisU HDR

## Constructor
`newKTX2Loader( manager :LoadingManager)`
Constructs a new KTX2 loader.

## Import

## Methods
- `.detectSupport( renderer :WebGPURenderer|WebGLRenderer) :KTX2Loader` — Detects hardware support for available compressed texture formats, to determine
the output format for the transcoder. Must be called before loading a texture.
- `.detectSupportAsync( renderer :WebGPURenderer) : Promise` — Async version of KTX2Loader#detectSupport .
- `.dispose()` — Frees internal resources. This method should be called
when the loader is no longer required.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded KTX2 texture
to the onLoad() callback.
- `.parse( buffer :ArrayBuffer, onLoad :function, onError :onErrorCallback) : Promise` — Parses the given KTX2 data.
- `.setTranscoderPath( path :string) :KTX2Loader` — Sets the transcoder path. The WASM transcoder and JS wrapper are available from the examples/jsm/libs/basis directory.
- `.setWorkerLimit( workerLimit :number) :KTX2Loader` — Sets the maximum number of Web Workers to be allocated by this instance.

## Source