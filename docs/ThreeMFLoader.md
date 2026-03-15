# ThreeMFLoader
Extends: Loader→

A loader for the 3D Manufacturing Format (3MF) format. The following features from the core specification are supported: 3D Models Object Resources (Meshes and Components) Material Resources (Base Materials) 3MF Materials and Properties Extension are only partially supported. Texture 2D Texture 2D Groups Color Groups (Vertex Colors) Metallic Display Properties (PBR)

## Constructor
`newThreeMFLoader( manager :LoadingManager)`
Constructs a new 3MF loader.

## Import

## Properties
- `.availableExtensions : Array.<Object>` — An array of available extensions.

## Methods
- `.addExtension( extension :Object)` — Adds a 3MF extension.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded 3MF asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :Group` — Parses the given 3MF data and returns the resulting group.

## Source