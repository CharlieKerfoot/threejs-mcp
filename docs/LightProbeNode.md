# LightProbeNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→

Module for representing light probes as nodes.

## Constructor
`newLightProbeNode( light :LightProbe)`
Constructs a new light probe node.

## Properties
- `.lightProbe :UniformArrayNode` — Light probe represented as a uniform of spherical harmonics.

## Methods
- `.update( frame :NodeFrame)` — Overwritten to updated light probe specific uniforms.

## Source