# ReferenceNode
Extends: EventDispatcher→Node→

This type of node establishes a reference to a property of another object.
In this way, the value of the node is automatically linked to the value of
referenced object. Reference nodes internally represent the linked value
as a uniform.

## Constructor
`newReferenceNode( property :string, uniformType :string, object :Object, count :number)`
Constructs a new reference node.

## Properties
- `.count : number` — When the linked property is an array, this parameter defines its length. Default is null .
- `.group :UniformGroupNode` — The uniform group of the internal uniform. Default is null .
- `.name : string` — An optional label of the internal uniform node. Default is null .
- `.node :UniformNode` — The uniform node that holds the value of the reference node. Default is null .
- `.object : Object` — The object the property belongs to. Default is null .
- `.properties : Array.<string>` — The property name might have dots so nested properties can be referred.
The hierarchy of the names is stored inside this array.
- `.property : string` — The name of the property the node refers to.
- `.reference : Object` — Points to the current referred object. This property exists next to ReferenceNode#object since the final reference might be updated from calling code. Default is null .
- `.uniformType : string` — The uniform type that should be used to represent the property value.
- `.updateType : string` — Overwritten since reference nodes are updated per object. Default is 'object' .

## Methods
- `.element( indexNode :IndexNode) :ReferenceElementNode` — When the referred property is array-like, this method can be used
to access elements via an index node.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from
the type of the reference node.
- `.getValueFromReference( object :Object) :any` — Returns the property value from the given referred object.
- `.label( name :string) :ReferenceNode` — Sets the label for the internal uniform.
- `.setGroup( group :UniformGroupNode) :ReferenceNode` — Sets the uniform group for this reference node.
- `.setName( name :string) :ReferenceNode` — Sets the name for the internal uniform.
- `.setNodeType( uniformType :string)` — Sets the node type which automatically defines the internal
uniform type.
- `.setup( builder :NodeBuilder) :UniformNode` — The output of the reference node is the internal uniform node.
- `.update( frame :NodeFrame)` — Overwritten to update the internal uniform value.
- `.updateReference( state :NodeFrame|NodeBuilder) : Object` — Allows to update the reference based on the given state. The state is only
evaluated ReferenceNode#object is not set.
- `.updateValue()` — Retrieves the value from the referred object property and uses it
to updated the internal uniform.

## Source