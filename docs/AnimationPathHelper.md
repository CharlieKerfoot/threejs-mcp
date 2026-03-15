# AnimationPathHelper
Extends: EventDispatcher→Object3D→

Visualizes the motion path of an animated object based on position keyframes
from an AnimationClip.

## Constructor
`newAnimationPathHelper( root :Object3D, clip :AnimationClip, object :Object3D, options :Object)`
Constructs a new animation path helper.

## Import

## Properties
- `.clip :AnimationClip` — The animation clip containing position keyframes.
- `.divisions : number` — Number of samples for smooth path interpolation. Default is 100 .
- `.isAnimationPathHelper : boolean` — This flag can be used for type testing. Default is true .
- `.line :Line` — The line representing the animation path.
- `.object :Object3D` — The object whose path is being visualized.
- `.points :Points| null` — Points marking keyframe positions.
- `.root :Object3D` — The root object containing the animation clips.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance.
- `.setColor( color :number |Color| string)` — Sets the path line color.
- `.setMarkerColor( color :number |Color| string)` — Sets the keyframe marker color.
- `.updateMatrixWorld( force :boolean)` — Updates the helper's transform to match the object's parent.

## Source