# LineMaterial
Extends: EventDispatcher→Material→ShaderMaterial→

A material for drawing wireframe-style geometries. Unlike LineBasicMaterial , it supports arbitrary line widths and allows using world units
instead of screen space units. This material is used with LineSegments2 and Line2 . This module can only be used with WebGLRenderer . When using WebGPURenderer ,
use Line2NodeMaterial .

## Constructor
`newLineMaterial( parameters :Object)`
Constructs a new line segments geometry.

## Import

## Properties
- `.alphaToCoverage : boolean` — Whether to use alphaToCoverage or not. When enabled, this can improve the
anti-aliasing of line edges when using MSAA.
- `.color :Color` — The material's color. Default is (1,1,1) .
- `.dashOffset : number` — Where in the dash cycle the dash starts. Default is 0 .
- `.dashScale : number` — The scale of the dashes and gaps. Default is 1 .
- `.dashSize : number` — The size of the dash. Default is 1 .
- `.dashed : boolean` — Whether the line is dashed, or solid. Default is false .
- `.gapSize : number` — The size of the gap. Default is 0 .
- `.isLineMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.linewidth : number` — Controls line thickness in CSS pixel units when worldUnits is false (default),
or in world units when worldUnits is true . Default is 1 .
- `.opacity : number` — The opacity. Default is 1 .
- `.resolution :Vector2` — The size of the viewport, in screen pixels. This must be kept updated to make
screen-space rendering accurate.The LineSegments2.onBeforeRender callback
performs the update for visible objects.
- `.worldUnits : boolean` — Whether the material's sizes (width, dash gaps) are in world units. Default is false .

## Source