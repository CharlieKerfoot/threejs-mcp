# StructTypeNode
Extends: EventDispatcher→Node→

Represents a struct type node in the node-based system.
This class is used to define and manage the layout and types of struct members.
It extends the base Node class and provides methods to get the length of the struct,
retrieve member types, and generate the struct type for a builder.

## Constructor
`newStructTypeNode( membersLayout :Object, name :string)`
Creates an instance of StructTypeNode.

## Properties
- `.isStructLayoutNode : boolean` — This flag can be used for type testing. Default is true .
- `.membersLayout : Array.<{name: string, type: string, atomic: boolean}>` — The layout of the members for the struct
- `.name : string` — The name of the struct. Default is null .

## Methods
- `.getLength() : number` — Returns the length of the struct.
The length is calculated by summing the lengths of the struct's members.

## Source