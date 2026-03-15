# MorphAnimMesh
Extends: EventDispatcher→Object3D→Mesh→

A special type of an animated mesh with a simple interface
for animation playback. It allows to playback just one animation
without any transitions or fading between animation changes.

## Constructor
`newMorphAnimMesh( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new morph anim mesh.

## Import

## Properties
- `.activeAction :AnimationAction` — The current active animation action. Default is null .
- `.mixer :AnimationMixer` — The internal animation mixer.

## Methods
- `.playAnimation( label :string, fps :number)` — Plays the defined animation clip. The implementation assumes the animation
clips are stored in Object3D#animations or the geometry.
- `.setDirectionBackward()` — Sets the animation playback direction to "backward".
- `.setDirectionForward()` — Sets the animation playback direction to "forward".
- `.updateAnimation( delta :number)` — Updates the animations of the mesh. Must be called inside the animation loop.

## Source