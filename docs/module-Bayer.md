# Bayer

## Import

## Static Methods
- `.bayer16( uv :Node.<vec2>) :Node.<vec4>` — This TSL function can be used to sample a Bayer16 texture which is a 16x16 texture with a Bayer Matrix pattern.
It can be used for dithering effects but also as an alternative to blue-noise. When u...
- `.bayerDither( color :Node.<vec3>, steps :Node.<float>) :Node.<vec3>` — This TSL function applies Bayer dithering to a color input. It uses a 4x4 Bayer matrix
pattern to add structured noise before color quantization, which helps reduce visible
color banding when limit...

## Source