# AnimationUtils

A class with various methods to assist with animations.

## Static Methods
- `.convertArray( array :TypedArray | Array, type :TypedArray.constructor) : TypedArray` — Converts an array to a specific type
- `.flattenJSON( jsonKeys :Array.<number>, times :Array.<number>, values :Array.<number>, valuePropertyName :string)` — Used for parsing AOS keyframe formats.
- `.getKeyframeOrder( times :Array.<number>) : Array.<number>` — Returns an array by which times and values can be sorted.
- `.isTypedArray( object :any) : boolean` — Returns true if the given object is a typed array.
- `.makeClipAdditive( targetClip :AnimationClip, referenceFrame :number, referenceClip :AnimationClip, fps :number) :AnimationClip` — Converts the keyframes of the given animation clip to an additive format.
- `.sortedArray( values :Array.<number>, stride :number, order :Array.<number>) : Array.<number>` — Sorts the given array by the previously computed order via getKeyframeOrder() .
- `.subclip( sourceClip :AnimationClip, name :string, startFrame :number, endFrame :number, fps :number) :AnimationClip` — Creates a new clip, containing only the segment of the original clip between the given frames.

## Source