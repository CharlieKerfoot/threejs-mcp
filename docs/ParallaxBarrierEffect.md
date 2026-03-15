# ParallaxBarrierEffect

A class that creates an parallax barrier effect. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use ParallaxBarrierPassNode .

## Constructor
`newParallaxBarrierEffect( renderer :WebGLRenderer)`
Constructs a new parallax barrier effect.

## Import

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the effect is no longer required.
- `.render( scene :Object3D, camera :Camera)` — When using this effect, this method should be called instead of the
default WebGLRenderer#render .
- `.setSize( width :number, height :number)` — Resizes the effect.

## Source