# AnimationClip

A reusable set of keyframe tracks which represent an animation.

## Constructor
`newAnimationClip( name :string, duration :number, tracks :Array.<KeyframeTrack>, blendMode :NormalAnimationBlendMode|AdditiveAnimationBlendMode)`
Constructs a new animation clip. Note: Instead of instantiating an AnimationClip directly with the constructor, you can
use the static interface of this class for creating clips. In most cases though, animation clips
will automatically be created by loaders when importing animated 3D assets.

## Properties
- `.blendMode :NormalAnimationBlendMode|AdditiveAnimationBlendMode` — Defines how the animation is blended/combined when two or more animations
are simultaneously played.
- `.duration : number` — The clip's duration in seconds.
- `.name : string` — The clip's name.
- `.tracks : Array.<KeyframeTrack>` — An array of keyframe tracks.
- `.userData : Object` — An object that can be used to store custom data about the animation clip.
It should not hold references to functions as these will not be cloned.
- `.uuid : string` — The UUID of the animation clip.

## Methods
- `.clone() :AnimationClip` — Returns a new animation clip with copied values from this instance.
- `.optimize() :AnimationClip` — Optimizes each track by removing equivalent sequential keys (which are
common in morph target sequences).
- `.resetDuration() :AnimationClip` — Sets the duration of this clip to the duration of its longest keyframe track.
- `.toJSON() : Object` — Serializes this animation clip into JSON.
- `.trim() :AnimationClip` — Trims all tracks to the clip's duration.
- `.validate() : boolean` — Performs minimal validation on each track in the clip. Returns true if all
tracks are valid.

## Static Methods
- `.CreateClipsFromMorphTargetSequences( morphTargets :Array.<Object>, fps :number, noLoop :boolean) : Array.<AnimationClip>` — Returns an array of new AnimationClips created from the morph target
sequences of a geometry, trying to sort morph target names into
animation-group-based patterns like "Walk_001, Walk_002, Run_001...
- `.CreateFromMorphTargetSequence( name :string, morphTargetSequence :Array.<Object>, fps :number, noLoop :boolean) :AnimationClip` — Returns a new animation clip from the passed morph targets array of a
geometry, taking a name and the number of frames per second. Note: The fps parameter is required, but the animation speed can b...
- `.findByName( objectOrClipArray :Array.<AnimationClip> |Object3D, name :string) :AnimationClip` — Searches for an animation clip by name, taking as its first parameter
either an array of clips, or a mesh or geometry that contains an
array named "animations" property.
- `.parse( json :Object) :AnimationClip` — Factory method for creating an animation clip from the given JSON.
- `.parseAnimation( animation :Object, bones :Array.<Bone>) :AnimationClip` — Parses the animation.hierarchy format and returns a new animation clip.
- `.toJSON( clip :AnimationClip) : Object` — Serializes the given animation clip into JSON.

## Source