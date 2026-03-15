# Object3DNode
Extends: EventDispatcher→Node→

This node can be used to access transformation related metrics of 3D objects.
Depending on the selected scope, a different metric is represented as a uniform
in the shader. The following scopes are supported: POSITION : The object's position in world space. VIEW_POSITION : The object's position in view/camera space. DIRECTION : The object's direction in world space. SCALE : The object's scale in world space. WORLD_MATRIX : The object's matrix in world space.

## Constructor
`newObject3DNode( scope :'position' | 'viewPosition' | 'direction' | 'scale' | 'worldMatrix', object3d :Object3D)`
Constructs a new object 3D node.

## Properties
- `.object3d :Object3D` — The 3D object. Default is null .
- `.scope : 'position' | 'viewPosition' | 'direction' | 'scale' | 'worldMatrix'` — The node reports a different type of transformation depending on the scope.
- `.uniformNode :UniformNode` — Holds the value of the node as a uniform.
- `.updateType : string` — Overwritten since this type of node is updated per object. Default is 'object' .

## Methods
- `.generate( builder :NodeBuilder) : string` — Generates the code snippet of the uniform node. The node type of the uniform
node also depends on the selected scope.
- `.getNodeType() : 'mat4' | 'vec3' | 'float'` — Overwritten since the node type is inferred from the scope.
- `.update( frame :NodeFrame)` — Updates the uniform value depending on the scope.

## Source