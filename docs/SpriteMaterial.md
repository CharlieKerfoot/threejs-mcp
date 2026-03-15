# SpriteMaterial
Extends: EventDispatcher→Material→

A material for rendering instances of Sprite .

## Constructor
`newSpriteMaterial( parameters :Object)`
Constructs a new sprite material.

## Properties
- `.alphaMap :Texture` — The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Only the color of the texture is used, ignoring the alpha channel ...
- `.color :Color` — Color of the material. Default is (1,1,1) .
- `.fog : boolean` — Whether the material is affected by fog or not. Default is true .
- `.isSpriteMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.map :Texture` — The color map. May optionally include an alpha channel, typically combined
with Material#transparent or Material#alphaTest . The texture map
color is modulated by the diffuse color . Default is null .
- `.rotation : number` — The rotation of the sprite in radians. Default is 0 .
- `.sizeAttenuation : boolean` — Specifies whether size of the sprite is attenuated by the camera depth (perspective camera only). Default is true .
- `.transparent : boolean` — Overwritten since sprite materials are transparent
by default. Default is true .

## Source