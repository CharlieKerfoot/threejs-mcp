# CanvasTexture
Extends: EventDispatcher→Texture→

Creates a texture from a canvas element. This is almost the same as the base texture class, except that it sets Texture#needsUpdate to true immediately since a canvas can directly be used for rendering.

## Constructor
`newCanvasTexture( canvas :HTMLCanvasElement, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, format :number, type :number, anisotropy :number)`
Constructs a new texture.

## Properties
- `.isCanvasTexture : boolean` — This flag can be used for type testing. Default is true .

## Source