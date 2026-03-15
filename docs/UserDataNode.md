# UserDataNode
Extends: EventDispatcher→Node→ReferenceNode→

A special type of reference node that allows to link values in userData fields to node objects. Since UserDataNode is extended from ReferenceNode , the node value
will automatically be updated when the rotation user data field changes.

## Constructor
`newUserDataNode( property :string, inputType :string, userData :Object)`
Constructs a new user data node.

## Properties
- `.userData : Object` — A reference to the userData object. If not provided, the userData property of the 3D object that uses the node material is evaluated. Default is null .

## Methods
- `.updateReference( state :NodeFrame|NodeBuilder) : Object` — Overwritten to make sure ReferenceNode#reference points to the correct userData field.

## Source