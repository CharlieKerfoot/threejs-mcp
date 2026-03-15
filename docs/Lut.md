# Lut

Represents a lookup table for colormaps. It is used to determine the color
values from a range of data values.

## Constructor
`newLut( colormap :'rainbow' | 'cooltowarm' | 'blackbody' | 'grayscale', count :number)`
Constructs a new Lut.

## Import

## Properties
- `.isLut : boolean` — This flag can be used for type testing. Default is true .
- `.lut : Array.<Color>` — The lookup table for the selected color map
- `.map : Array.<Array.<number>>` — The currently selected color map.
- `.maxV : number` — The maximum value to be represented with the lookup table. Default is 1 .
- `.minV : number` — The minimum value to be represented with the lookup table. Default is 0 .
- `.n : number` — The number of colors of the current selected color map. Default is 32 .

## Methods
- `.addColorMap( name :string, arrayOfColors :Array.<Array.<number>>) :Lut` — Adds a color map to this Lut instance.
- `.copy( lut :Lut) :Lut` — Copies the given lut.
- `.createCanvas() : HTMLCanvasElement` — Creates a canvas in order to visualize the lookup table as a texture.
- `.getColor( alpha :number) :Color` — Returns an instance of Color for the given data value.
- `.set( value :Lut) :Lut` — Sets the given LUT.
- `.setColorMap( colormap :string, count :number) :Lut` — Configure the lookup table for the given color map and number of colors.
- `.setMax( max :number) :Lut` — Sets the maximum value to be represented with this LUT.
- `.setMin( min :number) :Lut` — Sets the minimum value to be represented with this LUT.
- `.updateCanvas( canvas :HTMLCanvasElement) : HTMLCanvasElement` — Updates the given canvas with the Lut's data.

## Source