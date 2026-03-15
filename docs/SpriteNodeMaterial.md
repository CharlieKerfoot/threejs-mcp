# SpriteNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of SpriteMaterial .

## Constructor
`newSpriteNodeMaterial( parameters :Object)`
Constructs a new sprite node material.

## Properties
- `.isSpriteNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.positionNode :Node.<vec2>` — This property makes it possible to define the position of the sprite with a
node. That can be useful when the material is used with instanced rendering
and node data are defined with an instanced a...
- `.rotationNode :Node.<float>` — The rotation of sprite materials is by default inferred from the rotation ,
property. This node property allows to overwrite the default and define
the rotation with a node instead. If you don't wa...
- `.scaleNode :Node.<vec2>` — This node property provides an additional way to scale sprites next to Object3D.scale . The scale transformation based in Object3D.scale is multiplied with the scale value of this node in the verte...
- `.sizeAttenuation : boolean` — Whether to use size attenuation or not. Default is true .
- `.transparent : boolean` — In Sprites, the transparent property is enabled by default. Default is true .

## Methods
- `.setupPositionView( builder :NodeBuilder) :Node.<vec3>` — Setups the position node in view space. This method implements
the sprite specific vertex shader.

## Source