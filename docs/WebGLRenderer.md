# WebGLRenderer

This renderer uses WebGL 2 to display scenes. WebGL 1 is not supported since r163 .

## Constructor
`newWebGLRenderer( parameters :WebGLRenderer~Options)`
Constructs a new WebGL renderer.

## Properties
- `.autoClear : boolean` — Whether the renderer should automatically clear its output before rendering a frame or not. Default is true .
- `.autoClearColor : boolean` — If WebGLRenderer#autoClear set to true , whether the renderer should clear
the color buffer or not. Default is true .
- `.autoClearDepth : boolean` — If WebGLRenderer#autoClear set to true , whether the renderer should clear
the depth buffer or not. Default is true .
- `.autoClearStencil : boolean` — If WebGLRenderer#autoClear set to true , whether the renderer should clear
the stencil buffer or not. Default is true .
- `.capabilities :WebGLRenderer~Capabilities` — Holds details about the capabilities of the current rendering context.
- `.clippingPlanes : Array.<Plane>` — User-defined clipping planes specified in world space. These planes apply globally.
Points in space whose dot product with the plane is negative are cut away.
- `.coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem` — Defines the coordinate system of the renderer. In WebGLRenderer , the value is always WebGLCoordinateSystem . Default is WebGLCoordinateSystem .
- `.debug : Object` — A object with debug configuration settings. checkShaderErrors : If it is true , defines whether material shader programs are
checked for errors during compilation and linkage process. It may be use...
- `.domElement : HTMLCanvasElement | OffscreenCanvas` — A canvas where the renderer draws its output. This is automatically created by the renderer
in the constructor (if not provided already); you just need to add it to your page like so: document.body...
- `.extensions : Object` — Provides methods for retrieving and testing WebGL extensions. get(extensionName:string) : Used to check whether a WebGL extension is supported
and return the extension object if available. has(exte...
- `.info :WebGLRenderer~Info` — Holds a series of statistical information about the GPU memory
and the rendering process. Useful for debugging and monitoring. By default these data are reset at each render call but when having
mu...
- `.isWebGLRenderer : boolean` — This flag can be used for type testing. Default is true .
- `.localClippingEnabled : boolean` — Whether the renderer respects object-level clipping planes or not. Default is false .
- `.outputColorSpace :SRGBColorSpace|LinearSRGBColorSpace` — Defines the output color space of the renderer. Default is SRGBColorSpace .
- `.properties : Object` — Used to track properties of other objects like native WebGL objects.
- `.renderLists : Object` — Manages the render lists of the renderer.
- `.shadowMap :WebGLRenderer~ShadowMap` — Interface for managing shadows.
- `.sortObjects : boolean` — Whether the renderer should sort objects or not. Note: Sorting is used to attempt to properly render objects that have some
degree of transparency. By definition, sorting objects may not work in al...
- `.state : Object` — Interface for managing the WebGL state.
- `.toneMapping :NoToneMapping|LinearToneMapping|ReinhardToneMapping|CineonToneMapping|ACESFilmicToneMapping|CustomToneMapping|AgXToneMapping|NeutralToneMapping` — The tone mapping technique of the renderer. Default is NoToneMapping .
- `.toneMappingExposure : number` — Exposure level of tone mapping. Default is 1 .
- `.transmissionResolutionScale : number` — The normalized resolution scale for the transmission render target, measured in percentage
of viewport dimensions. Lowering this value can result in significant performance improvements
when using ...
- `.xr :WebXRManager` — A reference to the XR manager.

## Methods
- `.clear( color :boolean, depth :boolean, stencil :boolean)` — Tells the renderer to clear its color, depth or stencil drawing buffer(s).
This method initializes the buffers to the current clear color values.
- `.clearColor()` — Clears the color buffer. Equivalent to calling renderer.clear( true, false, false ) .
- `.clearDepth()` — Clears the depth buffer. Equivalent to calling renderer.clear( false, true, false ) .
- `.clearStencil()` — Clears the stencil buffer. Equivalent to calling renderer.clear( false, false, true ) .
- `.compile( scene :Object3D, camera :Camera, targetScene :Scene) : Set.<Material>` — Compiles all materials in the scene with the camera. This is useful to precompile shaders
before the first rendering. If you want to add a 3D object to an existing scene, use the third
optional par...
- `.compileAsync( scene :Object3D, camera :Camera, targetScene :Scene) : Promise` — Asynchronous version of WebGLRenderer#compile . This method makes use of the KHR_parallel_shader_compile WebGL extension. Hence,
it is recommended to use this version of compile() whenever possible.
- `.copyFramebufferToTexture( texture :FramebufferTexture, position :Vector2, level :number)` — Copies pixels from the current bound framebuffer into the given texture.
- `.copyTextureToTexture( srcTexture :Texture, dstTexture :Texture, srcRegion :Box2|Box3, dstPosition :Vector2|Vector3, srcLevel :number, dstLevel :number)` — Copies data of the given source texture into a destination texture. When using render target textures as srcTexture and dstTexture , you must make sure both render targets are initialized WebGLRend...
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.forceContextLoss()` — Simulates a loss of the WebGL context. This requires support for the WEBGL_lose_context extension.
- `.forceContextRestore()` — Simulates a restore of the WebGL context. This requires support for the WEBGL_lose_context extension.
- `.getActiveCubeFace() : number` — Returns the active cube face.
- `.getActiveMipmapLevel() : number` — Returns the active mipmap level.
- `.getClearAlpha() : number` — Returns the clear alpha. Ranges within [0,1] .
- `.getClearColor( target :Color) :Color` — Returns the clear color.
- `.getContext() : WebGL2RenderingContext` — Returns the rendering context.
- `.getContextAttributes() : WebGLContextAttributes` — Returns the rendering context attributes.
- `.getCurrentViewport( target :Vector2) :Vector2` — Returns the current viewport definition.
- `.getDrawingBufferSize( target :Vector2) :Vector2` — Returns the drawing buffer size in physical pixels. This method honors the pixel ratio.
- `.getPixelRatio() : number` — Returns the pixel ratio.
- `.getRenderTarget() :WebGLRenderTarget` — Returns the active render target.
- `.getScissor( target :Vector4) :Vector4` — Returns the scissor region.
- `.getScissorTest() : boolean` — Returns true if the scissor test is enabled.
- `.getSize( target :Vector2) :Vector2` — Returns the renderer's size in logical pixels. This method does not honor the pixel ratio.
- `.getViewport( target :Vector4) :Vector4` — Returns the viewport definition.
- `.initRenderTarget( target :WebGLRenderTarget)` — Initializes the given WebGLRenderTarget memory. Useful for initializing a render target so data
can be copied into it using WebGLRenderer#copyTextureToTexture before it has been
rendered to.
- `.initTexture( texture :Texture)` — Initializes the given texture. Useful for preloading a texture rather than waiting until first
render (which can cause noticeable lags due to decode and GPU upload overhead).
- `.readRenderTargetPixels( renderTarget :WebGLRenderTarget, x :number, y :number, width :number, height :number, buffer :TypedArray, activeCubeFaceIndex :number, textureIndex :number)` — Reads the pixel data from the given render target into the given buffer.
- `.readRenderTargetPixelsAsync( renderTarget :WebGLRenderTarget, x :number, y :number, width :number, height :number, buffer :TypedArray, activeCubeFaceIndex :number, textureIndex :number) : Promise.<TypedArray>` — Asynchronous, non-blocking version of WebGLRenderer#readRenderTargetPixels . It is recommended to use this version of readRenderTargetPixels() whenever possible.
- `.render( scene :Object3D, camera :Camera)` — Renders the given scene (or other type of 3D object) using the given camera. The render is done to a previously specified render target set by calling WebGLRenderer#setRenderTarget or to the canvas...
- `.resetState()` — Can be used to reset the internal WebGL state. This method is mostly
relevant for applications which share a single WebGL context across
multiple WebGL libraries.
- `.setAnimationLoop( callback :onAnimationCallback)` — Applications are advised to always define the animation loop
with this method and not manually with requestAnimationFrame() for best compatibility.
- `.setClearAlpha( alpha :number)` — Sets the clear alpha.
- `.setClearColor( color :Color, alpha :number)` — Sets the clear color and alpha.
- `.setDrawingBufferSize( width :number, height :number, pixelRatio :number)` — This method allows to define the drawing buffer size by specifying
width, height and pixel ratio all at once. The size of the drawing
buffer is computed with this formula: size.x = width * pixelRat...
- `.setEffects( effects :Array)` — Sets the post-processing effects to be applied after rendering.
- `.setOpaqueSort( method :function)` — Sets a custom opaque sort function for the render lists. Pass null to use the default painterSortStable function.
- `.setPixelRatio( value :number)` — Sets the given pixel ratio and resizes the canvas if necessary.
- `.setRenderTarget( renderTarget :WebGLRenderTarget, activeCubeFace :number, activeMipmapLevel :number)` — Sets the active rendertarget.
- `.setScissor( x :number |Vector4, y :number, width :number, height :number)` — Sets the scissor region to render from (x, y) to (x + width, y + height) .
- `.setScissorTest( boolean :boolean)` — Enable or disable the scissor test. When this is enabled, only the pixels
within the defined scissor area will be affected by further renderer
actions.
- `.setSize( width :number, height :number, updateStyle :boolean)` — Resizes the output canvas to (width, height) with device pixel ratio taken
into account, and also sets the viewport to fit that size, starting in (0,
0). Setting updateStyle to false prevents any s...
- `.setTransparentSort( method :function)` — Sets a custom transparent sort function for the render lists. Pass null to use the default reversePainterSortStable function.
- `.setViewport( x :number |Vector4, y :number, width :number, height :number)` — Sets the viewport to render from (x, y) to (x + width, y + height) .

## Type Definitions
- `.Capabilities` — WebGLRenderer Capabilities.
- `.Info` — WebGLRenderer Info
- `.InfoMemory` — WebGLRenderer Info Memory
- `.InfoRender` — WebGLRenderer Info Render
- `.Options` — WebGLRenderer options.
- `.ShadowMap` — WebGLRenderer Shadow Map.

## Source