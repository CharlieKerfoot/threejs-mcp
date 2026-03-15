# IsolateNode
Extends: EventDispatcher→Node→

This node can be used as a cache management component for another node.
Caching is in general used by default in NodeBuilder but this node
allows the usage of a shared parent cache during the build process.

## Constructor
`newIsolateNode( node :Node, parent :boolean)`
Constructs a new cache node.

## Properties
- `.isIsolateNode : boolean` — This flag can be used for type testing. Default is true .
- `.node :Node` — The node that should be cached.
- `.parent : boolean` — Whether this node refers to a shared parent cache or not. Default is true .

## Source