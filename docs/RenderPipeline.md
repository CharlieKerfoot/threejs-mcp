# RenderPipeline

This module is responsible to manage the rendering pipeline setups in apps.
You usually create a single instance of this class and use it to define
the output of your render pipeline and post processing effect chain. Note: This module can only be used with WebGPURenderer .

## Constructor
`newRenderPipeline( renderer :Renderer, outputNode :Node.<vec4>)`
Constructs a new render pipeline management module.

## Properties
- `.context : Object` — Returns the current context of the render pipeline stack.
- `.needsUpdate :Node.<vec4>` — Must be set to true when the output node changes.
- `.outputColorTransform : boolean` — Whether the default output tone mapping and color
space transformation should be enabled or not. It is enabled by default by it must be disabled when
effects must be executed after tone mapping and...
- `.outputNode :Node.<vec4>` — A node which defines the final output of the rendering
pipeline. This is usually the last node in a chain
of effect nodes.
- `.renderer :Renderer` — A reference to the renderer.

## Methods
- `.dispose()` — Frees internal resources.
- `.render()` — When RenderPipeline is used to apply rendering pipeline and post processing effects,
the application must use this version of render() inside
its animation loop (not the one from the renderer).
- `.renderAsync() : Promise` — When RenderPipeline is used to apply rendering pipeline and post processing effects,
the application must use this version of renderAsync() inside
its animation loop (not the one from the renderer).

## Source