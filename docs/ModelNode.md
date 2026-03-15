# ModelNode
Extends: EventDispatcher→Node→Object3DNode→

This type of node is a specialized version of Object3DNode with larger set of model related metrics. Unlike Object3DNode , ModelNode extracts the reference to the 3D object from the
current node frame state.

## Constructor
`newModelNode( scope :'position' | 'viewPosition' | 'direction' | 'scale' | 'worldMatrix')`
Constructs a new object model node.

## Methods
- `.update( frame :NodeFrame)` — Extracts the model reference from the frame state and then
updates the uniform value depending on the scope.

## Source