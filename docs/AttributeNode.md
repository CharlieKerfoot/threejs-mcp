# AttributeNode
Extends: EventDispatcher→Node→

Base class for representing shader attributes as nodes.

## Constructor
`newAttributeNode( attributeName :string, nodeType :string)`
Constructs a new attribute node.

## Properties
- `.global : boolean` — AttributeNode sets this property to true by default. Default is true .

## Methods
- `.getAttributeName( builder :NodeBuilder) : string` — Returns the attribute name of this node. The method can be
overwritten in derived classes if the final name must be computed
analytically.
- `.setAttributeName( attributeName :string) :AttributeNode` — Sets the attribute name to the given value. The method can be
overwritten in derived classes if the final name must be computed
analytically.

## Source