# MeshNormalMaterial
Extends: EventDispatcher→Material→

A material that maps the normal vectors to RGB colors.

## Constructor
`newMeshNormalMaterial( parameters :Object)`
Constructs a new mesh normal material.

## Properties
- `.bumpMap :Texture` — The texture to create a bump map. The black and white values map to the
perceived depth in relation to the lights. Bump doesn't actually affect
the geometry of the object, only the lighting. If a n...
- `.bumpScale : number` — How much the bump map affects the material. Typical range is [0,1] . Default is 1 .
- `.displacementBias : number` — The offset of the displacement map's values on the mesh's vertices.
The bias is added to the scaled sample of the displacement map.
Without a displacement map set, this value is not applied. Defaul...
- `.displacementMap :Texture` — The displacement map affects the position of the mesh's vertices. Unlike
other maps which only affect the light and shade of the material the
displaced vertices can cast shadows, block other object...
- `.displacementScale : number` — How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement
map set, this value is not applied. Default is 0 .
- `.flatShading : boolean` — Whether the material is rendered with flat shading or not. Default is false .
- `.isMeshNormalMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.normalMap :Texture` — The texture to create a normal map. The RGB values affect the surface
normal for each pixel fragment and change the way the color is lit. Normal
maps do not change the actual shape of the surface, ...
- `.normalMapType :TangentSpaceNormalMap|ObjectSpaceNormalMap` — The type of normal map. Default is TangentSpaceNormalMap .
- `.normalScale :Vector2` — How much the normal map affects the material. Typical value range is [0,1] . Default is (1,1) .
- `.wireframe : boolean` — Renders the geometry as a wireframe. Default is false .
- `.wireframeLinewidth : number` — Controls the thickness of the wireframe. WebGL and WebGPU ignore this property and always render
1 pixel wide lines. Default is 1 .

## Source