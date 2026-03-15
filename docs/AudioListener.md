# AudioListener
Extends: EventDispatcher→Object3D→

The class represents a virtual listener of the all positional and non-positional audio effects
in the scene. A three.js application usually creates a single listener. It is a mandatory
constructor parameter for audios entities like Audio and PositionalAudio . In most cases, the listener object is a child of the camera. So the 3D transformation of the
camera represents the 3D transformation of the listener.

## Constructor
`newAudioListener()`
Constructs a new audio listener.

## Properties
- `.context :AudioContext` — The native audio context.
- `.filter : AudioNode` — An optional filter. Defined via AudioListener#setFilter . Default is null .
- `.gain : GainNode` — The gain node used for volume control.
- `.timeDelta : number` — Time delta values required for linearRampToValueAtTime() usage. Default is 0 .

## Methods
- `.getFilter() : AudioNode` — Returns the current set filter.
- `.getInput() : GainNode` — Returns the listener's input node. This method is used by other audio nodes to connect to this listener.
- `.getMasterVolume() : number` — Returns the applications master volume.
- `.removeFilter() :AudioListener` — Removes the current filter from this listener.
- `.setFilter( value :AudioNode) :AudioListener` — Sets the given filter to this listener.
- `.setMasterVolume( value :number) :AudioListener` — Sets the applications master volume. This volume setting affects
all audio nodes in the scene.

## Source