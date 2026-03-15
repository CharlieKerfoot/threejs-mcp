# MD2CharacterComplex

This class represents a management component for animated MD2
character assets. It provides a larger API compared to MD2Character .

## Constructor
`newMD2CharacterComplex()`
Constructs a new MD2 character.

## Import

## Properties
- `.angularSpeed : number` — The character's angular speed. Default is 2.5 .
- `.animationFPS : number` — The FPS Default is 6 .
- `.backAcceleration : number` — The character's back acceleration. Default is 600 .
- `.controls : Object` — The movement controls. Default is null .
- `.currentSkin :Texture` — The current skin. Default is undefined .
- `.frontAcceleration : number` — The character's front acceleration. Default is 600 .
- `.frontDeceleration : number` — The character's front deceleration. Default is 600 .
- `.maxReverseSpeed : number` — The character's maximum reverse speed. Default is - 275 .
- `.maxSpeed : number` — The character's maximum speed. Default is 275 .
- `.meshBody :Mesh` — The body mesh. Default is null .
- `.meshWeapon :Mesh` — The weapon mesh. Default is null .
- `.root :Object3D` — The root 3D object
- `.scale : number` — The mesh scale. Default is 1 .
- `.skinsBody : Array.<Texture>` — The body skins.
- `.skinsWeapon : Array.<Texture>` — The weapon skins.
- `.transitionFrames : number` — The transition frames. Default is 15 .
- `.weapons : Array.<Mesh>` — The weapon meshes.

## Methods
- `.enableShadows( enable :boolean)` — Toggles shadow casting and receiving on the character's meshes.
- `.loadParts( config :Object)` — Loads the character model for the given config.
- `.setAnimation( animationName :string)` — Sets the defined animation clip as the active animation.
- `.setPlaybackRate( rate :number)` — Sets the animation playback rate.
- `.setSkin( index :number)` — Sets the skin defined by the given skin index. This will result in a different texture
for the body mesh.
- `.setVisible( enable :boolean)` — Toggles visibility on the character's meshes.
- `.setWeapon( index :number)` — Sets the weapon defined by the given weapon index. This will result in a different weapon
hold by the character.
- `.setWireframe( wireframeEnabled :boolean)` — Sets the wireframe material flag.
- `.shareParts( original :MD2CharacterComplex)` — Shares certain resources from a different character model.
- `.updateAnimations( delta :number)` — Updates the animations of the mesh. Must be called inside the animation loop.
- `.updateBehaviors()` — Updates the animation state based on the control inputs.
- `.updateMovementModel( delta :number)` — Transforms the character model based on the control input.

## Source