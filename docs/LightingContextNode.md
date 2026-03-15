# LightingContextNode
Extends: EventDispatcher→Node→ContextNode→

LightingContextNode represents an extension of the ContextNode module
by adding lighting specific context data. It represents the runtime context of LightsNode .

## Constructor
`newLightingContextNode( lightsNode :LightsNode, lightingModel :LightingModel, backdropNode :Node.<vec3>, backdropAlphaNode :Node.<float>)`
Constructs a new lighting context node.

## Properties
- `.backdropAlphaNode :Node.<float>` — A backdrop alpha node. Default is null .
- `.backdropNode :Node.<vec3>` — A backdrop node. Default is null .
- `.lightingModel :LightingModel` — The current lighting model. Default is null .

## Methods
- `.getContext() : Object` — Returns a lighting context object.

## Source