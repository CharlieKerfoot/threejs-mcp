# Water
Extends: EventDispatcher→Object3D→Mesh→

A basic flat, reflective water effect. Note that this class can only be used with WebGLRenderer .
When using WebGPURenderer , use WaterMesh . References: Flat mirror for three.js An implementation of water shader based on the flat mirror Water shader explanations in WebGL

## Constructor
`newWater( geometry :BufferGeometry, options :Water~Options)`
Constructs a new water instance.

## Import

## Properties
- `.isWater : boolean` — This flag can be used for type testing. Default is true .

## Type Definitions
- `.Options` — Constructor options of Water .

## Source