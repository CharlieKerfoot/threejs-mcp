# MaterialLoader
Extends: Loader→

Class for loading materials. The files are internally
loaded via FileLoader . This loader does not support node materials. Use NodeMaterialLoader instead.

## Constructor
`newMaterialLoader( manager :LoadingManager)`
Constructs a new material loader.

## Properties
- `.textures : Object.<string,Texture>` — A dictionary holding textures used by the material.

## Methods
- `.createMaterialFromType( type :string) :Material` — Creates a material for the given type.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and pass the loaded material to the onLoad() callback.
- `.parse( json :Object) :Material` — Parses the given JSON object and returns a material.
- `.setTextures( value :Object) :MaterialLoader` — Textures are not embedded in the material JSON so they have
to be injected before the loading process starts.

## Static Methods
- `.createMaterialFromType( type :string) :Material` — Creates a material for the given type.

## Source