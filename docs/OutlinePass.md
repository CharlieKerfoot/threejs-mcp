# OutlinePass
Extends: Pass→

A pass for rendering outlines around selected objects.

## Constructor
`newOutlinePass( resolution :Vector2, scene :Scene, camera :Camera, selectedObjects :Array.<Object3D>)`
Constructs a new outline pass.

## Import

## Properties
- `.downSampleRatio : number` — The downsample ratio. The effect can be rendered in a much
lower resolution than the beauty pass. Default is 2 .
- `.edgeGlow : number` — Can be used for an animated glow/pulse effect. Default is 0 .
- `.edgeStrength : number` — The edge strength. Default is 3 .
- `.edgeThickness : number` — The edge thickness. Default is 1 .
- `.hiddenEdgeColor :Color` — The hidden edge color. Default is (0.1,0.04,0.02) .
- `.patternTexture :Texture` — Can be used to highlight selected 3D objects. Requires to set OutlinePass#usePatternTexture to true . Default is null .
- `.pulsePeriod : number` — The pulse period. Default is 0 .
- `.renderCamera : Object` — The camera.
- `.renderScene : Object` — The scene to render.
- `.resolution :Vector2` — The effect's resolution. Default is (256,256) .
- `.selectedObjects : Array.<Object3D>` — The selected 3D objects that should receive an outline.
- `.usePatternTexture : boolean` — Whether to use a pattern texture for to highlight selected
3D objects or not. Default is false .
- `.visibleEdgeColor :Color` — The visible edge color. Default is (1,1,1) .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the pass is no longer used in your app.
- `.render( renderer :WebGLRenderer, writeBuffer :WebGLRenderTarget, readBuffer :WebGLRenderTarget, deltaTime :number, maskActive :boolean)` — Performs the Outline pass.
- `.setSize( width :number, height :number)` — Sets the size of the pass.

## Source