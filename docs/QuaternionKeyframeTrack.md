# QuaternionKeyframeTrack
Extends: KeyframeTrack→

A track for Quaternion keyframe values.

## Constructor
`newQuaternionKeyframeTrack( name :string, times :Array.<number>, values :Array.<number>, interpolation :InterpolateLinear|InterpolateDiscrete|InterpolateSmooth)`
Constructs a new Quaternion keyframe track.

## Properties
- `.ValueTypeName : string` — The value type name. Default is 'quaternion' .

## Methods
- `.InterpolantFactoryMethodLinear( result :TypedArray) :QuaternionLinearInterpolant` — Overwritten so the method returns Quaternion based interpolant.

## Source