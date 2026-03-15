# OutlineEffect

An outline effect for toon shaders. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use ToonOutlinePassNode .

## Constructor
`newOutlineEffect( renderer :WebGLRenderer, parameters :OutlineEffect~Options)`
Constructs a new outline effect.

## Import

## Methods
- `.render( scene :Object3D, camera :Camera)` — When using this effect, this method should be called instead of the
default WebGLRenderer#render .
- `.renderOutline( scene :Object3D, camera :Camera)` — This method can be used to render outlines in VR. const effect = new OutlineEffect( renderer );
let renderingOutline = false;
scene.onAfterRender = function () {
	if ( renderingOutline ) return;
	r...
- `.setSize( width :number, height :number)` — Resizes the effect.

## Type Definitions
- `.Options` — This type represents configuration settings of OutlineEffect .

## Source