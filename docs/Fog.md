# Fog

This class can be used to define a linear fog that grows linearly denser
with the distance.

## Constructor
`newFog( color :number |Color, near :number, far :number)`
Constructs a new fog.

## Properties
- `.color :Color` — The fog's color.
- `.far : number` — The maximum distance at which fog stops being calculated and applied.
Objects that are more than far units away from the active camera won't
be affected by fog. Default is 1000 .
- `.isFog : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the fog.
- `.near : number` — The minimum distance to start applying fog. Objects that are less than near units from the active camera won't be affected by fog. Default is 1 .

## Methods
- `.clone() :Fog` — Returns a new fog with copied values from this instance.
- `.toJSON( meta :Object | string) : Object` — Serializes the fog into JSON.

## Source