# VolumeNodeMaterial
Extends: EventDispatcher→Material→NodeMaterial→

Volume node material.

## Constructor
`newVolumeNodeMaterial( parameters :Object)`
Constructs a new volume node material.

## Properties
- `.isVolumeNodeMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.offsetNode :Node.<float>` — Offsets the distance a ray has been traveled through a volume.
Can be used to implement dithering to reduce banding. Default is null .
- `.scatteringNode : function |FunctionNode.<vec4>` — Node used for scattering calculations. Default is null .
- `.steps : number` — Number of steps used for raymarching. Default is 25 .

## Source