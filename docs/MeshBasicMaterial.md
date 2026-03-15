# MeshBasicMaterial
Extends: EventDispatcher→Material→

A material for drawing geometries in a simple shaded (flat or wireframe) way. This material is not affected by lights.

## Constructor
`newMeshBasicMaterial( parameters :Object)`
Constructs a new mesh basic material.

## Properties
- `.alphaMap :Texture` — The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Only the color of the texture is used, ignoring the alpha channel ...
- `.aoMap :Texture` — The red channel of this texture is used as the ambient occlusion map.
Requires a second set of UVs. Default is null .
- `.aoMapIntensity : number` — Intensity of the ambient occlusion effect. Range is [0,1] , where 0 disables ambient occlusion. Where intensity is 1 and the AO map's
red channel is also 1 , ambient light is fully occluded on a su...
- `.color :Color` — Color of the material. Default is (1,1,1) .
- `.combine :MultiplyOperation|MixOperation|AddOperation` — How to combine the result of the surface's color with the environment map, if any. When set to MixOperation , the MeshBasicMaterial#reflectivity is used to
blend between the two colors. Default is ...
- `.envMap :Texture` — The environment map. Default is null .
- `.envMapRotation :Euler` — The rotation of the environment map in radians. Default is (0,0,0) .
- `.fog : boolean` — Whether the material is affected by fog or not. Default is true .
- `.isMeshBasicMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lightMap :Texture` — The light map. Requires a second set of UVs. Default is null .
- `.lightMapIntensity : number` — Intensity of the baked light. Default is 1 .
- `.map :Texture` — The color map. May optionally include an alpha channel, typically combined
with Material#transparent or Material#alphaTest . The texture map
color is modulated by the diffuse color . Default is null .
- `.reflectivity : number` — How much the environment map affects the surface.
The valid range is between 0 (no reflections) and 1 (full reflections). Default is 1 .
- `.refractionRatio : number` — The index of refraction (IOR) of air (approximately 1) divided by the
index of refraction of the material. It is used with environment mapping
modes CubeRefractionMapping and EquirectangularRefract...
- `.specularMap :Texture` — Specular map used by the material. Default is null .
- `.wireframe : boolean` — Renders the geometry as a wireframe. Default is false .
- `.wireframeLinecap : 'round' | 'bevel' | 'miter'` — Defines appearance of wireframe ends. Can only be used with SVGRenderer . Default is 'round' .
- `.wireframeLinejoin : 'round' | 'bevel' | 'miter'` — Defines appearance of wireframe joints. Can only be used with SVGRenderer . Default is 'round' .
- `.wireframeLinewidth : number` — Controls the thickness of the wireframe. Can only be used with SVGRenderer . Default is 1 .

## Source