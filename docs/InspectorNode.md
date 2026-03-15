# InspectorNode
Extends: EventDispatcher→Node→

InspectorNode is a wrapper node that allows inspection of node values during rendering.
It can be used to debug or analyze node outputs in the rendering pipeline.

## Constructor
`newInspectorNode( node :Node, name :string, callback :function | null)`
Creates an InspectorNode.

## Properties
- `.type` — Returns the type of the node.

## Methods
- `.getName() : string` — Returns the name of the inspector node.
- `.getNodeType( builder :NodeBuilder) : string` — Returns the type of the wrapped node.
- `.setup( builder :NodeBuilder) :Node` — Sets up the inspector node.
- `.update( frame :NodeFrame)` — Updates the inspector node, allowing inspection of the wrapped node.

## Source