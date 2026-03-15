# SkyMesh
Extends: EventDispatcher→Object3D→Mesh→

Represents a skydome for scene backgrounds. Based on A Practical Analytic Model for Daylight aka The Preetham Model, the de facto standard for analytical skydomes. Note that this class can only be used with WebGPURenderer .
When using WebGLRenderer , use Sky . More references: http://simonwallner.at/project/atmospheric-scattering/ http://blenderartists.org/forum/showthread.php?245954-preethams-sky-impementation-HDR

## Constructor
`newSkyMesh()`
Constructs a new skydome.

## Import

## Properties
- `.cloudCoverage :UniformNode.<float>` — The cloud coverage uniform.
- `.cloudDensity :UniformNode.<float>` — The cloud density uniform.
- `.cloudElevation :UniformNode.<float>` — The cloud elevation uniform.
- `.cloudScale :UniformNode.<float>` — The cloud scale uniform.
- `.cloudSpeed :UniformNode.<float>` — The cloud speed uniform.
- `.isSky : boolean` — This flag can be used for type testing. Default is true .
- `.isSkyMesh : boolean` — This flag can be used for type testing. Default is true .
- `.mieCoefficient :UniformNode.<float>` — The mieCoefficient uniform.
- `.mieDirectionalG :UniformNode.<float>` — The mieDirectionalG uniform.
- `.rayleigh :UniformNode.<float>` — The rayleigh uniform.
- `.sunPosition :UniformNode.<vec3>` — The sun position uniform.
- `.turbidity :UniformNode.<float>` — The turbidity uniform.
- `.upUniform :UniformNode.<vec3>` — The up position.

## Source