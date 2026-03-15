# GTAOPass
Extends: Pass→

A pass for an GTAO effect. GTAOPass provides better quality than SSAOPass but is also more expensive.

## Constructor
`newGTAOPass( scene :Scene, camera :Camera, width :number, height :number, parameters :Object, aoParameters :Object, pdParameters :Object)`
Constructs a new GTAO pass.

## Import

## Properties
- `.blendIntensity : number` — The AO blend intensity. Default is 1 .
- `.camera :Camera` — The camera.
- `.clear : boolean` — Overwritten to perform a clear operation by default. Default is true .
- `.gtaoMap :Texture` — A texture holding the computed AO.
- `.height : number` — The height of the effect. Default is 512 .
- `.output : number` — The output configuration. Default is 0 .
- `.pdRadiusExponent : number` — The Poisson Denoise radius exponent. Default is 2 .
- `.pdRings : number` — The number of Poisson Denoise rings. Default is 2 .
- `.pdSamples : number` — The Poisson Denoise sample count. Default is 16 .
- `.scene :Scene` — The scene to render the AO for.
- `.width : number` — The width of the effect. Default is 512 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the GTAO pass.
- `.setGBuffer( depthTexture :DepthTexture, normalTexture :DepthTexture)` — Configures the GBuffer of this pass. If no arguments are passed,
the pass creates an internal render target for holding depth
and normal data.
- `.setSceneClipBox( box :Box3)` — Configures the clip box of the GTAO shader with the given AABB.
- `.setSize( width :number, height :number)` — Sets the size of the pass.
- `.updateGtaoMaterial( parameters :Object)` — Updates the GTAO material from the given parameter object.
- `.updatePdMaterial( parameters :Object)` — Updates the Denoise material from the given parameter object.

## Source