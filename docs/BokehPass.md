# BokehPass
Extends: Pass→

Pass for creating depth of field (DOF) effect.

## Constructor
`newBokehPass( scene :Scene, camera :Camera, params :BokehPass~Options)`
Constructs a new Bokeh pass.

## Import

## Properties
- `.camera :Camera` — The camera.
- `.materialBokeh :ShaderMaterial` — The pass bokeh material.
- `.scene :Scene` — The scene to render the DOF for.
- `.uniforms : Object` — The pass uniforms.  Use this object if you want to update the focus , aperture or maxblur values at runtime. pass.uniforms.focus.value = focus;
pass.uniforms.aperture.value = aperture;
pass.uniform...

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the Bokeh pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Type Definitions
- `.Options` — Constructor options of BokehPass .

## Source