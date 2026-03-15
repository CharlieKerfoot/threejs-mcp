# InspectorBase

## Constructor
`newInspectorBase()`
InspectorBase is the base class for all inspectors.

## Properties
- `.currentFrame : Object` — The current frame being processed.
- `.nodeFrame` — Returns the node frame for the current renderer.

## Methods
- `.begin()` — Called when a frame begins.
- `.beginCompute( uid :string, computeNode :ComputeNode)` — Called when a compute operation begins.
- `.beginRender( uid :string, scene :Scene, camera :Camera, renderTarget :WebGLRenderTarget)` — Called when a render operation begins.
- `.computeAsync( computeNode :ComputeNode, dispatchSizeOrCount :number | Array.<number>)` — When a compute operation is performed.
- `.copyFramebufferToTexture( framebufferTexture :Texture)` — Called when a framebuffer copy operation is performed.
- `.copyTextureToTexture( srcTexture :Texture, dstTexture :Texture)` — Called when a texture copy operation is performed.
- `.finish()` — Called when a frame ends.
- `.finishCompute( uid :string, computeNode :ComputeNode)` — Called when a compute operation ends.
- `.finishRender( uid :string)` — Called when an animation loop ends.
- `.getRenderer() :WebGLRenderer` — Returns the renderer associated with this inspector.
- `.init()` — Initializes the inspector.
- `.inspect( node :Node)` — Inspects a node.
- `.setRenderer( renderer :WebGLRenderer) :InspectorBase` — Sets the renderer for this inspector.

## Source