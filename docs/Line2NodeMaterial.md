# Line2NodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

This node material can be used to render lines with a size larger than one
by representing them as instanced meshes.

## Constructor
`newLine2NodeMaterial( parameters :Object)`
Constructs a new node material for wide line rendering.

## Properties
- `.alphaToCoverage : boolean` — Whether alpha to coverage should be used or not. Default is true .
- `.blending : number` — Blending is set to NoBlending since transparency
is not supported, yet. Default is 0 .
- `.dashOffset : number` — The dash offset. Default is 0 .
- `.dashScaleNode :Node.<float>` — Defines the dash scale. Default is null .
- `.dashSizeNode :Node.<float>` — Defines the dash size. Default is null .
- `.dashed : boolean` — Whether the lines should be dashed or not. Default is false .
- `.gapSizeNode :Node.<float>` — Defines the gap size. Default is null .
- `.isLine2NodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lineColorNode :Node.<vec3>` — Defines the lines color. Default is null .
- `.offsetNode :Node.<float>` — Defines the offset. Default is null .
- `.vertexColors : boolean` — Whether vertex colors should be used or not. Default is false .
- `.worldUnits : boolean` — Whether the lines should sized in world units or not.
When set to false the unit is pixel. Default is false .

## Methods
- `.setup( builder :NodeBuilder)` — Setups the vertex and fragment stage of this node material.

## Source