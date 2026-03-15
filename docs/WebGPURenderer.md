# WebGPURenderer
Extends: Renderer→

This renderer is the new alternative of WebGLRenderer . WebGPURenderer has the ability
to target different backends. By default, the renderer tries to use a WebGPU backend if the
browser supports WebGPU. If not, WebGPURenderer falls backs to a WebGL 2 backend.

## Constructor
`newWebGPURenderer( parameters :WebGPURenderer~Options)`
Constructs a new WebGPU renderer.

## Properties
- `.isWebGPURenderer : boolean` — This flag can be used for type testing. Default is true .
- `.library :StandardNodeLibrary` — The generic default value is overwritten with the
standard node library for type mapping.

## Type Definitions
- `.Options` — WebGPURenderer options.

## Source