# MemberNode
Extends: EventDispatcher→Node→

Base class for representing member access on an object-like
node data structures.

## Constructor
`newMemberNode( structNode :Node, property :string)`
Constructs a member node.

## Properties
- `.isMemberNode : boolean` — This flag can be used for type testing. Default is true .
- `.property :Node` — The property name.
- `.structNode :Node` — The struct node.

## Source