# Cache

A simple caching system, used internally by FileLoader .
To enable caching across all loaders that use FileLoader , add THREE.Cache.enabled = true. once in your app.

## Properties
- `.enabled : boolean` — Whether caching is enabled or not. Default is false .
- `.files : Object.<string, Object>` — A dictionary that holds cached files.

## Static Methods
- `.add( key :string, file :Object)` — Adds a cache entry with a key to reference the file. If this key already
holds a file, it is overwritten.
- `.clear()` — Remove all values from the cache.
- `.get( key :string) : Object | undefined` — Gets the cached value for the given key.
- `.remove( key :string)` — Removes the cached file associated with the given key.

## Source