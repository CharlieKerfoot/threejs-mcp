# ScreenNode
Extends: EventDispatcher→Node→

This node provides a collection of screen related metrics.
Depending on ScreenNode#scope , the nodes can represent
resolution or viewport data as well as fragment or uv coordinates.

## Constructor
`newScreenNode( scope :'coordinate' | 'viewport' | 'size' | 'uv' | 'dpr')`
Constructs a new screen node.

## Properties
- `.isViewportNode : boolean` — This flag can be used for type testing. Default is true .
- `.scope : 'coordinate' | 'viewport' | 'size' | 'uv' | 'dpr'` — The node represents different metric depending on which scope is selected. ScreenNode.COORDINATE : Window-relative coordinates of the current fragment according to WebGPU standards. ScreenNode.VIEW...

## Methods
- `.getNodeType() : 'float' | 'vec2' | 'vec4'` — This method is overwritten since the node type depends on the selected scope.
- `.getUpdateType() :NodeUpdateType` — This method is overwritten since the node's update type depends on the selected scope.
- `.update( frame :NodeFrame)` — ScreenNode implements Node#update to retrieve viewport and size information
from the current renderer.

## Source