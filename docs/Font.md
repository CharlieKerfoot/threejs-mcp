# Font

Class representing a font.

## Constructor
`newFont( data :Object)`
Constructs a new font.

## Properties
- `.data : Object` — The font data as JSON.
- `.isFont : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.generateShapes( text :string, size :number, direction :string) : Array.<Shape>` — Generates geometry shapes from the given text and size. The result of this method
should be used with ShapeGeometry to generate the actual geometry data.

## Source