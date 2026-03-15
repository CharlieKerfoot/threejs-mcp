# MeshDistanceMaterial
Extends: EventDispatcher→Material→

A material used internally for implementing shadow mapping with
point lights. Can also be used to customize the shadow casting of an object by assigning
an instance of MeshDistanceMaterial to Object3D#customDistanceMaterial .
The following examples demonstrates this approach in order to ensure
transparent parts of objects do not cast shadows.

## Constructor
`newMeshDistanceMaterial( parameters :Object)`
Constructs a new mesh distance material.

## Properties
- `.alphaMap :Texture` — The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Only the color of the texture is used, ignoring the alpha channel ...
- `.displacementBias : number` — The offset of the displacement map's values on the mesh's vertices.
The bias is added to the scaled sample of the displacement map.
Without a displacement map set, this value is not applied. Defaul...
- `.displacementMap :Texture` — The displacement map affects the position of the mesh's vertices. Unlike
other maps which only affect the light and shade of the material the
displaced vertices can cast shadows, block other object...
- `.displacementScale : number` — How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement
map set, this value is not applied. Default is 0 .
- `.isMeshDistanceMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.map :Texture` — The color map. May optionally include an alpha channel, typically combined
with Material#transparent or Material#alphaTest . Default is null .

## Source