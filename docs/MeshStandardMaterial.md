# MeshStandardMaterial
Extends: EventDispatcher→Material→

A standard physically based material, using Metallic-Roughness workflow. Physically based rendering (PBR) has recently become the standard in many
3D applications, such as Unity , Unreal and 3D Studio Max . This approach differs from older approaches in that instead of using
approximations for the way in which light interacts with a surface, a
physically correct model is used. The idea is that, instead of tweaking
materials to look good under specific lighting, a material can be created
that will react 'correctly' under all lighting scenarios. In practice this gives a more accurate and realistic looking result than
the MeshLambertMaterial or MeshPhongMaterial , at the cost of
being somewhat more computationally expensive. MeshStandardMaterial uses per-fragment
shading. Note that for best results you should always specify an environment map when using this material. For a non-technical introduction to the concept of PBR and how to set up a
PBR material, check out these articles by the people at marmoset : Basic Theory of Physically Based Rendering Physically Based Rendering and You Can Too Technical details of the approach used in three.js (and most other PBR systems) can be found is this paper from Disney (pdf), by Brent Burley.

## Constructor
`newMeshStandardMaterial( parameters :Object)`
Constructs a new mesh standard material.

## Properties
- `.alphaMap :Texture` — The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Only the color of the texture is used, ignoring the alpha channel ...
- `.aoMap :Texture` — The red channel of this texture is used as the ambient occlusion map.
Requires a second set of UVs. Default is null .
- `.aoMapIntensity : number` — Intensity of the ambient occlusion effect. Range is [0,1] , where 0 disables ambient occlusion. Where intensity is 1 and the AO map's
red channel is also 1 , ambient light is fully occluded on a su...
- `.bumpMap :Texture` — The texture to create a bump map. The black and white values map to the
perceived depth in relation to the lights. Bump doesn't actually affect
the geometry of the object, only the lighting. If a n...
- `.bumpScale : number` — How much the bump map affects the material. Typical range is [0,1] . Default is 1 .
- `.color :Color` — Color of the material. Default is (1,1,1) .
- `.displacementBias : number` — The offset of the displacement map's values on the mesh's vertices.
The bias is added to the scaled sample of the displacement map.
Without a displacement map set, this value is not applied. Defaul...
- `.displacementMap :Texture` — The displacement map affects the position of the mesh's vertices. Unlike
other maps which only affect the light and shade of the material the
displaced vertices can cast shadows, block other object...
- `.displacementScale : number` — How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement
map set, this value is not applied. Default is 0 .
- `.emissive :Color` — Emissive (light) color of the material, essentially a solid color
unaffected by other lighting. Default is (0,0,0) .
- `.emissiveIntensity : number` — Intensity of the emissive light. Modulates the emissive color. Default is 1 .
- `.emissiveMap :Texture` — Set emissive (glow) map. The emissive map color is modulated by the
emissive color and the emissive intensity. If you have an emissive map,
be sure to set the emissive color to something other than...
- `.envMap :Texture` — The environment map. To ensure a physically correct rendering, environment maps
are internally pre-processed with PMREMGenerator . Default is null .
- `.envMapIntensity : number` — Scales the effect of the environment map by multiplying its color. Default is 1 .
- `.envMapRotation :Euler` — The rotation of the environment map in radians. Default is (0,0,0) .
- `.flatShading : boolean` — Whether the material is rendered with flat shading or not. Default is false .
- `.fog : boolean` — Whether the material is affected by fog or not. Default is true .
- `.isMeshStandardMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lightMap :Texture` — The light map. Requires a second set of UVs. Default is null .
- `.lightMapIntensity : number` — Intensity of the baked light. Default is 1 .
- `.map :Texture` — The color map. May optionally include an alpha channel, typically combined
with Material#transparent or Material#alphaTest . The texture map
color is modulated by the diffuse color . Default is null .
- `.metalness : number` — How much the material is like a metal. Non-metallic materials such as wood
or stone use 0.0 , metallic use 1.0 , with nothing (usually) in between.
A value between 0.0 and 1.0 could be used for a r...
- `.metalnessMap :Texture` — The blue channel of this texture is used to alter the metalness of the
material. Default is null .
- `.normalMap :Texture` — The texture to create a normal map. The RGB values affect the surface
normal for each pixel fragment and change the way the color is lit. Normal
maps do not change the actual shape of the surface, ...
- `.normalMapType :TangentSpaceNormalMap|ObjectSpaceNormalMap` — The type of normal map. Default is TangentSpaceNormalMap .
- `.normalScale :Vector2` — How much the normal map affects the material. Typical value range is [0,1] . Default is (1,1) .
- `.roughness : number` — How rough the material appears. 0.0 means a smooth mirror reflection, 1.0 means fully diffuse. If roughnessMap is also provided,
both values are multiplied. Default is 1 .
- `.roughnessMap :Texture` — The green channel of this texture is used to alter the roughness of the
material. Default is null .
- `.wireframe : boolean` — Renders the geometry as a wireframe. Default is false .
- `.wireframeLinecap : 'round' | 'bevel' | 'miter'` — Defines appearance of wireframe ends. Can only be used with SVGRenderer . Default is 'round' .
- `.wireframeLinejoin : 'round' | 'bevel' | 'miter'` — Defines appearance of wireframe joints. Can only be used with SVGRenderer . Default is 'round' .
- `.wireframeLinewidth : number` — Controls the thickness of the wireframe. Can only be used with SVGRenderer . Default is 1 .

## Source