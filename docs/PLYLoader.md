# PLYLoader
Extends: Loader→

A loader for PLY the PLY format (known as the Polygon
File Format or the Stanford Triangle Format). Limitations: ASCII decoding assumes file is UTF-8.

## Constructor
`newPLYLoader( manager :LoadingManager)`
Constructs a new PLY loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded PLY asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) :BufferGeometry` — Parses the given PLY data and returns the resulting geometry.
- `.setCustomPropertyNameMapping( mapping :Object)` — Custom properties outside of the defaults for position, uv, normal
and color attributes can be added using the setCustomPropertyNameMapping method.
For example, the following maps the element prope...
- `.setPropertyNameMapping( mapping :Object)` — Sets a property name mapping that maps default property names
to custom ones. For example, the following maps the properties
“diffuse_(red|green|blue)” in the file to standard color names. loader.s...

## Source