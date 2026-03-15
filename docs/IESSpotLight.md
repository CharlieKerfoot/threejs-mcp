# IESSpotLight
Extends: EventDispatcher→Object3D→Light→SpotLight→

A IES version of SpotLight . Can only be used with WebGPURenderer .

## Constructor
`newIESSpotLight( color :number |Color| string, intensity :number, distance :number, angle :number, penumbra :number, decay :number)`
Constructs a new IES spot light.

## Properties
- `.iesMap :Texture` — The IES map. It's a lookup table that stores normalized attenuation factors
(0.0 to 1.0) that represent the light's intensity at a specific angle. Default is null .

## Source