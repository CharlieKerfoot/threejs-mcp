# AnimationAction

An instance of AnimationAction schedules the playback of an animation which is
stored in AnimationClip .

## Constructor
`newAnimationAction( mixer :AnimationMixer, clip :AnimationClip, localRoot :Object3D, blendMode :NormalAnimationBlendMode|AdditiveAnimationBlendMode)`
Constructs a new animation action.

## Properties
- `.blendMode :NormalAnimationBlendMode|AdditiveAnimationBlendMode` — Defines how the animation is blended/combined when two or more animations
are simultaneously played.
- `.clampWhenFinished : boolean` — If set to true the animation will automatically be paused on its last frame. If set to false, AnimationAction#enabled will automatically be switched
to false when the last loop of the action has fi...
- `.enabled : boolean` — If set to false , the action is disabled so it has no impact. When the action is re-enabled, the animation continues from its current
time (setting enabled to false doesn't reset the action). Defau...
- `.loop :LoopRepeat|LoopOnce|LoopPingPong` — The loop mode, set via AnimationAction#setLoop . Default is LoopRepeat .
- `.paused : boolean` — If set to true , the playback of the action is paused. Default is false .
- `.repetitions : number` — The number of repetitions of the performed clip over the course of this action.
Can be set via AnimationAction#setLoop . Setting this number has no effect if AnimationAction#loop is set to THREE:Lo...
- `.time : number` — The local time of this action (in seconds, starting with 0 ). The value gets clamped or wrapped to [0,clip.duration] (according to the
loop state). Default is Infinity .
- `.timeScale : number` — Scaling factor for the AnimationAction#time . A value of 0 causes the
animation to pause. Negative values cause the animation to play backwards. Default is 1 .
- `.weight : number` — The degree of influence of this action (in the interval [0, 1] ). Values
between 0 (no impact) and 1 (full impact) can be used to blend between
several actions. Default is 1 .
- `.zeroSlopeAtEnd : boolean` — Enables smooth interpolation without separate clips for start, loop and end. Default is true .
- `.zeroSlopeAtStart : boolean` — Enables smooth interpolation without separate clips for start, loop and end. Default is true .

## Methods
- `.crossFadeFrom( fadeOutAction :AnimationAction, duration :number, warp :boolean) :AnimationAction` — Causes this action to fade in and the given action to fade out,
within the passed time interval.
- `.crossFadeTo( fadeInAction :AnimationAction, duration :number, warp :boolean) :AnimationAction` — Causes this action to fade out and the given action to fade in,
within the passed time interval.
- `.fadeIn( duration :number) :AnimationAction` — Fades the animation in by increasing its weight gradually from 0 to 1 ,
within the passed time interval.
- `.fadeOut( duration :number) :AnimationAction` — Fades the animation out by decreasing its weight gradually from 1 to 0 ,
within the passed time interval.
- `.getClip() :AnimationClip` — Returns the animation clip of this animation action.
- `.getEffectiveTimeScale() : number` — Returns the effective time scale of this action.
- `.getEffectiveWeight() : number` — Returns the effective weight of this action.
- `.getMixer() :AnimationMixer` — Returns the animation mixer of this animation action.
- `.getRoot() :Object3D` — Returns the root object of this animation action.
- `.halt( duration :number) :AnimationAction` — Decelerates this animation's speed to 0 within the passed time interval.
- `.isRunning() : boolean` — Returns true if the animation is running.
- `.isScheduled() : boolean` — Returns true when AnimationAction#play has been called.
- `.play() :AnimationAction` — Starts the playback of the animation.
- `.reset() :AnimationAction` — Resets the playback of the animation.
- `.setDuration( duration :number) :AnimationAction` — Sets the duration for a single loop of this action.
- `.setEffectiveTimeScale( timeScale :number) :AnimationAction` — Sets the effective time scale of this action. An action has no effect and thus an effective time scale of zero when the
action is paused.
- `.setEffectiveWeight( weight :number) :AnimationAction` — Sets the effective weight of this action. An action has no effect and thus an effective weight of zero when the
action is disabled.
- `.setLoop( mode :LoopRepeat|LoopOnce|LoopPingPong, repetitions :number) :AnimationAction` — Configures the loop settings for this action.
- `.startAt( time :number) :AnimationAction` — Defines the time when the animation should start.
- `.stop() :AnimationAction` — Stops the playback of the animation.
- `.stopFading() :AnimationAction` — Stops any fading which is applied to this action.
- `.stopWarping() :AnimationAction` — Stops any scheduled warping which is applied to this action.
- `.syncWith( action :AnimationAction) :AnimationAction` — Synchronizes this action with the passed other action.
- `.warp( startTimeScale :number, endTimeScale :number, duration :number) :AnimationAction` — Changes the playback speed, within the passed time interval, by modifying AnimationAction#timeScale gradually from startTimeScale to endTimeScale .

## Source