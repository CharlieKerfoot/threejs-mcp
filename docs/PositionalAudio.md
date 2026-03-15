# PositionalAudio
Extends: EventDispatcher→Object3D→Audio→

Represents a positional audio object.

## Constructor
`newPositionalAudio( listener :AudioListener)`
Constructs a positional audio.

## Properties
- `.panner : PannerNode` — The panner node represents the location, direction, and behavior of an audio
source in 3D space.

## Methods
- `.getDistanceModel() : 'linear' | 'inverse' | 'exponential'` — Returns the current distance model.
- `.getMaxDistance() : number` — Returns the current max distance.
- `.getRefDistance() : number` — Returns the current reference distance.
- `.getRolloffFactor() : number` — Returns the current rolloff factor.
- `.setDirectionalCone( coneInnerAngle :number, coneOuterAngle :number, coneOuterGain :number) :PositionalAudio` — Sets the directional cone in which the audio can be listened.
- `.setDistanceModel( value :'linear' | 'inverse' | 'exponential') :PositionalAudio` — Defines which algorithm to use to reduce the volume of the audio source
as it moves away from the listener. Read the spec for more details.
- `.setMaxDistance( value :number) :PositionalAudio` — Defines the maximum distance between the audio source and the listener,
after which the volume is not reduced any further. This value is used only by the linear distance model.
- `.setRefDistance( value :number) :PositionalAudio` — Defines the reference distance for reducing volume as the audio source moves
further from the listener – i.e. the distance at which the volume reduction
starts taking effect.
- `.setRolloffFactor( value :number) :PositionalAudio` — Defines how quickly the volume is reduced as the source moves away from the listener.

## Source