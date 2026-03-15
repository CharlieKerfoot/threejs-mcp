# SSRPass
Extends: Pass→

A pass for a basic SSR effect.

## Constructor
`newSSRPass( options :SSRPass~Options)`
Constructs a new SSR pass.

## Import

## Properties
- `.blur : boolean` — Whether to blur reflections or not. Default is true .
- `.bouncing : boolean` — Whether bouncing is enabled or not. Default is false .
- `.camera :Camera` — The camera.
- `.clear : boolean` — Overwritten to perform a clear operation by default. Default is true .
- `.distanceAttenuation : boolean` — Whether to use distance attenuation or not. Default is true .
- `.fresnel : boolean` — Whether to use fresnel or not. Default is true .
- `.groundReflector :ReflectorForSSRPass` — The ground reflector. Default is 0 .
- `.height : number` — The height of the effect. Default is 512 .
- `.infiniteThick : boolean` — Whether to use infinite thickness or not. Default is false .
- `.maxDistance : number` — Controls how far a fragment can reflect. Default is 180 .
- `.opacity : number` — The opacity. Default is 0.5 .
- `.output : number` — The output configuration. Default is 0 .
- `.renderer :WebGLRenderer` — The renderer.
- `.resolutionScale : number` — The resolution scale. Valid values are in the range [0,1] . 1 means best quality but also results in
more computational overhead. Setting to 0.5 means
the effect is computed in half-resolution. Def...
- `.scene :Scene` — The scene to render.
- `.selective : boolean` — Whether the pass is selective or not. Default is false .
- `.selects : Array.<Object3D>` — Which 3D objects should be affected by SSR. If not set, the entire scene is affected. Default is null .
- `.thickness : number` — Controls the cutoff between what counts as a
possible reflection hit and what does not. Default is .018 .
- `.width : number` — The width of the effect. Default is 512 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the SSR pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Type Definitions
- `.Options` — Constructor options of SSRPass .

## Source