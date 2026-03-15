# TransitionNode
Extends: EventDispatcher→Node→TempNode→

Post processing node for creating a transition effect between scenes.

## Constructor
`newTransitionNode( textureNodeA :TextureNode, textureNodeB :TextureNode, mixTextureNode :TextureNode, mixRatioNode :Node.<float>, thresholdNode :Node.<float>, useTextureNode :Node.<float>)`
Constructs a new transition node.

## Import

## Properties
- `.mixRatioNode :Node.<float>` — The interpolation factor that controls the mix.
- `.mixTextureNode :TextureNode` — A texture that defines how the transition effect should look like.
- `.textureNodeA :TextureNode` — A texture node that represents the beauty pass of the first scene.
- `.textureNodeB :TextureNode` — A texture node that represents the beauty pass of the second scene.
- `.thresholdNode :Node.<float>` — Can be used to tweak the linear interpolation.
- `.useTextureNode :Node.<float>` — Whether mixTextureNode should influence the transition or not.

## Methods
- `.setup( builder :NodeBuilder) : ShaderCallNodeInternal` — This method is used to setup the effect's TSL code.

## Source