# WaterMesh
Extends: EventDispatcher→Object3D→Mesh→

A basic flat, reflective water effect. Note that this class can only be used with WebGPURenderer .
When using WebGLRenderer , use Water . References: Flat mirror for three.js An implementation of water shader based on the flat mirror Water shader explanations in WebGL

## Constructor
`newWaterMesh( geometry :BufferGeometry, options :WaterMesh~Options)`
Constructs a new water mesh.

## Import

## Properties
- `.alpha :UniformNode.<float>` — The alpha value. Default is 1 .
- `.distortionScale :UniformNode.<float>` — The distortion scale. Default is 20 .
- `.isWaterMesh : boolean` — This flag can be used for type testing. Default is true .
- `.resolutionScale : number` — The effect's resolution scale. Default is 0.5 .
- `.size :UniformNode.<float>` — The size value. Default is 1 .
- `.sunColor :UniformNode.<color>` — The sun color. Default is 0xffffff .
- `.sunDirection :UniformNode.<vec3>` — The sun direction. Default is (0.70707,0.70707,0.0) .
- `.waterColor :UniformNode.<color>` — The water color. Default is 0x7f7f7f .
- `.waterNormals :TextureNode` — The water's normal map.

## Type Definitions
- `.Options` — Constructor options of WaterMesh .

## Source