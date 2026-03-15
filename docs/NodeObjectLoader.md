# NodeObjectLoader
Extends: Loader→ObjectLoader→

A special type of object loader for loading 3D objects using
node materials.

## Constructor
`newNodeObjectLoader( manager :LoadingManager)`
Constructs a new node object loader.

## Properties
- `.nodeMaterials : Object.<string, NodeMaterial.constructor>` — Represents a dictionary of node material types.
- `.nodes : Object.<string, Node.constructor>` — Represents a dictionary of node types.

## Methods
- `.parse( json :Object, onLoad :function) :Object3D` — Parses the node objects from the given JSON.
- `.parseMaterials( json :Object, textures :Object.<string,Texture>) : Object.<string,NodeMaterial>` — Parses the node objects from the given JSON and textures.
- `.parseNodes( json :Array.<Object>, textures :Object.<string,Texture>) : Object.<string,Node>` — Parses the node objects from the given JSON and textures.
- `.setNodeMaterials( value :Object.<string, NodeMaterial.constructor>) :NodeObjectLoader` — Defines the dictionary of node material types.
- `.setNodes( value :Object.<string, Node.constructor>) :NodeObjectLoader` — Defines the dictionary of node types.

## Source