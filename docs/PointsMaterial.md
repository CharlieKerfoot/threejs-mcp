# PointsMaterial
Extends: EventDispatcher→Material→

A material for rendering point primitives. Materials define the appearance of renderable 3D objects.

## Constructor
`newPointsMaterial( parameters :Object)`
Constructs a new points material.

## Properties
- `.alphaMap :Texture` — The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Only the color of the texture is used, ignoring the alpha channel ...
- `.color :Color` — Color of the material. Default is (1,1,1) .
- `.fog : boolean` — Whether the material is affected by fog or not. Default is true .
- `.isPointsMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.map :Texture` — The color map. May optionally include an alpha channel, typically combined
with Material#transparent or Material#alphaTest . The texture map
color is modulated by the diffuse color . Default is null .
- `.size : number` — Defines the size of the points in pixels. Might be capped if the value exceeds hardware dependent parameters like gl.ALIASED_POINT_SIZE_RANGE . Default is 1 .
- `.sizeAttenuation : boolean` — Specifies whether size of individual points is attenuated by the camera depth (perspective camera only). Default is true .

## Source