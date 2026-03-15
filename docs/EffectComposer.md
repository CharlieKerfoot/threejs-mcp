# EffectComposer

Used to implement post-processing effects in three.js.
The class manages a chain of post-processing passes to produce the final visual result.
Post-processing passes are executed in order of their addition/insertion.
The last pass is automatically rendered to screen. This module can only be used with WebGLRenderer .

## Constructor
`newEffectComposer( renderer :WebGLRenderer, renderTarget :WebGLRenderTarget)`
Constructs a new effect composer.

## Import

## Properties
- `.passes : Array.<Pass>` — An array representing the (ordered) chain of post-processing passes.
- `.readBuffer :WebGLRenderTarget` — A reference to the internal read buffer. Passes usually read
the previous render result from this buffer.
- `.renderToScreen : boolean` — Whether the final pass is rendered to the screen (default framebuffer) or not. Default is true .
- `.renderer :WebGLRenderer` — The renderer.
- `.writeBuffer :WebGLRenderTarget` — A reference to the internal write buffer. Passes usually write
their result into this buffer.

## Methods
- `.addPass( pass :Pass)` — Adds the given pass to the pass chain.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever the composer is no longer used in your app.
- `.insertPass( pass :Pass, index :number)` — Inserts the given pass at a given index.
- `.isLastEnabledPass( passIndex :number) : boolean` — Returns true if the pass for the given index is the last enabled pass in the pass chain.
- `.removePass( pass :Pass)` — Removes the given pass from the pass chain.
- `.render( deltaTime :number)` — Executes all enabled post-processing passes in order to produce the final frame.
- `.reset( renderTarget :WebGLRenderTarget)` — Resets the internal state of the EffectComposer.
- `.setPixelRatio( pixelRatio :number)` — Sets device pixel ratio. This is usually used for HiDPI device to prevent blurring output.
Setting the pixel ratio will automatically resize the composer.
- `.setSize( width :number, height :number)` — Resizes the internal read and write buffers as well as all passes. Similar to WebGLRenderer#setSize ,
this method honors the current pixel ration.
- `.swapBuffers()` — Swaps the internal read/write buffers.

## Source