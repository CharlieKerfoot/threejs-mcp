# PropertyBinding

This holds a reference to a real property in the scene graph; used internally.

## Constructor
`newPropertyBinding( rootNode :Object, path :string, parsedPath :Object)`
Constructs a new property binding.

## Properties
- `.node : Object` — The object owns the animated property.
- `.parsedPath : Object` — An object holding information about the path.
- `.path : string` — The object path to the animated property.
- `.rootNode :Object3D|Skeleton` — The root node.

## Methods
- `.bind()` — Creates a getter / setter pair for the property tracked by this binding.
- `.unbind()` — Unbinds the property.

## Static Methods
- `.create( root :Object, path :string, parsedPath :Object) :PropertyBinding| Composite` — Factory method for creating a property binding from the given parameters.
- `.findNode( root :Object, nodeName :string | number) : Object` — Searches for a node in the hierarchy of the given root object by the given
node name.
- `.parseTrackName( trackName :string) : Object` — Parses the given track name (an object path to an animated property) and
returns an object with information about the path. Matches strings in the following forms: nodeName.property nodeName.proper...
- `.sanitizeNodeName( name :string) : string` — Replaces spaces with underscores and removes unsupported characters from
node names, to ensure compatibility with parseTrackName().

## Source