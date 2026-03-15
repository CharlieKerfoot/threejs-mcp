# UniformGroupNode
Extends: EventDispatcher→Node→

This node can be used to group single instances of UniformNode and manage them as a uniform buffer. In most cases, the predefined nodes objectGroup , renderGroup and frameGroup will be used when defining the UniformNode#groupNode property. objectGroup : Uniform buffer per object. renderGroup : Shared uniform buffer, updated once per render call. frameGroup : Shared uniform buffer, updated once per frame.

## Constructor
`newUniformGroupNode( name :string, shared :boolean, order :number)`
Constructs a new uniform group node.

## Properties
- `.isUniformGroup : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the uniform group node.
- `.order : number` — Influences the internal sorting.
TODO: Add details when this property should be changed. Default is 1 .
- `.shared : boolean` — Whether this uniform group node is shared or not. Default is false .

## Source