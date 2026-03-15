# LineBasicMaterial
Extends: EventDispatcher→Material→

A material for rendering line primitives. Materials define the appearance of renderable 3D objects.

## Constructor
`newLineBasicMaterial( parameters :Object)`
Constructs a new line basic material.

## Properties
- `.color :Color` — Color of the material. Default is (1,1,1) .
- `.fog : boolean` — Whether the material is affected by fog or not. Default is true .
- `.isLineBasicMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.linecap : 'butt' | 'round' | 'square'` — Defines appearance of line ends. Can only be used with SVGRenderer . Default is 'round' .
- `.linejoin : 'round' | 'bevel' | 'miter'` — Defines appearance of line joints. Can only be used with SVGRenderer . Default is 'round' .
- `.linewidth : number` — Controls line thickness or lines. Can only be used with SVGRenderer . WebGL and WebGPU
ignore this setting and always render line primitives with a
width of one pixel. Default is 1 .
- `.map :Texture` — Sets the color of the lines using data from a texture. The texture map
color is modulated by the diffuse color . Default is null .

## Source