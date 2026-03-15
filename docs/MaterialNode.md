# MaterialNode
Extends: EventDispatcher→Node→

This class should simplify the node access to material properties.
It internal uses reference nodes to make sure  changes to material
properties are automatically reflected to predefined TSL objects
like e.g. materialColor .

## Constructor
`newMaterialNode( scope :string)`
Constructs a new material node.

## Properties
- `.scope : string` — The scope defines what material property is referred by the node.

## Methods
- `.getCache( property :string, type :string) :MaterialReferenceNode` — Returns a cached reference node for the given property and type.
- `.getColor( property :string) :MaterialReferenceNode.<color>` — Returns a color-typed material reference node for the given property name.
- `.getFloat( property :string) :MaterialReferenceNode.<float>` — Returns a float-typed material reference node for the given property name.
- `.getTexture( property :string) :MaterialReferenceNode` — Returns a texture-typed material reference node for the given property name.
- `.setup( builder :NodeBuilder) :Node` — The node setup is done depending on the selected scope. Multiple material properties
might be grouped into a single node composition if they logically belong together.

## Source