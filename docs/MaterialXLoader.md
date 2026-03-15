# MaterialXLoader
Extends: Loader→

A loader for the MaterialX format. The node materials loaded with this loader can only be used with WebGPURenderer .

## Constructor
`newMaterialXLoader( manager :LoadingManager)`
Constructs a new MaterialX loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :MaterialXLoader` — Starts loading from the given URL and passes the loaded MaterialX asset
to the onLoad() callback.
- `.parse( text :string) : Object.<string,NodeMaterial>` — Parses the given MaterialX data and returns the resulting materials. Supported standard_surface inputs: base, base_color: Base color/albedo opacity: Alpha/transparency specular_roughness: Surface r...

## Source