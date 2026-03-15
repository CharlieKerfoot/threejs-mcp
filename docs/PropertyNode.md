# PropertyNode
Extends: EventDispatcher→Node→

This class represents a shader property. It can be used
to explicitly define a property and assign a value to it. PropertyNode is used by the engine to predefined common material properties
for TSL code.

## Constructor
`newPropertyNode( nodeType :string, name :string, varying :boolean)`
Constructs a new property node.

## Properties
- `.global : boolean` — This flag is used for global cache. Default is true .
- `.isPropertyNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the property in the shader. If no name is defined,
the node system auto-generates one. Default is null .
- `.varying : boolean` — Whether this property is a varying or not. Default is false .

## Source