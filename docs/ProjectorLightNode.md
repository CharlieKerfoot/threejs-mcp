# ProjectorLightNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→SpotLightNode→

An implementation of a projector light node.

## Constructor
`newProjectorLightNode()`

## Methods
- `.getSpotAttenuation( builder :NodeBuilder) :Node.<float>` — Overwrites the default implementation to compute projection attenuation.

## Source