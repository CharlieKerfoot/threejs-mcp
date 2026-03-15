# UniformNode
Extends: EventDispatcher→Node→InputNode→

Class for representing a uniform.

## Constructor
`newUniformNode( value :any, nodeType :string)`
Constructs a new uniform node.

## Properties
- `.groupNode :UniformGroupNode` — The uniform group of this uniform. By default, uniforms are
managed per object but they might belong to a shared group
which is updated per frame or render call.
- `.isUniformNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name or label of the uniform. Default is '' .

## Methods
- `.getGroup() :UniformGroupNode` — Returns the UniformNode#groupNode .
- `.getUniformHash( builder :NodeBuilder) : string` — By default, this method returns the result of Node#getHash but derived
classes might overwrite this method with a different implementation.
- `.label( name :string) :UniformNode` — Sets the UniformNode#name property.
- `.setGroup( group :UniformGroupNode) :UniformNode` — Sets the UniformNode#groupNode property.
- `.setName( name :string) :UniformNode` — Sets the UniformNode#name property.

## Source