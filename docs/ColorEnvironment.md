# ColorEnvironment
Extends: EventDispatcher→Object3D→Scene→

This class represents a scene with a uniform color that can be used as
input for PMREMGenerator#fromScene . The resulting PMREM represents
uniform ambient lighting and can be used for Image Based Lighting by
assigning it to Scene#environment .

## Constructor
`newColorEnvironment( color :number |Color)`
Constructs a new color environment.

## Import

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the environment is no longer required.

## Source