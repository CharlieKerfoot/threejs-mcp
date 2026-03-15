# GLTFExporter

An exporter for glTF 2.0. glTF (GL Transmission Format) is an open format specification for efficient delivery and loading of 3D content. Assets may be provided either in JSON (.gltf)
or binary (.glb) format. External files store textures (.jpg, .png) and additional binary
data (.bin). A glTF asset may deliver one or more scenes, including meshes, materials,
textures, skins, skeletons, morph targets, animations, lights, and/or cameras. GLTFExporter supports the glTF 2.0 extensions : KHR_lights_punctual KHR_materials_clearcoat KHR_materials_dispersion KHR_materials_emissive_strength KHR_materials_ior KHR_materials_iridescence KHR_materials_specular KHR_materials_sheen KHR_materials_transmission KHR_materials_unlit KHR_materials_volume KHR_mesh_quantization KHR_texture_transform EXT_materials_bump EXT_mesh_gpu_instancing The following glTF 2.0 extension is supported by an external user plugin: KHR_materials_variants

## Constructor
`newGLTFExporter()`
Constructs a new glTF exporter.

## Import

## Properties
- `.textureUtils :WebGLTextureUtils|WebGPUTextureUtils` — A reference to a texture utils module. Default is null .

## Methods
- `.parse( input :Scene| Array.<Scene>, onDone :GLTFExporter~OnDone, onError :GLTFExporter~OnError, options :GLTFExporter~Options)` — Parses the given scenes and generates the glTF output.
- `.parseAsync( input :Scene| Array.<Scene>, options :GLTFExporter~Options) : Promise.<(ArrayBuffer|string)>` — Async version of GLTFExporter#parse .
- `.register( callback :function) :GLTFExporter` — Registers a plugin callback. This API is internally used to implement the various
glTF extensions but can also used by third-party code to add additional logic
to the exporter.
- `.setTextureUtils( utils :WebGLTextureUtils|WebGPUTextureUtils) :GLTFExporter` — Sets the texture utils for this exporter. Only relevant when compressed textures have to be exported. Depending on whether you use WebGLRenderer or WebGPURenderer , you must inject the
correspondin...
- `.unregister( callback :function) :GLTFExporter` — Unregisters a plugin callback.

## Type Definitions
- `.OnDone( result :ArrayBuffer | string)` — onDone callback of GLTFExporter .
- `.OnError( error :Error)` — onError callback of GLTFExporter .
- `.Options` — Export options of GLTFExporter .

## Source