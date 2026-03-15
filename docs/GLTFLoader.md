# GLTFLoader
Extends: Loader→

A loader for the glTF 2.0 format. glTF (GL Transmission Format) is an open format specification whenever possible. Be advised that image bitmaps are not
automatically GC-collected when they are no longer referenced, and they require special handling during
the disposal process. GLTFLoader supports the following glTF 2.0 extensions: KHR_draco_mesh_compression KHR_materials_clearcoat KHR_materials_dispersion KHR_materials_ior KHR_materials_specular KHR_materials_transmission KHR_materials_iridescence KHR_materials_unlit KHR_materials_volume KHR_mesh_quantization KHR_meshopt_compression KHR_lights_punctual KHR_texture_basisu KHR_texture_transform EXT_texture_webp EXT_meshopt_compression EXT_mesh_gpu_instancing The following glTF 2.0 extension is supported by an external user plugin: KHR_materials_variants MSFT_texture_dds KHR_animation_pointer NEEDLE_progressive

## Constructor
`newGLTFLoader( manager :LoadingManager)`
Constructs a new glTF loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded glTF asset
to the onLoad() callback.
- `.parse( data :string | ArrayBuffer, path :string, onLoad :function, onError :onErrorCallback)` — Parses the given glTF data and returns the resulting group.
- `.parseAsync( data :string | ArrayBuffer, path :string) : Promise.<GLTFLoader~LoadObject>` — Async version of GLTFLoader#parse .
- `.register( callback :function) :GLTFLoader` — Registers a plugin callback. This API is internally used to implement the various
glTF extensions but can also used by third-party code to add additional logic
to the loader.
- `.setDRACOLoader( dracoLoader :DRACOLoader) :GLTFLoader` — Sets the given Draco loader to this loader. Required for decoding assets
compressed with the KHR_draco_mesh_compression extension.
- `.setKTX2Loader( ktx2Loader :KTX2Loader) :GLTFLoader` — Sets the given KTX2 loader to this loader. Required for loading KTX2
compressed textures.
- `.setMeshoptDecoder( meshoptDecoder :Object) :GLTFLoader` — Sets the given meshopt decoder. Required for decoding assets
compressed with the EXT_meshopt_compression extension.
- `.unregister( callback :function) :GLTFLoader` — Unregisters a plugin callback.

## Type Definitions
- `.LoadObject` — Loader result of GLTFLoader .

## Source