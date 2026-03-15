# PointLight
Extends: EventDispatcher→Object3D→Light→

A light that gets emitted from a single point in all directions. A common
use case for this is to replicate the light emitted from a bare
lightbulb. This light can cast shadows - see the PointLightShadow for details.

## Constructor
`newPointLight( color :number |Color| string, intensity :number, distance :number, decay :number)`
Constructs a new point light.

## Properties
- `.decay : number` — The amount the light dims along the distance of the light. In context of
physically-correct rendering the default value should not be changed. Default is 2 .
- `.distance : number` — When distance is zero, light will attenuate according to inverse-square
law to infinite distance. When distance is non-zero, light will attenuate
according to inverse-square law until near the dist...
- `.isPointLight : boolean` — This flag can be used for type testing. Default is true .
- `.power : number` — The light's power. Power is the luminous power of the light measured in lumens (lm).
Changing the power will also change the light's intensity.
- `.shadow :PointLightShadow` — This property holds the light's shadow configuration.

## Source