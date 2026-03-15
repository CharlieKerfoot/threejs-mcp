# RectAreaLightNode
Extends: EventDispatcher→Node→LightingNode→AnalyticLightNode→

Module for representing rect area lights as nodes.

## Constructor
`newRectAreaLightNode( light :RectAreaLight)`
Constructs a new rect area light node.

## Properties
- `.halfHeight :UniformNode.<vec3>` — Uniform node representing the half height of the are light.
- `.halfWidth :UniformNode.<vec3>` — Uniform node representing the half width of the are light.
- `.updateType : string` — The updateType is set to NodeUpdateType.RENDER since the light
relies on viewMatrix which might vary per render call. Default is 'render' .

## Methods
- `.update( frame :NodeFrame)` — Overwritten to updated rect area light specific uniforms.

## Static Methods
- `.setLTC( ltc :RectAreaLightTexturesLib)` — Used to configure the internal BRDF approximation texture data.

## Source