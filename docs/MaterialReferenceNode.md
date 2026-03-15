# MaterialReferenceNode
Extends: EventDispatcher→Node→ReferenceNode→

This node is a special type of reference node which is intended
for linking material properties with node values. When changing material.opacity , the node value of opacityNode will
automatically be updated.

## Constructor
`newMaterialReferenceNode( property :string, inputType :string, material :Material)`
Constructs a new material reference node.

## Properties
- `.isMaterialReferenceNode : boolean` — This flag can be used for type testing. Default is true .
- `.material :Material` — The material the property belongs to. When no material is set,
the node refers to the material of the current rendered object. Default is null .

## Methods
- `.updateReference( state :NodeFrame|NodeBuilder) : Object` — Updates the reference based on the given state. The state is only evaluated MaterialReferenceNode#material is not set.

## Source