# MorphNode
Extends: EventDispatcher→Node→

This node implements the vertex transformation shader logic which is required
for morph target animation.

## Constructor
`newMorphNode( mesh :Mesh)`
Constructs a new morph node.

## Properties
- `.mesh :Mesh` — The mesh holding the morph targets.
- `.morphBaseInfluence :UniformNode.<float>` — A uniform node which represents the morph base influence value.
- `.updateType : string` — The update type overwritten since morph nodes are updated per object.

## Methods
- `.setup( builder :NodeBuilder)` — Setups the morph node by assigning the transformed vertex data to predefined node variables.
- `.update( frame :NodeFrame)` — Updates the state of the morphed mesh by updating the base influence.

## Source