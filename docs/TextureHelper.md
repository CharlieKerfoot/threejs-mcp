# TextureHelper
Extends: EventDispatcher→Object3D→Mesh→

A helper that can be used to display any type of texture for
debugging purposes. Depending on the type of texture (2D, 3D, Array),
the helper becomes a plane or box mesh. This helper can only be used with WebGLRenderer .
When using WebGPURenderer , import from TextureHelperGPU.js .

## Constructor
`newTextureHelper( texture :Texture, width :number, height :number, depth :number)`
Constructs a new texture helper.

## Import

## Properties
- `.texture :Texture` — The texture to visualize.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source