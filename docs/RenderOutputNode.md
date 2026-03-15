# RenderOutputNode
Extends: EventDispatcher→Node→TempNode→

Normally, tone mapping and color conversion happens automatically
before outputting pixel too the default (screen) framebuffer. In certain
post processing setups this happens to late because certain effects
require e.g. sRGB input. For such scenarios, RenderOutputNode can be used
to apply tone mapping and color space conversion at an arbitrary point
in the effect chain. When applying tone mapping and color space conversion manually with this node,
you have to set RenderPipeline#outputColorTransform to false .

## Constructor
`newRenderOutputNode( colorNode :Node, toneMapping :number, outputColorSpace :string)`
Constructs a new render output node.

## Properties
- `.colorNode :Node` — The color node to process.
- `.isRenderOutputNode : boolean` — This flag can be used for type testing. Default is true .
- `.outputColorSpace : string` — The output color space.

## Methods
- `.getToneMapping() : number` — Gets the tone mapping type.
- `.setToneMapping( value :number) :ToneMappingNode` — Sets the tone mapping type.

## Source