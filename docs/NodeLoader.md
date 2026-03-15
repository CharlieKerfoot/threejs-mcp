# NodeLoader
Extends: Loader→

A loader for loading node objects in the three.js JSON Object/Scene format.

## Constructor
`newNodeLoader( manager :LoadingManager)`
Constructs a new node loader.

## Properties
- `.nodes : Object.<string, Node.constructor>` — Represents a dictionary of node types.
- `.textures : Object.<string,Texture>` — Represents a dictionary of textures.

## Methods
- `.createNodeFromType( type :string) :Node` — Creates a node object from the given type.
- `.load( url :string, onLoad :function, onProgress :function, onError :function)` — Loads the node definitions from the given URL.
- `.parse( json :Object) :Node` — Parses the node from the given JSON.
- `.parseNodes( json :Array.<Object>) : Object.<string,Node>` — Parse the node dependencies for the loaded node.
- `.setNodes( value :Object.<string, Node.constructor>) :NodeLoader` — Defines the dictionary of node types.
- `.setTextures( value :Object.<string,Texture>) :NodeLoader` — Defines the dictionary of textures.

## Source