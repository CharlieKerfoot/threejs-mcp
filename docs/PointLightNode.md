# PointLightNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→

Module for representing point lights as nodes.

## Constructor
`newPointLightNode( light :PointLight)`
Constructs a new point light node.

## Properties
- `.cutoffDistanceNode :UniformNode.<float>` — Uniform node representing the cutoff distance.
- `.decayExponentNode :UniformNode.<float>` — Uniform node representing the decay exponent.

## Methods
- `.setupShadowNode() :PointShadowNode` — Overwritten to setup point light specific shadow.
- `.update( frame :NodeFrame)` — Overwritten to updated point light specific uniforms.

## Source