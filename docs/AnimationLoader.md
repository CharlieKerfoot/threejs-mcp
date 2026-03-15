# AnimationLoader
Extends: Loader→

Class for loading animation clips in the JSON format. The files are internally
loaded via FileLoader .

## Constructor
`newAnimationLoader( manager :LoadingManager)`
Constructs a new animation loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and pass the loaded animations as an array
holding instances of AnimationClip to the onLoad() callback.
- `.parse( json :Object) : Array.<AnimationClip>` — Parses the given JSON object and returns an array of animation clips.

## Source