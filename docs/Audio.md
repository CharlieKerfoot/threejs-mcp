# Audio
Extends: EventDispatcher→Object3D→

Represents a non-positional ( global ) audio object. This and related audio modules make use of the Web Audio API .

## Constructor
`newAudio( listener :AudioListener)`
Constructs a new audio.

## Properties
- `.autoplay : boolean` — Whether to start playback automatically or not. Default is false .
- `.buffer : AudioBuffer` — A reference to an audio buffer. Defined via Audio#setBuffer . Default is null .
- `.context :AudioContext` — The audio context.
- `.detune : number` — Modify pitch, measured in cents. +/- 100 is a semitone.
+/- 1200 is an octave. Defined via Audio#setDetune . Default is 0 .
- `.duration : undefined | number` — Overrides the default duration of the audio. Default is undefined .
- `.filters : Array.<AudioNode>` — Can be used to apply a variety of low-order filters to create
more complex sound effects e.g. via BiquadFilterNode . The property is automatically set by Audio#setFilters .
- `.gain : GainNode` — The gain node used for volume control.
- `.hasPlaybackControl : boolean` — Indicates whether the audio playback can be controlled
with method like Audio#play or Audio#pause . This flag will be automatically set when audio sources are
defined. Default is true .
- `.isPlaying : boolean` — Indicates whether the audio is playing or not. This flag will be automatically set when using Audio#play , Audio#pause , Audio#stop . Default is false .
- `.listener :AudioListener` — The global audio listener.
- `.loop : boolean` — Whether the audio should loop or not. Defined via Audio#setLoop . Default is false .
- `.loopEnd : number` — Defines where in the audio buffer the replay should
stop, in seconds. Default is 0 .
- `.loopStart : number` — Defines where in the audio buffer the replay should
start, in seconds. Default is 0 .
- `.offset : number` — An offset to the time within the audio buffer the playback
should begin, in seconds. Default is 0 .
- `.playbackRate : number` — The playback speed. Defined via Audio#setPlaybackRate . Default is 1 .
- `.source : AudioNode` — Holds a reference to the current audio source. The property is automatically by one of the set*() methods. Default is null .
- `.sourceType : 'empty' | 'audioNode' | 'mediaNode' | 'mediaStreamNode' | 'buffer'` — Defines the source type. The property is automatically set by one of the set*() methods. Default is 'empty' .

## Methods
- `.connect() :Audio` — Connects to the audio source. This is used internally on
initialisation and when setting / removing filters.
- `.disconnect() :Audio| undefined` — Disconnects to the audio source. This is used internally on
initialisation and when setting / removing filters.
- `.getDetune() : number` — Returns the detuning of oscillation in cents.
- `.getFilter() : AudioNode | undefined` — Returns the first filter in the list of filters.
- `.getFilters() : Array.<AudioNode>` — Returns the current set filters.
- `.getLoop() : boolean` — Returns the loop flag. Can only be used with compatible audio sources that allow playback control.
- `.getOutput() : GainNode` — Returns the output audio node.
- `.getPlaybackRate() : number` — Returns the current playback rate.
- `.getVolume() : number` — Returns the volume.
- `.onEnded()` — Automatically called when playback finished.
- `.pause() :Audio| undefined` — Pauses the playback of the audio. Can only be used with compatible audio sources that allow playback control.
- `.play( delay :number) :Audio| undefined` — Starts the playback of the audio. Can only be used with compatible audio sources that allow playback control.
- `.setBuffer( audioBuffer :AudioBuffer) :Audio` — Sets the given audio buffer as the source of this instance. Audio#sourceType is set to buffer and Audio#hasPlaybackControl to true .
- `.setDetune( value :number) :Audio` — Defines the detuning of oscillation in cents.
- `.setFilter( filter :AudioNode) :Audio` — Applies a single filter node to the audio.
- `.setFilters( value :Array.<AudioNode>) :Audio` — Sets an array of filters and connects them with the audio source.
- `.setLoop( value :boolean) :Audio| undefined` — Sets the loop flag. Can only be used with compatible audio sources that allow playback control.
- `.setLoopEnd( value :number) :Audio` — Sets the loop end value which defines where in the audio buffer the replay should
stop, in seconds.
- `.setLoopStart( value :number) :Audio` — Sets the loop start value which defines where in the audio buffer the replay should
start, in seconds.
- `.setMediaElementSource( mediaElement :HTMLMediaElement) :Audio` — Sets the given media element as the source of this instance. Audio#sourceType is set to mediaNode and Audio#hasPlaybackControl to false .
- `.setMediaStreamSource( mediaStream :MediaStream) :Audio` — Sets the given media stream as the source of this instance. Audio#sourceType is set to mediaStreamNode and Audio#hasPlaybackControl to false .
- `.setNodeSource( audioNode :AudioNode) :Audio` — Sets the given audio node as the source of this instance. Audio#sourceType is set to audioNode and Audio#hasPlaybackControl to false .
- `.setPlaybackRate( value :number) :Audio| undefined` — Sets the playback rate. Can only be used with compatible audio sources that allow playback control.
- `.setVolume( value :number) :Audio` — Sets the volume.
- `.stop( delay :number) :Audio| undefined` — Stops the playback of the audio. Can only be used with compatible audio sources that allow playback control.

## Source