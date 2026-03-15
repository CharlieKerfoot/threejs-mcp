# RenderTransitionPass
Extends: Pass→

A special type of render pass for implementing transition effects.
When active, the pass will transition from scene A to scene B.

## Constructor
`newRenderTransitionPass( sceneA :Scene, cameraA :Camera, sceneB :Scene, cameraB :Camera)`
Constructs a render transition pass.

## Import

## Properties
- `.cameraA :Camera` — The camera of the first scene.
- `.cameraB :Camera` — The camera of the second scene.
- `.material :ShaderMaterial` — The pass material.
- `.sceneA :Scene` — The first scene.
- `.sceneB :Scene` — The second scene.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the transition pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.
- `.setTexture( value :Texture)` — Sets the effect texture.
- `.setTextureThreshold( value :boolean | number)` — Sets the texture threshold. This value defines how strong the texture effects
the transition. Must be in the range [0,1] (0 means full effect, 1 means no effect).
- `.setTransition( value :boolean | number)` — Sets the transition factor. Must be in the range [0,1] .
This value determines to what degree both scenes are mixed.
- `.useTexture( value :boolean)` — Toggles the usage of a texture for the effect.

## Source