# FogExp2

This class can be used to define an exponential squared fog,
which gives a clear view near the camera and a faster than exponentially
densening fog farther from the camera.

## Constructor
`newFogExp2( color :number |Color, density :number)`
Constructs a new fog.

## Properties
- `.color :Color` — The fog's color.
- `.density : number` — Defines how fast the fog will grow dense. Default is 0.00025 .
- `.isFogExp2 : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the fog.

## Methods
- `.clone() :FogExp2` — Returns a new fog with copied values from this instance.
- `.toJSON( meta :Object | string) : Object` — Serializes the fog into JSON.

## Source