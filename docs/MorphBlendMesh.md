# MorphBlendMesh
Extends: EventDispatcher→Object3D→Mesh→

A special type of an animated mesh with a more advanced interface
for animation playback. Unlike MorphAnimMesh . It allows to
playback more than one morph animation at the same time but without
fading options.

## Constructor
`newMorphBlendMesh( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new morph blend mesh.

## Import

## Properties
- `.animationsList : Array.<Object>` — A list of animations.
- `.animationsMap : Object.<string, Object>` — A dictionary of animations.

## Methods
- `.autoCreateAnimations( fps :number)` — Automatically creates animations based on the values in Mesh#morphTargetDictionary .
- `.createAnimation( name :string, start :number, end :number, fps :number)` — Creates a new animation.
- `.getAnimationDuration( name :string) : number` — Returns the duration for the defined animation.
- `.getAnimationTime( name :string) : number` — Returns the time for the defined animation.
- `.playAnimation( name :string)` — Plays the defined animation.
- `.setAnimationDirectionBackward( name :string)` — Sets the animation playback direction to "backward" for the
defined animation.
- `.setAnimationDirectionForward( name :string)` — Sets the animation playback direction to "forward" for the
defined animation.
- `.setAnimationDuration( name :string, duration :number)` — Sets the duration to the given value for the defined animation.
- `.setAnimationFPS( name :string, fps :number)` — Sets the FPS to the given value for the defined animation.
- `.setAnimationTime( name :string, time :number)` — Sets the time to the given value for the defined animation.
- `.setAnimationWeight( name :string, weight :number)` — Sets the weight to the given value for the defined animation.
- `.stopAnimation( name :string)` — Stops the defined animation.
- `.update( delta :number)` — Updates the animations of the mesh.

## Source