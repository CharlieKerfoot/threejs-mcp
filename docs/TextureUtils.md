# TextureUtils

A class containing utility functions for textures.

## Static Methods
- `.contain( texture :Texture, aspect :number) :Texture` — Scales the texture as large as possible within its surface without cropping
or stretching the texture. The method preserves the original aspect ratio of
the texture. Akin to CSS object-fit: contain
- `.cover( texture :Texture, aspect :number) :Texture` — Scales the texture to the smallest possible size to fill the surface, leaving
no empty space. The method preserves the original aspect ratio of the texture.
Akin to CSS object-fit: cover .
- `.fill( texture :Texture) :Texture` — Configures the texture to the default transformation. Akin to CSS object-fit: fill .
- `.getByteLength( width :number, height :number, format :number, type :number) : number` — Determines how many bytes must be used to represent the texture.

## Source