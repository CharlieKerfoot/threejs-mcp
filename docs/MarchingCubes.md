# MarchingCubes

A marching cubes implementation. Port of: http://webglsamples.org/blob/blob.html

## Constructor
`newMarchingCubes( resolution :number, material :Material, enableUvs :boolean, enableColors :boolean, maxPolyCount :number)`
Constructs a new marching cubes instance.

## Import

## Properties
- `.enableColors : boolean` — Whether colors should be animated or not. Default is false .
- `.enableUvs : boolean` — Whether texture coordinates should be animated or not. Default is false .
- `.isMarchingCubes : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.addBall( ballx :number, bally :number, ballz :number, strength :number, subtract :number, colors :Color)` — Adds a reciprocal ball (nice and blobby) that, to be fast, fades to zero after
a fixed distance, determined by strength and subtract.
- `.addPlaneX( strength :number, subtract :number)` — Adds a plane along the x-axis.
- `.addPlaneY( strength :number, subtract :number)` — Adds a plane along the y-axis.
- `.addPlaneZ( strength :number, subtract :number)` — Adds a plane along the z-axis.
- `.blur( intensity :number)` — Applies a blur with the given intensity.
- `.getCell( x :number, y :number, z :number) : number` — Returns the cell value for the given coordinates.
- `.reset()` — Resets the effect.
- `.setCell( x :number, y :number, z :number, value :number)` — Sets the cell value for the given coordinates.
- `.update()` — Updates the effect.

## Source