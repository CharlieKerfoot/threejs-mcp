# SplitNode
Extends: EventDispatcher→Node→

This module is part of the TSL core and usually not used in app level code. SplitNode represents a property access operation which means it is
used to implement any .xyzw , .rgba and stpq usage on node objects.
For example:

## Constructor
`newSplitNode( node :Node, components :string)`
Constructs a new split node.

## Properties
- `.components : string` — The components that should be accessed.
- `.isSplitNode : boolean` — This flag can be used for type testing. Default is true .
- `.node :Node` — The node that should be accessed.

## Methods
- `.getComponentType( builder :NodeBuilder) : string` — Returns the component type of the node's type.
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from requested components.
- `.getScope() :Node` — Returns the scope of the node.
- `.getVectorLength() : number` — Returns the vector length which is computed based on the requested components.

## Source