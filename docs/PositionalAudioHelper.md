# PositionalAudioHelper
Extends: EventDispatcher→Object3D→Line→

This helper displays the directional cone of a positional audio. PositionalAudioHelper must be added as a child of the positional audio.

## Constructor
`newPositionalAudioHelper( audio :PositionalAudio, range :number, divisionsInnerAngle :number, divisionsOuterAngle :number)`
Constructs a new positional audio helper.

## Import

## Properties
- `.audio :PositionalAudio` — The audio to visualize.
- `.divisionsInnerAngle : number` — The number of divisions of the inner part of the directional cone. Default is 16 .
- `.divisionsOuterAngle : number` — The number of divisions of the outer part of the directional cone. Default is 2 .
- `.range : number` — The range of the directional cone. Default is 1 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.update()` — Updates the helper. This method must be called whenever the directional cone
of the positional audio is changed.

## Source