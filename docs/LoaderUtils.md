# LoaderUtils

A class with loader utility functions.

## Constructor
`newLoaderUtils()`

## Static Methods
- `.extractUrlBase( url :string) : string` — Extracts the base URL from the given URL.
- `.resolveURL( url :string, path :string) : string` — Resolves relative URLs against the given path. Absolute paths, data urls,
and blob URLs will be returned as is. Invalid URLs will return an empty
string.

## Source