# StereoEffect

A class that creates an stereo effect. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use StereoPassNode .

## Constructor
`newStereoEffect( renderer :WebGLRenderer)`
Constructs a new stereo effect.

## Import

## Methods
- `.render( scene :Object3D, camera :Camera)` — When using this effect, this method should be called instead of the
default WebGLRenderer#render .
- `.setEyeSeparation( eyeSep :number)` — Sets the given eye separation.
- `.setSize( width :number, height :number)` — Resizes the effect.

## Source