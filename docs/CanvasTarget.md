# CanvasTarget
Extends: EventDispatcher→

CanvasTarget is a class that represents the final output destination of the renderer.

## Constructor
`newCanvasTarget( domElement :HTMLCanvasElement | OffscreenCanvas)`
Constructs a new CanvasTarget.

## Properties
- `.colorTexture :FramebufferTexture` — The color texture of the default framebuffer.
- `.depthTexture :DepthTexture` — The depth texture of the default framebuffer.
- `.domElement : HTMLCanvasElement | OffscreenCanvas` — A reference to the canvas element the renderer is drawing to.
This value of this property will automatically be created by
the renderer.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getDrawingBufferSize( target :Vector2) :Vector2` — Returns the drawing buffer size in physical pixels. This method honors the pixel ratio.
- `.getPixelRatio() : number` — Returns the pixel ratio.
- `.getScissor( target :Vector4) :Vector4` — Returns the scissor rectangle.
- `.getScissorTest() : boolean` — Returns the scissor test value.
- `.getSize( target :Vector2) :Vector2` — Returns the renderer's size in logical pixels. This method does not honor the pixel ratio.
- `.getViewport( target :Vector4) :Vector4` — Returns the viewport definition.
- `.setDrawingBufferSize( width :number, height :number, pixelRatio :number)` — This method allows to define the drawing buffer size by specifying
width, height and pixel ratio all at once. The size of the drawing
buffer is computed with this formula: size.x = width * pixelRat...
- `.setPixelRatio( value :number)` — Sets the given pixel ratio and resizes the canvas if necessary.
- `.setScissor( x :number |Vector4, y :number, width :number, height :number)` — Defines the scissor rectangle.
- `.setScissorTest( boolean :boolean)` — Defines the scissor test.
- `.setSize( width :number, height :number, updateStyle :boolean)` — Sets the size of the renderer.
- `.setViewport( x :number |Vector4, y :number, width :number, height :number, minDepth :number, maxDepth :number)` — Defines the viewport.

## Source