# Loader

Abstract base class for loaders.

## Constructor
`newLoader( manager :LoadingManager)(abstract)`
Constructs a new loader.

## Properties
- `.crossOrigin : string` — The crossOrigin string to implement CORS for loading the url from a
different domain that allows CORS. Default is 'anonymous' .
- `.manager :LoadingManager` — The loading manager. Default is DefaultLoadingManager .
- `.path : string` — The base path from which the asset will be loaded.
- `.requestHeader : Object.<string,any>` — The request header used in HTTP request.
- `.resourcePath : string` — The base path from which additional resources like textures will be loaded.
- `.withCredentials : boolean` — Whether the XMLHttpRequest uses credentials. Default is false .
- `.DEFAULT_MATERIAL_NAME : string` — The default material name that is used by loaders
when creating materials for loaded 3D objects. Note: Not all loaders might honor this setting. Default is '__DEFAULT' .

## Methods
- `.abort() :Loader` — This method can be implemented in loaders for aborting ongoing requests.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) (abstract)` — This method needs to be implemented by all concrete loaders. It holds the
logic for loading assets from the backend.
- `.loadAsync( url :string, onProgress :onProgressCallback) : Promise` — A async version of Loader#load .
- `.parse( data :any) (abstract)` — This method needs to be implemented by all concrete loaders. It holds the
logic for parsing the asset into three.js entities.
- `.setCrossOrigin( crossOrigin :string) :Loader` — Sets the crossOrigin String to implement CORS for loading the URL
from a different domain that allows CORS.
- `.setPath( path :string) :Loader` — Sets the base path for the asset.
- `.setRequestHeader( requestHeader :Object) :Loader` — Sets the given request header.
- `.setResourcePath( resourcePath :string) :Loader` — Sets the base path for dependent resources like textures.
- `.setWithCredentials( value :boolean) :Loader` — Whether the XMLHttpRequest uses credentials such as cookies, authorization
headers or TLS client certificates, see XMLHttpRequest.withCredentials . Note: This setting has no effect if you are loadi...

## Source