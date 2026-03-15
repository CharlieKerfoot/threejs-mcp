# Renderer

Base class for renderers.

## Constructor
`newRenderer( backend :Backend, parameters :Renderer~Options)`
Constructs a new renderer.

## Properties
- `.alpha : boolean` — Whether the default framebuffer should be transparent or opaque. Default is true .
- `.autoClear : boolean` — Whether the renderer should automatically clear the current rendering target
before execute a render() call. The target can be the canvas (default framebuffer)
or the current bound render target (c...
- `.autoClearColor : boolean` — When autoClear is set to true , this property defines whether the renderer
should clear the color buffer. Default is true .
- `.autoClearDepth : boolean` — When autoClear is set to true , this property defines whether the renderer
should clear the depth buffer. Default is true .
- `.autoClearStencil : boolean` — When autoClear is set to true , this property defines whether the renderer
should clear the stencil buffer. Default is true .
- `.backend :Backend` — A reference to the current backend.
- `.contextNode :ContextNode` — A global context node that stores override nodes for specific transformations or calculations.
These nodes can be used to replace default behavior in the rendering pipeline.
- `.coordinateSystem : number` — The coordinate system of the renderer. The value of this property
depends on the selected backend. Either THREE.WebGLCoordinateSystem or THREE.WebGPUCoordinateSystem .
- `.currentColorSpace : string` — The current color space of the renderer. When not producing screen output,
the color space is always the working color space.
- `.currentSamples : number` — The current number of samples used for multi-sample anti-aliasing (MSAA). When rendering to a custom render target, the number of samples of that render target is used.
If the renderer needs an int...
- `.currentToneMapping : number` — The current tone mapping of the renderer. When not producing screen output,
the tone mapping is always NoToneMapping .
- `.debug :DebugConfig` — The renderer's debug configuration.
- `.depth : boolean` — Whether the default framebuffer should have a depth buffer or not. Default is true .
- `.domElement : HTMLCanvasElement | OffscreenCanvas` — A reference to the canvas element the renderer is drawing to.
This value of this property will automatically be created by
the renderer.
- `.highPrecision : boolean` — Enables or disables high precision for model-view and normal-view matrices.
When enabled, will use CPU 64-bit precision for higher precision instead of GPU 32-bit for higher performance. NOTE: 64-b...
- `.highPrecision : boolean` — Returns whether high precision is enabled or not.
- `.info :Info` — Holds a series of statistical information about the GPU memory
and the rendering process. Useful for debugging and monitoring.
- `.initialized (readonly)` — Returns whether the renderer has been initialized or not.
- `.inspector :InspectorBase` — The inspector instance. The inspector can be any class that extends from InspectorBase .
- `.isOutputTarget` — Returns true if the rendering settings are set to screen output.
- `.isRenderer : boolean` — This flag can be used for type testing. Default is true .
- `.library :NodeLibrary` — The node library defines how certain library objects like materials, lights
or tone mapping functions are mapped to node types. This is required since
although instances of classes like MeshBasicMa...
- `.lighting :Lighting` — A map-like data structure for managing lights.
- `.logarithmicDepthBuffer : boolean` — Whether logarithmic depth buffer is enabled or not. Default is false .
- `.needsFrameBufferTarget` — Returns true if a framebuffer target is needed to perform tone mapping or color space conversion.
If this is the case, the renderer allocates an internal render target for that purpose.
- `.onDeviceLost : function` — A callback function that defines what should happen when a device/context lost occurs.
- `.opaque : boolean` — Whether the renderer should render opaque render objects or not. Default is true .
- `.outputColorSpace : string` — Defines the output color space of the renderer. Default is SRGBColorSpace .
- `.reversedDepthBuffer : boolean` — Whether reversed depth buffer is enabled or not. Default is false .
- `.samples : number` — The number of samples used for multi-sample anti-aliasing (MSAA). Default is 0 .
- `.shadowMap :ShadowMapConfig` — The renderer's shadow configuration.
- `.sortObjects : boolean` — Whether the renderer should sort its render lists or not. Note: Sorting is used to attempt to properly render objects that have some degree of transparency.
By definition, sorting objects may not w...
- `.stencil : boolean` — Whether the default framebuffer should have a stencil buffer or not. Default is false .
- `.toneMapping : number` — Defines the tone mapping of the renderer. Default is NoToneMapping .
- `.toneMappingExposure : number` — Defines the tone mapping exposure. Default is 1 .
- `.transparent : boolean` — Whether the renderer should render transparent render objects or not. Default is true .
- `.xr :XRManager` — The renderer's XR manager.

## Methods
- `.clear( color :boolean, depth :boolean, stencil :boolean)` — Performs a manual clear operation. This method ignores autoClear properties.
- `.clearAsync( color :boolean, depth :boolean, stencil :boolean) : Promise` — Async version of Renderer#clear .
- `.clearColor()` — Performs a manual clear operation of the color buffer. This method ignores autoClear properties.
- `.clearColorAsync() : Promise` — Async version of Renderer#clearColor .
- `.clearDepth()` — Performs a manual clear operation of the depth buffer. This method ignores autoClear properties.
- `.clearDepthAsync() : Promise` — Async version of Renderer#clearDepth .
- `.clearStencil()` — Performs a manual clear operation of the stencil buffer. This method ignores autoClear properties.
- `.clearStencilAsync() : Promise` — Async version of Renderer#clearStencil .
- `.compile( scene :Object3D, camera :Camera, targetScene :Scene) : function` — Alias for compileAsync() .
- `.compileAsync( scene :Object3D, camera :Camera, targetScene :Scene) : Promise` — Compiles all materials in the given scene. This can be useful to avoid a
phenomenon which is called "shader compilation stutter", which occurs when
rendering an object with a new shader for the fir...
- `.compute( computeNodes :Node| Array.<Node>, dispatchSize :number | Array.<number> |IndirectStorageBufferAttribute) : Promise | undefined` — Execute a single or an array of compute nodes. This method can only be called
if the renderer has been initialized.
- `.computeAsync( computeNodes :Node| Array.<Node>, dispatchSize :number | Array.<number> |IndirectStorageBufferAttribute) : Promise` — Execute a single or an array of compute nodes.
- `.copyFramebufferToTexture( framebufferTexture :FramebufferTexture, rectangle :Vector2|Vector4)` — Copies the current bound framebuffer into the given texture.
- `.copyTextureToTexture( srcTexture :Texture, dstTexture :Texture, srcRegion :Box2|Box3, dstPosition :Vector2|Vector3, srcLevel :number, dstLevel :number)` — Copies data of the given source texture into a destination texture.
- `.dispose()` — Frees all internal resources of the renderer. Call this method if the renderer
is no longer in use by your app.
- `.getActiveCubeFace() : number` — Returns the active cube face.
- `.getActiveMipmapLevel() : number` — Returns the active mipmap level.
- `.getAnimationLoop() : function` — Returns the current animation loop callback.
- `.getArrayBufferAsync( attribute :StorageBufferAttribute) : Promise.<ArrayBuffer>` — Can be used to transfer buffer data from a storage buffer attribute
from the GPU to the CPU in context of compute shaders.
- `.getCanvasTarget() :CanvasTarget` — Returns the current canvas target.
- `.getClearAlpha() : number` — Returns the clear alpha.
- `.getClearColor( target :Color) :Color` — Returns the clear color.
- `.getClearDepth() : number` — Returns the clear depth.
- `.getClearStencil() : number` — Returns the clear stencil.
- `.getColorBufferType() : number` — Returns the output buffer type.
- `.getContext() : GPUCanvasContext | WebGL2RenderingContext` — Returns the rendering context.
- `.getDrawingBufferSize( target :Vector2) :Vector2` — Returns the drawing buffer size in physical pixels. This method honors the pixel ratio.
- `.getMRT() :MRTNode` — Returns the MRT configuration.
- `.getMaxAnisotropy() : number` — Returns the maximum available anisotropy for texture filtering.
- `.getOutputBufferType() : number` — Returns the output buffer type.
- `.getOutputRenderTarget() :RenderTarget` — Returns the current output target.
- `.getPixelRatio() : number` — Returns the pixel ratio.
- `.getRenderObjectFunction() : function` — Returns the current render object function.
- `.getRenderTarget() :RenderTarget` — Returns the current render target.
- `.getScissor( target :Vector4) :Vector4` — Returns the scissor rectangle.
- `.getScissorTest() : boolean` — Returns the scissor test value.
- `.getSize( target :Vector2) :Vector2` — Returns the renderer's size in logical pixels. This method does not honor the pixel ratio.
- `.getViewport( target :Vector4) :Vector4` — Returns the viewport definition.
- `.hasCompatibility( name :string) : boolean` — Checks if the given compatibility is supported by the selected backend. If the
renderer has not been initialized, this method always returns false .
- `.hasFeature( name :string) : boolean` — Checks if the given feature is supported by the selected backend. If the
renderer has not been initialized, this method always returns false .
- `.hasFeatureAsync( name :string) : Promise.<boolean>` — Checks if the given feature is supported by the selected backend.
- `.hasInitialized() : boolean` — Returns true when the renderer has been initialized.
- `.init() : Promise.<this>` — Initializes the renderer so it is ready for usage.
- `.initRenderTarget( renderTarget :RenderTarget)` — Initializes the given render target.
- `.initTexture( texture :Texture)` — Initializes the given texture. Useful for preloading a texture rather than waiting until first render
(which can cause noticeable lags due to decode and GPU upload overhead). This method can only b...
- `.initTextureAsync( texture :Texture) : Promise` — Initializes the given textures. Useful for preloading a texture rather than waiting until first render
(which can cause noticeable lags due to decode and GPU upload overhead).
- `.isOccluded( object :Object3D) : boolean` — This method performs an occlusion query for the given 3D object.
It returns true if the given 3D object is fully occluded by other
3D objects in the scene.
- `.readRenderTargetPixelsAsync( renderTarget :RenderTarget, x :number, y :number, width :number, height :number, textureIndex :number, faceIndex :number) : Promise.<TypedArray>` — Reads pixel data from the given render target.
- `.render( scene :Object3D, camera :Camera)` — Renders the scene or 3D object with the given camera. This method can only be called
if the renderer has been initialized. When using render() inside an animation loop,
it's guaranteed the renderer...
- `.renderAsync( scene :Object3D, camera :Camera) : Promise` — Renders the scene in an async fashion.
- `.renderObject( object :Object3D, scene :Scene, camera :Camera, geometry :BufferGeometry, material :Material, group :Object, lightsNode :LightsNode, clippingContext :ClippingContext, passId :string)` — This method represents the default render object function that manages the render lifecycle
of the object.
- `.setAnimationLoop( callback :onAnimationCallback) : Promise` — Applications are advised to always define the animation loop
with this method and not manually with requestAnimationFrame() for best compatibility.
- `.setCanvasTarget( canvasTarget :CanvasTarget)` — Sets the canvas target. The canvas target manages the HTML canvas
or the offscreen canvas the renderer draws into.
- `.setClearAlpha( alpha :number)` — Defines the clear alpha.
- `.setClearColor( color :Color, alpha :number)` — Defines the clear color and optionally the clear alpha.
- `.setClearDepth( depth :number)` — Defines the clear depth.
- `.setClearStencil( stencil :number)` — Defines the clear stencil.
- `.setDrawingBufferSize( width :number, height :number, pixelRatio :number)` — This method allows to define the drawing buffer size by specifying
width, height and pixel ratio all at once. The size of the drawing
buffer is computed with this formula: size.x = width * pixelRat...
- `.setMRT( mrt :MRTNode) :Renderer` — Sets the given MRT configuration.
- `.setOpaqueSort( method :function)` — Defines a manual sort function for the opaque render list.
Pass null to use the default sort.
- `.setOutputRenderTarget( renderTarget :Object)` — Sets the output render target for the renderer.
- `.setPixelRatio( value :number)` — Sets the given pixel ratio and resizes the canvas if necessary.
- `.setRenderObjectFunction( renderObjectFunction :renderObjectFunction)` — Sets the given render object function. Calling this method overwrites the default implementation
which is Renderer#renderObject . Defining a custom function can be useful
if you want to modify the ...
- `.setRenderTarget( renderTarget :RenderTarget, activeCubeFace :number, activeMipmapLevel :number)` — Sets the given render target. Calling this method means the renderer does not
target the default framebuffer (meaning the canvas) anymore but a custom framebuffer.
Use null as the first argument to...
- `.setScissor( x :number |Vector4, y :number, width :number, height :number)` — Defines the scissor rectangle.
- `.setScissorTest( boolean :boolean)` — Defines the scissor test.
- `.setSize( width :number, height :number, updateStyle :boolean)` — Sets the size of the renderer.
- `.setTransparentSort( method :function)` — Defines a manual sort function for the transparent render list.
Pass null to use the default sort.
- `.setViewport( x :number |Vector4, y :number, width :number, height :number, minDepth :number, maxDepth :number)` — Defines the viewport.
- `.waitForGPU() : Promise` — Can be used to synchronize CPU operations with GPU tasks. So when this method is called,
the CPU waits for the GPU to complete its operation (e.g. a compute task).

## Type Definitions
- `.Options` — Renderer options.

## Source