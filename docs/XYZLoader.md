# XYZLoader
Extends: Loader→

A loader for the XYZ format. XYZ is a very simple format for storing point clouds. The layouts XYZ (points) and XYZRGB (points + colors) are supported.

## Constructor
`newXYZLoader()`

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded XYZ asset
to the onLoad() callback.
- `.parse( text :string) :BufferGeometry` — Parses the given XYZ data and returns the resulting geometry.

## Source