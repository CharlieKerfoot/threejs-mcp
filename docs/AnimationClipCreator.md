# AnimationClipCreator

A utility class with factory methods for creating basic animation clips.

## Import

## Static Methods
- `.CreateMaterialColorAnimation( duration :number, colors :Array.<Color>) :AnimationClip` — Creates an animation clip that animates the color property of a 3D object's
material.
- `.CreatePulsationAnimation( duration :number, pulseScale :number) :AnimationClip` — Creates an animation clip that scales a 3D object in a pulse pattern
in the given period.
- `.CreateRotationAnimation( period :number, axis :'x' | 'y' | 'z') :AnimationClip` — Creates an animation clip that rotates a 3D object 360 degrees
in the given period of time around the given axis.
- `.CreateScaleAxisAnimation( period :number, axis :'x' | 'y' | 'z') :AnimationClip` — Creates an animation clip that scales a 3D object from 0 to 1 in the given period of time along the given axis.
- `.CreateShakeAnimation( duration :number, shakeScale :Vector3) :AnimationClip` — Creates an animation clip that translates a 3D object in a shake pattern
in the given period.
- `.CreateVisibilityAnimation( duration :number) :AnimationClip` — Creates an animation clip that toggles the visibility of a 3D object.

## Source