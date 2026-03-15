# RenderTarget
Extends: EventDispatcher→

A render target is a buffer where the video card draws pixels for a scene
that is being rendered in the background. It is used in different effects,
such as applying postprocessing to a rendered image before displaying it
on the screen.

## Constructor
`newRenderTarget( width :number, height :number, options :RenderTarget~Options)`
Constructs a new render target.

## Properties
- `.depth : number` — The depth of the render target. Default is 1 .
- `.depthBuffer : boolean` — Whether to allocate a depth buffer or not. Default is true .
- `.depthTexture :DepthTexture` — Instead of saving the depth in a renderbuffer, a texture
can be used instead which is useful for further processing
e.g. in context of post-processing. Default is null .
- `.height : number` — The height of the render target. Default is 1 .
- `.isRenderTarget : boolean` — This flag can be used for type testing. Default is true .
- `.multiview : boolean` — Whether to this target is used in multiview rendering. Default is false .
- `.resolveDepthBuffer : boolean` — Whether to resolve the depth buffer or not. Default is true .
- `.resolveStencilBuffer : boolean` — Whether to resolve the stencil buffer or not. Default is true .
- `.samples : number` — The number of MSAA samples. A value of 0 disables MSAA. Default is 0 .
- `.scissor :Vector4` — A rectangular area inside the render target's viewport. Fragments that are
outside the area will be discarded. Default is (0,0,width,height) .
- `.scissorTest : boolean` — Indicates whether the scissor test should be enabled when rendering into
this render target or not. Default is false .
- `.stencilBuffer : boolean` — Whether to allocate a stencil buffer or not. Default is false .
- `.texture :Texture` — The texture representing the default color attachment.
- `.textures : Array.<Texture>` — An array of textures. Each color attachment is represented as a separate texture.
Has at least a single entry for the default color attachment.
- `.viewport :Vector4` — A rectangular area representing the render target's viewport. Default is (0,0,width,height) .
- `.width : number` — The width of the render target. Default is 1 .

## Methods
- `.clone() :RenderTarget` — Returns a new render target with copied values from this instance.
- `.copy( source :RenderTarget) :RenderTarget` — Copies the settings of the given render target. This is a structural copy so
no resources are shared between render targets after the copy. That includes
all MRT textures and the depth texture.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setSize( width :number, height :number, depth :number)` — Sets the size of this render target.

## Type Definitions
- `.Options` — Render target options.

## Source