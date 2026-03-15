# PassNode
Extends: EventDispatcher→Node→TempNode→

Represents a render pass (sometimes called beauty pass) in context of post processing.
This pass produces a render for the given scene and camera and can provide multiple outputs
via MRT for further processing.

## Constructor
`newPassNode( scope :'color' | 'depth', scene :Scene, camera :Camera, options :Object)`
Constructs a new pass node.

## Properties
- `.camera :Camera` — A reference to the camera.
- `.contextNode :ContextNode| null` — An optional global context for the pass.
- `.global : boolean` — This flag is used for global cache. Default is true .
- `.isPassNode : boolean` — This flag can be used for type testing. Default is true .
- `.opaque : boolean` — Whether the pass is opaque. Default is true .
- `.options : Object` — Options for the internal render target.
- `.overrideMaterial :Material| null` — An optional override material for the pass.
- `.renderTarget :RenderTarget` — The pass's render target.
- `.scene :Scene` — A reference to the scene.
- `.scope : 'color' | 'depth'` — The scope of the pass. The scope determines whether the node outputs color or depth.
- `.transparent : boolean` — Whether the pass is transparent. Default is false .
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.FRAME since the node renders the
scene once per frame in its PassNode#updateBefore method. Default is 'frame' .
- `.COLOR : 'color'`
- `.DEPTH : 'depth'`

## Methods
- `.compileAsync( renderer :Renderer) : Promise` — Precompiles the pass. Note that this method must be called after the pass configuration is complete.
So calls like setMRT() and getTextureNode() must proceed the precompilation.
- `.dispose()` — Frees internal resources. Should be called when the node is no longer in use.
- `.getLayers() :Layers` — Gets the current layer configuration of the pass.
- `.getLinearDepthNode( name :string) :Node` — Returns a linear depth node of this pass.
- `.getMRT() :MRTNode` — Returns the current MRT node.
- `.getPreviousTexture( name :string) :Texture` — Returns the texture holding the data of the previous frame for the given output name.
- `.getPreviousTextureNode( name :string) :TextureNode` — Returns the previous texture node for the given output name.
- `.getResolution() : number` — Gets the current resolution of the pass.
- `.getResolutionScale() : number` — Gets the current resolution scale of the pass.
- `.getTexture( name :string) :Texture` — Returns the texture for the given output name.
- `.getTextureNode( name :string) :TextureNode` — Returns the texture node for the given output name.
- `.getViewZNode( name :string) :Node` — Returns a viewZ node of this pass.
- `.setLayers( layers :Layers) :PassNode` — Sets the layer configuration that should be used when rendering the pass.
- `.setMRT( mrt :MRTNode) :PassNode` — Sets the given MRT node to setup MRT for this pass.
- `.setPixelRatio( pixelRatio :number)` — Sets the pixel ratio the pass's render target and updates the size.
- `.setResolution( resolution :number) :PassNode` — Sets the resolution for the pass.
The resolution is a factor that is multiplied with the renderer's width and height.
- `.setResolutionScale( resolutionScale :number) :PassNode` — Sets the resolution scale for the pass.
The resolution scale is a factor that is multiplied with the renderer's width and height.
- `.setScissor( x :number |Vector4, y :number, width :number, height :number)` — This method allows to define the pass's scissor rectangle. By default, the scissor rectangle is kept
in sync with the pass's dimensions. To reverse the process and use auto-sizing again, call the m...
- `.setSize( width :number, height :number)` — Sets the size of the pass's render target. Honors the pixel ratio.
- `.setViewport( x :number |Vector4, y :number, width :number, height :number)` — This method allows to define the pass's viewport. By default, the viewport is kept in sync
with the pass's dimensions. To reverse the process and use auto-sizing again, call the method
with null as...
- `.toggleTexture( name :string)` — Switches current and previous textures for the given output name.

## Source