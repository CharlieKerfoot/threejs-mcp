# SpotLightNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→

Module for representing spot lights as nodes.

## Constructor
`newSpotLightNode( light :SpotLight)`
Constructs a new spot light node.

## Properties
- `.colorNode :UniformNode.<Color>` — Uniform node representing the light color.
- `.coneCosNode :UniformNode.<float>` — Uniform node representing the cone cosine.
- `.cutoffDistanceNode :UniformNode.<float>` — Uniform node representing the cutoff distance.
- `.decayExponentNode :UniformNode.<float>` — Uniform node representing the decay exponent.
- `.penumbraCosNode :UniformNode.<float>` — Uniform node representing the penumbra cosine.

## Methods
- `.getSpotAttenuation( builder :NodeBuilder, angleCosine :Node.<float>) :Node.<float>` — Computes the spot attenuation for the given angle.
- `.update( frame :NodeFrame)` — Overwritten to updated spot light specific uniforms.

## Source