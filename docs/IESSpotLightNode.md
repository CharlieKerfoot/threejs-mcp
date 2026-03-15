# IESSpotLightNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→SpotLightNode→

An IES version of the default spot light node.

## Constructor
`newIESSpotLightNode()`

## Methods
- `.getSpotAttenuation( builder :NodeBuilder, angleCosine :Node.<float>) :Node.<float>` — Overwrites the default implementation to compute an IES conform spot attenuation.

## Source