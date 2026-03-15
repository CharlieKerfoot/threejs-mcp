# LineDashedMaterial
Extends: EventDispatcher→Material→LineBasicMaterial→

A material for rendering line primitives. Materials define the appearance of renderable 3D objects.

## Constructor
`newLineDashedMaterial( parameters :Object)`
Constructs a new line dashed material.

## Properties
- `.dashSize : number` — The size of the dash. This is both the gap with the stroke. Default is 3 .
- `.gapSize : number` — The size of the gap. Default is 1 .
- `.isLineDashedMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.scale : number` — The scale of the dashed part of a line. Default is 1 .

## Source