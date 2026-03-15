# Sky
Extends: EventDispatcher→Object3D→Mesh→

Represents a skydome for scene backgrounds. Based on A Practical Analytic Model for Daylight aka The Preetham Model, the de facto standard for analytical skydomes. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use SkyMesh . More references: http://simonwallner.at/project/atmospheric-scattering/ http://blenderartists.org/forum/showthread.php?245954-preethams-sky-impementation-HDR

## Constructor
`newSky()`
Constructs a new skydome.

## Import

## Properties
- `.isSky : boolean` — This flag can be used for type testing. Default is true .

## Source