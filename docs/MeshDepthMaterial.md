# MeshDepthMaterial
Extends: EventDispatcher→Material→

A material for drawing geometry by depth. Depth is based off of the camera
near and far plane. White is nearest, black is farthest.

## Constructor
`newMeshDepthMaterial( parameters :Object)`
Constructs a new mesh depth material.

## Properties
- `.alphaMap :Texture` — The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Only the color of the texture is used, ignoring the alpha channel ...
- `.depthPacking :BasicDepthPacking|RGBADepthPacking|RGBDepthPacking|RGDepthPacking` — Type for depth packing. Default is BasicDepthPacking .
- `.displacementBias : number` — The offset of the displacement map's values on the mesh's vertices.
The bias is added to the scaled sample of the displacement map.
Without a displacement map set, this value is not applied. Defaul...
- `.displacementMap :Texture` — The displacement map affects the position of the mesh's vertices. Unlike
other maps which only affect the light and shade of the material the
displaced vertices can cast shadows, block other object...
- `.displacementScale : number` — How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement
map set, this value is not applied. Default is 0 .
- `.isMeshDepthMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.map :Texture` — The color map. May optionally include an alpha channel, typically combined
with Material#transparent or Material#alphaTest . Default is null .
- `.wireframe : boolean` — Renders the geometry as a wireframe. Default is false .
- `.wireframeLinewidth : number` — Controls the thickness of the wireframe. WebGL and WebGPU ignore this property and always render
1 pixel wide lines. Default is 1 .

## Source