# AnaglyphEffect

A class that creates an anaglyph effect using physically-correct
off-axis stereo projection. This implementation uses CameraUtils.frameCorners() to align stereo
camera frustums to a virtual screen plane, providing accurate depth
perception with zero parallax at the plane distance. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use AnaglyphPassNode .

## Constructor
`newAnaglyphEffect( renderer :WebGLRenderer, width :number, height :number)`
Constructs a new anaglyph effect.

## Import

## Properties
- `.eyeSep : number` — The interpupillary distance (eye separation) in world units.
Typical human IPD is 0.064 meters (64mm). Default is 0.064 .
- `.planeDistance : number` — The distance in world units from the viewer to the virtual
screen plane where zero parallax (screen depth) occurs.
Objects at this distance appear at the screen surface.
Objects closer appear in fr...

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.render( scene :Object3D, camera :Camera)` — When using this effect, this method should be called instead of the
default WebGLRenderer#render .
- `.setSize( width :number, height :number)` — Resizes the effect.

## Source