# OBJLoader
Extends: Loader→

A loader for the OBJ format. The OBJ format is a simple data-format that
represents 3D geometry in a human readable format as the position of each vertex, the UV position of
each texture coordinate vertex, vertex normals, and the faces that make each polygon defined as a list
of vertices, and texture vertices.

## Constructor
`newOBJLoader( manager :LoadingManager)`
Constructs a new OBJ loader.

## Import

## Properties
- `.materials : MaterialCreator` — A reference to a material creator. Default is null .

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded OBJ asset
to the onLoad() callback.
- `.parse( text :string) :Group` — Parses the given OBJ data and returns the resulting group.
- `.setMaterials( materials :MaterialCreator) :OBJLoader` — Sets the material creator for this OBJ. This object is loaded via MTLLoader .

## Source