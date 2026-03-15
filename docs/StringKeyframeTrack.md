# StringKeyframeTrack
Extends: KeyframeTrack→

A track for string keyframe values.

## Constructor
`newStringKeyframeTrack( name :string, times :Array.<number>, values :Array.<string>)`
Constructs a new string keyframe track. This keyframe track type has no interpolation parameter because the
interpolation is always discrete.

## Properties
- `.DefaultInterpolation :InterpolateLinear|InterpolateDiscrete|InterpolateSmooth` — The default interpolation type of this keyframe track. Default is InterpolateDiscrete .
- `.ValueBufferType : TypedArray | Array` — The value buffer type of this keyframe track. Default is Array.constructor .
- `.ValueTypeName : string` — The value type name. Default is 'string' .

## Source