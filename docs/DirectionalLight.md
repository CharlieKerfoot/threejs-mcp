# DirectionalLight
Extends: EventDispatcher→Object3D→Light→

A light that gets emitted in a specific direction. This light will behave
as though it is infinitely far away and the rays produced from it are all
parallel. The common use case for this is to simulate daylight; the sun is
far enough away that its position can be considered to be infinite, and
all light rays coming from it are parallel. A common point of confusion for directional lights is that setting the
rotation has no effect. This is because three.js's DirectionalLight is the
equivalent to what is often called a 'Target Direct Light' in other
applications. This means that its direction is calculated as pointing from the light's Object3D#position to the DirectionalLight#target position
(as opposed to a 'Free Direct Light' that just has a rotation
component). This light can cast shadows - see the DirectionalLightShadow for details.

## Constructor
`newDirectionalLight( color :number |Color| string, intensity :number)`
Constructs a new directional light.

## Properties
- `.isDirectionalLight : boolean` — This flag can be used for type testing. Default is true .
- `.shadow :DirectionalLightShadow` — This property holds the light's shadow configuration.
- `.target :Object3D` — The directional light points from its position to the
target's position. For the target's position to be changed to anything other
than the default, it must be added to the scene. It is also possib...

## Source