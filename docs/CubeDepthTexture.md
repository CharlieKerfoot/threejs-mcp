# CubeDepthTexture
Extends: EventDispatcher→Texture→DepthTexture→

This class can be used to automatically save the depth information of a
cube rendering into a cube texture with depth format. Used for PointLight shadows.

## Constructor
`newCubeDepthTexture( size :number, type :number, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, anisotropy :number, format :number)`
Constructs a new cube depth texture.

## Properties
- `.images : Array.<Image>` — Alias for CubeDepthTexture#image .
- `.isCubeDepthTexture : boolean` — This flag can be used for type testing. Default is true .
- `.isCubeTexture : boolean` — Set to true for cube texture handling in WebGLTextures. Default is true .

## Source