# RTTNode
Extends: EventDispatcher→Node→InputNode→UniformNode→TextureNode→

RTTNode takes another node and uses it with a QuadMesh to render into a texture (RTT).
This module is especially relevant in context of post processing where certain nodes require
texture input for their effects. With the helper function convertToTexture() which is based
on this module, the node system can automatically ensure texture input if required.

## Constructor
`newRTTNode( node :Node, width :number, height :number, options :Object)`
Constructs a new RTT node.

## Properties
- `.autoResize : boolean` — Whether the internal render target should automatically be resized or not. Default is true .
- `.autoUpdate : boolean` — Whether the texture should automatically be updated or not. Default is true .
- `.height : number` — The height of the internal render target. Default is null .
- `.isRTTNode : boolean` — This flag can be used for type testing. Default is true .
- `.node :Node` — The node to render a texture with.
- `.pixelRatio : number` — The pixel ratio Default is 1 .
- `.renderTarget :RenderTarget` — The render target
- `.textureNeedsUpdate : boolean` — Whether the texture requires an update or not. Default is true .
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.RENDER since the node updates
the texture once per render in its RTTNode#updateBefore method. Default is 'render' .
- `.width : number` — The width of the internal render target.
If not width is applied, the render target is automatically resized. Default is null .

## Methods
- `.setPixelRatio( pixelRatio :number)` — Sets the pixel ratio. This will also resize the render target.
- `.setSize( width :number, height :number)` — Sets the size of the internal render target

## Source