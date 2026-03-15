# PointsNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→SpriteNodeMaterial→

Node material version of PointsMaterial . This material can be used in two ways: By rendering point primitives with Points . Since WebGPU only supports point primitives
with a pixel size of 1 , it's not possible to define a size. By rendering point primitives with Sprites. In this case, size is honored,
see PointsNodeMaterial#sizeNode . const instancedPoints = new THREE.Sprite( new THREE.PointsNodeMaterial( { positionNode: instancedBufferAttribute( positionAttribute ) } ) );

## Constructor
`newPointsNodeMaterial( parameters :Object)`
Constructs a new points node material.

## Properties
- `.alphaToCoverage : boolean` — Whether alpha to coverage should be used or not. Default is true .
- `.isPointsNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.sizeNode :Node.<vec2>` — This node property provides an additional way to set the point size. Note that WebGPU only supports point primitives with 1 pixel size. Consequently,
this node has no effect when the material is us...

## Source