# HemisphereLightNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→

Module for representing hemisphere lights as nodes.

## Constructor
`newHemisphereLightNode( light :HemisphereLight)`
Constructs a new hemisphere light node.

## Properties
- `.groundColorNode :UniformNode.<vec3>` — Uniform node representing the light's ground color.
- `.lightDirectionNode :Node.<vec3>` — A node representing the light's direction.
- `.lightPositionNode :UniformNode.<vec3>` — Uniform node representing the light's position.

## Methods
- `.update( frame :NodeFrame)` — Overwritten to updated hemisphere light specific uniforms.

## Source