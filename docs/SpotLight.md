# SpotLight
Extends: EventDispatcher→Object3D→Light→

This light gets emitted from a single point in one direction, along a cone
that increases in size the further from the light it gets. This light can cast shadows - see the SpotLightShadow for details.

## Constructor
`newSpotLight( color :number |Color| string, intensity :number, distance :number, angle :number, penumbra :number, decay :number)`
Constructs a new spot light.

## Properties
- `.angle : number` — Maximum angle of light dispersion from its direction whose upper bound is Math.PI/2 . Default is Math.PI/3 .
- `.decay : number` — The amount the light dims along the distance of the light. In context of
physically-correct rendering the default value should not be changed. Default is 2 .
- `.distance : number` — Maximum range of the light. 0 means no limit. Default is 0 .
- `.isSpotLight : boolean` — This flag can be used for type testing. Default is true .
- `.map :Texture` — A texture used to modulate the color of the light. The spot light
color is mixed with the RGB value of this texture, with a ratio
corresponding to its alpha value. The cookie-like masking effect is...
- `.penumbra : number` — Percent of the spotlight cone that is attenuated due to penumbra.
Value range is [0,1] . Default is 0 .
- `.power : number` — The light's power. Power is the luminous power of the light measured in lumens (lm).
Changing the power will also change the light's intensity.
- `.shadow :SpotLightShadow` — This property holds the light's shadow configuration.
- `.target :Object3D` — The spot light points from its position to the
target's position. For the target's position to be changed to anything other
than the default, it must be added to the scene. It is also possible to s...

## Source