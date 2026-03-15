# ProjectorLight
Extends: EventDispatcher→Object3D→Light→SpotLight→

A projector light version of SpotLight . Can only be used with WebGPURenderer .

## Constructor
`newProjectorLight( color :number |Color| string, intensity :number, distance :number, angle :number, penumbra :number, decay :number)`
Constructs a new projector light.

## Properties
- `.aspect : number` — Aspect ratio of the light. Set to null to use the texture aspect ratio. Default is null .

## Source