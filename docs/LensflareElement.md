# LensflareElement

Represents a single flare that can be added to a Lensflare container.

## Constructor
`newLensflareElement( texture :Texture, size :number, distance :number, color :Color)`
Constructs a new lensflare element.

## Import

## Properties
- `.color :Color` — The flare's color Default is (1,1,1) .
- `.distance : number` — The normalized distance ( [0,1] ) from the light source.
A value of 0 means the flare is located at light source. Default is 0 .
- `.size : number` — The size in pixels. Default is 1 .
- `.texture :Texture` — The flare's texture.

## Source