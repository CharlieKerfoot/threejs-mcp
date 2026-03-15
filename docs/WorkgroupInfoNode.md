# WorkgroupInfoNode
Extends: EventDispatcher→Node→

A node allowing the user to create a 'workgroup' scoped buffer within the
context of a compute shader. Typically, workgroup scoped buffers are
created to hold data that is transferred from a global storage scope into
a local workgroup scope. For invocations within a workgroup, data
access speeds on 'workgroup' scoped buffers can be significantly faster
than similar access operations on globally accessible storage buffers. This node can only be used with a WebGPU backend.

## Constructor
`newWorkgroupInfoNode( scope :string, bufferType :string, bufferCount :number)`
Constructs a new buffer scoped to type scope.

## Properties
- `.bufferCount : number` — The buffer count. Default is 0 .
- `.bufferType : string` — The buffer type.
- `.elementType : string` — The data type of the array buffer.
- `.isWorkgroupInfoNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the workgroup scoped buffer. Default is '' .
- `.scope : string` — TODO.

## Methods
- `.element( indexNode :IndexNode) :WorkgroupInfoElementNode` — This method can be used to access elements via an index node.
- `.getElementType() : string` — The data type of the array buffer.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation since the input type
is inferred from the scope.
- `.label( name :string) :WorkgroupInfoNode` — Sets the name/label of this node.
- `.setName( name :string) :WorkgroupInfoNode` — Sets the name of this node.
- `.setScope( scope :string) :WorkgroupInfoNode` — Sets the scope of this node.

## Source