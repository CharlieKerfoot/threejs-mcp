# ViewportDepthNode
Extends: EventDispatcher→Node→

This node offers a collection of features in context of the depth logic in the fragment shader.
Depending on ViewportDepthNode#scope , it can be used to define a depth value for the current
fragment or for depth evaluation purposes.

## Constructor
`newViewportDepthNode( scope :'depth' | 'depthBase' | 'linearDepth', valueNode :Node)`
Constructs a new viewport depth node.

## Properties
- `.isViewportDepthNode : boolean` — This flag can be used for type testing. Default is true .
- `.scope : 'depth' | 'depthBase' | 'linearDepth'` — The node behaves differently depending on which scope is selected. ViewportDepthNode.DEPTH_BASE : Allows to define a value for the current fragment's depth. ViewportDepthNode.DEPTH : Represents the...
- `.valueNode :Node` — Can be used to define a custom depth value.
The property is ignored in the ViewportDepthNode.DEPTH scope. Default is null .

## Source