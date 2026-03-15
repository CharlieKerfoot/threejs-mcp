# RectAreaLight
Extends: EventDispatcher→Object3D→Light→

This class emits light uniformly across the face a rectangular plane.
This light type can be used to simulate light sources such as bright
windows or strip lighting. Important Notes: There is no shadow support. Only PBR materials are supported. You have to include RectAreaLightUniformsLib ( WebGLRenderer ) or RectAreaLightTexturesLib ( WebGPURenderer )
into your app and init the uniforms/textures.

## Constructor
`newRectAreaLight( color :number |Color| string, intensity :number, width :number, height :number)`
Constructs a new area light.

## Properties
- `.height : number` — The height of the light. Default is 10 .
- `.isRectAreaLight : boolean` — This flag can be used for type testing. Default is true .
- `.power : number` — The light's power. Power is the luminous power of the light measured in lumens (lm).
Changing the power will also change the light's intensity.
- `.width : number` — The width of the light. Default is 10 .

## Source