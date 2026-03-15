# KeyframeTrack

Represents a timed sequence of keyframes, which are composed of lists of
times and related values, and which are used to animate a specific property
of an object.

## Constructor
`newKeyframeTrack( name :string, times :Array.<number>, values :Array.<(number|string|boolean)>, interpolation :InterpolateLinear|InterpolateDiscrete|InterpolateSmooth|InterpolateBezier)`
Constructs a new keyframe track.

## Properties
- `.DefaultInterpolation :InterpolateLinear|InterpolateDiscrete|InterpolateSmooth|InterpolateBezier` — The default interpolation type of this keyframe track. Default is InterpolateLinear .
- `.TimeBufferType : TypedArray | Array` — The time buffer type of this keyframe track. Default is Float32Array.constructor .
- `.ValueBufferType : TypedArray | Array` — The value buffer type of this keyframe track. Default is Float32Array.constructor .
- `.ValueTypeName : string` — The value type name. Default is '' .
- `.name : string` — The track's name can refer to morph targets or bones or
possibly other values within an animated object. See PropertyBinding#parseTrackName
for the forms of strings that can be parsed for property ...
- `.times : Float32Array` — The keyframe times.
- `.values : Float32Array` — The keyframe values.

## Methods
- `.InterpolantFactoryMethodBezier( result :TypedArray) :BezierInterpolant` — Factory method for creating a new Bezier interpolant. The Bezier interpolant requires tangent data to be set via the settings property
on the track before creating the interpolant. The settings sho...
- `.InterpolantFactoryMethodDiscrete( result :TypedArray) :DiscreteInterpolant` — Factory method for creating a new discrete interpolant.
- `.InterpolantFactoryMethodLinear( result :TypedArray) :LinearInterpolant` — Factory method for creating a new linear interpolant.
- `.InterpolantFactoryMethodSmooth( result :TypedArray) :CubicInterpolant` — Factory method for creating a new smooth interpolant.
- `.clone() :KeyframeTrack` — Returns a new keyframe track with copied values from this instance.
- `.getInterpolation() :InterpolateLinear|InterpolateDiscrete|InterpolateSmooth|InterpolateBezier` — Returns the current interpolation type.
- `.getValueSize() : number` — Returns the value size.
- `.optimize() :KeyframeTrack` — Optimizes this keyframe track by removing equivalent sequential keys (which are
common in morph target sequences).
- `.scale( timeScale :number) :KeyframeTrack` — Scale all keyframe times by a factor (useful for frame - seconds conversions).
- `.setInterpolation( interpolation :InterpolateLinear|InterpolateDiscrete|InterpolateSmooth|InterpolateBezier) :KeyframeTrack` — Defines the interpolation factor method for this keyframe track.
- `.shift( timeOffset :number) :KeyframeTrack` — Moves all keyframes either forward or backward in time.
- `.trim( startTime :number, endTime :number) :KeyframeTrack` — Removes keyframes before and after animation without changing any values within the defined time range. Note: The method does not shift around keys to the start of the track time, because for inter...
- `.validate() : boolean` — Performs minimal validation on the keyframe track. Returns true if the values
are valid.

## Static Methods
- `.toJSON( track :KeyframeTrack) : Object` — Converts the keyframe track to JSON.

## Source