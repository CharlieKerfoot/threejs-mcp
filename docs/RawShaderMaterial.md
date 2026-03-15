# RawShaderMaterial
Extends: EventDispatcher→Material→ShaderMaterial→

This class works just like ShaderMaterial , except that definitions
of built-in uniforms and attributes are not automatically prepended to the
GLSL shader code. RawShaderMaterial can only be used with WebGLRenderer .

## Constructor
`newRawShaderMaterial( parameters :Object)`
Constructs a new raw shader material.

## Properties
- `.isRawShaderMaterial : boolean` — This flag can be used for type testing. Default is true .

## Source