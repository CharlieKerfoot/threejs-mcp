# ObjectLoader
Extends: Loader→

A loader for loading a JSON resource in the JSON Object/Scene format .
The files are internally loaded via FileLoader .

## Constructor
`newObjectLoader( manager :LoadingManager)`
Constructs a new object loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and pass the loaded 3D object to the onLoad() callback.
- `.loadAsync( url :string, onProgress :onProgressCallback) : Promise.<Object3D>` — Async version of ObjectLoader#load .
- `.parse( json :Object, onLoad :onLoad) :Object3D` — Parses the given JSON. This is used internally by ObjectLoader#load but can also be used directly to parse a previously loaded JSON structure.
- `.parseAsync( json :Object) : Promise.<Object3D>` — Async version of ObjectLoader#parse .

## Source