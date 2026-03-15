# HemisphereLight
Extends: EventDispatcher→Object3D→Light→

A light source positioned directly above the scene, with color fading from
the sky color to the ground color. This light cannot be used to cast shadows.

## Constructor
`newHemisphereLight( skyColor :number |Color| string, groundColor :number |Color| string, intensity :number)`
Constructs a new hemisphere light.

## Properties
- `.groundColor :Color` — The light's ground color.
- `.isHemisphereLight : boolean` — This flag can be used for type testing. Default is true .

## Source