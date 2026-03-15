# ViewportTextureNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

A special type of texture node which represents the data of the current viewport
as a texture. The module extracts data from the current bound framebuffer with
a copy operation so no extra render pass is required to produce the texture data
(which is good for performance). ViewportTextureNode can be used as an input for a
variety of effects like refractive or transmissive materials.

## Constructor
`newViewportTextureNode( uvNode :Node, levelNode :Node, framebufferTexture :Texture)`
Constructs a new viewport texture node.

## Properties
- `.defaultFramebuffer :FramebufferTexture` — The reference framebuffer texture. This is used to store the framebuffer texture
for the current render target. If the render target changes, a new framebuffer texture
is created automatically. Def...
- `.generateMipmaps : boolean` — Whether to generate mipmaps or not. Default is false .
- `.isOutputTextureNode : boolean` — This flag can be used for type testing. Default is true .
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.RENDER since the node should extract
the current contents of the bound framebuffer for each render call. Default is 'render' .

## Methods
- `.getTextureForReference( reference :RenderTarget) :Texture` — This methods returns a texture for the given render target reference. To avoid rendering errors, ViewportTextureNode must use unique framebuffer textures
for different render contexts.

## Source