# LineDashedNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Node material version of LineDashedMaterial .

## Constructor
`newLineDashedNodeMaterial( parameters :Object)`
Constructs a new line dashed node material.

## Properties
- `.dashOffset : number` — The dash offset. Default is 0 .
- `.dashScaleNode :Node.<float>` — The scale of dash materials is by default inferred from the scale property. This node property allows to overwrite the default
and define the scale with a node instead. If you don't want to overwri...
- `.dashSizeNode :Node.<float>` — The dash size of dash materials is by default inferred from the dashSize property. This node property allows to overwrite the default
and define the dash size with a node instead. If you don't want...
- `.gapSizeNode :Node.<float>` — The gap size of dash materials is by default inferred from the gapSize property. This node property allows to overwrite the default
and define the gap size with a node instead. If you don't want to...
- `.isLineDashedNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.offsetNode :Node.<float>` — The offset of dash materials is by default inferred from the dashOffset property. This node property allows to overwrite the default
and define the offset with a node instead. If you don't want to ...

## Methods
- `.setupVariants( builder :NodeBuilder)` — Setups the dash specific node variables.

## Source