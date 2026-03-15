# FileLoader
Extends: Loader→

A low level class for loading resources with the Fetch API, used internally by
most loaders. It can also be used directly to load any file type that does
not have a loader. This loader supports caching. If you want to use it, add THREE.Cache.enabled = true; once to your application.

## Constructor
`newFileLoader( manager :LoadingManager)`
Constructs a new file loader.

## Properties
- `.mimeType : string` — The expected mime type. Valid values can be found here
- `.responseType : 'arraybuffer' | 'blob' | 'document' | 'json' | ''` — The expected response type. Default is '' .

## Methods
- `.abort() :FileLoader` — Aborts ongoing fetch requests.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :any| undefined` — Starts loading from the given URL and pass the loaded response to the onLoad() callback.
- `.setMimeType( value :string) :FileLoader` — Sets the expected mime type of the loaded file.
- `.setResponseType( value :'arraybuffer' | 'blob' | 'document' | 'json' | '') :FileLoader` — Sets the expected response type.

## Source