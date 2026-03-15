# MD2Character

This class represents a management component for animated MD2
character assets.

## Constructor
`newMD2Character()`
Constructs a new MD2 character.

## Import

## Properties
- `.activeAnimationClipName : string` — The name of the active animation clip. Default is null .
- `.animationFPS : number` — The FPS Default is 6 .
- `.meshBody :Mesh` — The body mesh. Default is null .
- `.meshWeapon :Mesh` — The weapon mesh. Default is null .
- `.mixer :AnimationMixer` — The animation mixer. Default is null .
- `.root :Object3D` — The root 3D object
- `.scale : number` — The mesh scale. Default is 1 .
- `.skinsBody : Array.<Texture>` — The body skins.
- `.skinsWeapon : Array.<Texture>` — The weapon skins.
- `.weapons : Array.<Mesh>` — The weapon meshes.

## Methods
- `.loadParts( config :Object)` — Loads the character model for the given config.
- `.onLoadComplete()` — The onLoad callback function.
- `.setAnimation( clipName :string)` — Sets the defined animation clip as the active animation.
- `.setPlaybackRate( rate :number)` — Sets the animation playback rate.
- `.setSkin( index :number)` — Sets the skin defined by the given skin index. This will result in a different texture
for the body mesh.
- `.setWeapon( index :number)` — Sets the weapon defined by the given weapon index. This will result in a different weapon
hold by the character.
- `.setWireframe( wireframeEnabled :boolean)` — Sets the wireframe material flag.
- `.syncWeaponAnimation()` — Synchronizes the weapon with the body animation.
- `.update( delta :number)` — Updates the animations of the mesh. Must be called inside the animation loop.

## Source