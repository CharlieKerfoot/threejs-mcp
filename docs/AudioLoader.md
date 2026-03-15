# AudioLoader
Extends: Loader→

Class for loading audio buffers. Audios are internally
loaded via FileLoader .

## Constructor
`newAudioLoader( manager :LoadingManager)`
Constructs a new audio loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded audio buffer
to the onLoad() callback.

## Source