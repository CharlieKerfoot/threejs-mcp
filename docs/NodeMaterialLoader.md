# NodeMaterialLoader
Extends: Loader→MaterialLoader→

A special type of material loader for loading node materials.

## Constructor
`newNodeMaterialLoader( manager :LoadingManager)`
Constructs a new node material loader.

## Properties
- `.nodeMaterials : Object.<string, NodeMaterial.constructor>` — Represents a dictionary of node material types.
- `.nodes : Object.<string, Node.constructor>` — Represents a dictionary of node types.

## Methods
- `.createMaterialFromType( type :string) :Node` — Creates a node material from the given type.
- `.parse( json :Object) :NodeMaterial` — Parses the node material from the given JSON.
- `.setNodeMaterials( value :Object.<string, NodeMaterial.constructor>) :NodeLoader` — Defines the dictionary of node material types.
- `.setNodes( value :Object.<string, Node.constructor>) :NodeLoader` — Defines the dictionary of node types.

## Source