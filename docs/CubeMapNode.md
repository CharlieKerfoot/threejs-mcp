# CubeMapNode
Extends: EventDispatcher→Node→TempNode→

This node can be used to automatically convert environment maps in the
equirectangular format into the cube map format.

## Constructor
`newCubeMapNode( envNode :Node)`
Constructs a new cube map node.

## Properties
- `.envNode :Node` — The node representing the environment map.
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.RENDER since the node updates
the texture once per render in its CubeMapNode#updateBefore method. Default is 'render' .

## Source