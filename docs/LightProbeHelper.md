# LightProbeHelper
Extends: EventDispatcher→Object3D→Mesh→

Renders a sphere to visualize a light probe in the scene. This helper can only be used with WebGLRenderer .
When using WebGPURenderer , import from LightProbeHelperGPU.js .

## Constructor
`newLightProbeHelper( lightProbe :LightProbe, size :number)`
Constructs a new light probe helper.

## Import

## Properties
- `.lightProbe :LightProbe` — The light probe to visualize.
- `.size : number` — The size of the helper. Default is 1 .

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source