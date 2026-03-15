# AmbientLight
Extends: EventDispatcher→Object3D→Light→

This light globally illuminates all objects in the scene equally. It cannot be used to cast shadows as it does not have a direction.

## Constructor
`newAmbientLight( color :number |Color| string, intensity :number)`
Constructs a new ambient light.

## Properties
- `.isAmbientLight : boolean` — This flag can be used for type testing. Default is true .

## Source