# BarrierNode
Extends: EventDispatcher→Node→

Represents a GPU control barrier that synchronizes compute operations within a given scope. This node can only be used with a WebGPU backend.

## Constructor
`newBarrierNode( scope :string)`
Constructs a new barrier node.

## Source