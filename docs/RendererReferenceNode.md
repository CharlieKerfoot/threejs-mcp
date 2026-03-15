# RendererReferenceNode
Extends: EventDispatcher→Node→ReferenceBaseNode→

This node is a special type of reference node which is intended
for linking renderer properties with node values. When changing renderer.toneMappingExposure , the node value of exposureNode will
automatically be updated.

## Constructor
`newRendererReferenceNode( property :string, inputType :string, renderer :Renderer)`
Constructs a new renderer reference node.

## Properties
- `.renderer :Renderer` — The renderer the property belongs to. When no renderer is set,
the node refers to the renderer of the current state. Default is null .

## Methods
- `.updateReference( state :NodeFrame|NodeBuilder) : Object` — Updates the reference based on the given state. The state is only evaluated RendererReferenceNode#renderer is not set.

## Source