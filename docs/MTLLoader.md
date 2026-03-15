# MTLLoader
Extends: Loader→

A loader for the MTL format. The Material Template Library format (MTL) or .MTL File Format is a companion file format
to OBJ that describes surface shading (material) properties of objects within one or more
OBJ files.

## Constructor
`newMTLLoader()`

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded MTL asset
to the onLoad() callback.
- `.parse( text :string, path :string) : MaterialCreator` — Parses the given MTL data and returns the resulting material creator.
- `.setMaterialOptions( value :MTLLoader~MaterialOptions) :MTLLoader` — Sets the material options.

## Type Definitions
- `.MaterialOptions` — Material options of MTLLoader .

## Source