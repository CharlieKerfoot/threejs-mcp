# LoadingManager

Handles and keeps track of loaded and pending data. A default global
instance of this class is created and used by loaders if not supplied
manually. In general that should be sufficient, however there are times when it can
be useful to have separate loaders - for example if you want to show
separate loading bars for objects and textures.

## Constructor
`newLoadingManager( onLoad :function, onProgress :function, onError :function)`
Constructs a new loading manager.

## Properties
- `.abortController : AbortController` — Used for aborting ongoing requests in loaders using this manager.
- `.onError : function | undefined` — Executes when an error occurs. Default is undefined .
- `.onLoad : function | undefined` — Executes when all items have been loaded. Default is undefined .
- `.onProgress : function | undefined` — Executes when single items have been loaded. Default is undefined .
- `.onStart : function | undefined` — Executes when an item starts loading. Default is undefined .

## Methods
- `.abort() :LoadingManager` — Can be used to abort ongoing loading requests in loaders using this manager.
The abort only works if the loaders implement Loader#abort and AbortSignal.any() is supported in the browser.
- `.addHandler( regex :string, loader :Loader) :LoadingManager` — Registers a loader with the given regular expression. Can be used to
define what loader should be used in order to load specific files. A
typical use case is to overwrite the default loader for tex...
- `.getHandler( file :string) :Loader` — Can be used to retrieve the registered loader for the given file path.
- `.itemEnd( url :string)` — This should be called by any loader using the manager when the loader
ended loading an item.
- `.itemError( url :string)` — This should be called by any loader using the manager when the loader
encounters an error when loading an item.
- `.itemStart( url :string)` — This should be called by any loader using the manager when the loader
starts loading an item.
- `.removeHandler( regex :string) :LoadingManager` — Removes the loader for the given regular expression.
- `.resolveURL( url :string) : string` — Given a URL, uses the URL modifier callback (if any) and returns a
resolved URL. If no URL modifier is set, returns the original URL.
- `.setURLModifier( transform :function) :LoadingManager` — If provided, the callback will be passed each resource URL before a
request is sent. The callback may return the original URL, or a new URL to
override loading behavior. This behavior can be used t...

## Source