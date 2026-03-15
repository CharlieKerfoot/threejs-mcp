# Color

A Color instance is represented by RGB components in the linear working
color space , which defaults to LinearSRGBColorSpace . Inputs
conventionally using SRGBColorSpace (such as hexadecimals and CSS
strings) are converted to the working color space automatically. Source color spaces may be specified explicitly, to ensure correct conversions. // assumed already LinearSRGBColorSpace; no conversion
const color = new THREE.Color().setRGB( 0.5, 0.5, 0.5 );
// converted explicitly from SRGBColorSpace to LinearSRGBColorSpace
const color = new THREE.Color().setRGB( 0.5, 0.5, 0.5, SRGBColorSpace ); If THREE.ColorManagement is disabled, no conversions occur. For details,
see Color management . Iterating through a Color instance will yield
its components (r, g, b) in the corresponding order. A Color can be initialised
in any of the following ways: //empty constructor - will default white
const color1 = new THREE.Color();
//Hexadecimal color (recommended)
const color2 = new THREE.Color( 0xff0000 );
//RGB string
const color3 = new THREE.Color("rgb(255, 0, 0)");
const color4 = new THREE.Color("rgb(100%, 0%, 0%)");
//X11 color name - all 140 color names are supported.
//Note the lack of CamelCase in the name
const color5 = new THREE.Color( 'skyblue' );
//HSL string
const color6 = new THREE.Color("hsl(0, 100%, 50%)");
//Separate RGB values between 0 and 1
const color7 = new THREE.Color( 1, 0, 0 );

## Constructor
`newColor( r :number | string |Color, g :number, b :number)`
Constructs a new color. Note that standard method of specifying color in three.js is with a hexadecimal triplet,
and that method is used throughout the rest of the documentation.

## Properties
- `.b : number` — The blue component. Default is 1 .
- `.g : number` — The green component. Default is 1 .
- `.isColor : boolean` — This flag can be used for type testing. Default is true .
- `.r : number` — The red component. Default is 1 .
- `.NAMES : Object` — A dictionary with X11 color names. Note that multiple words such as Dark Orange become the string 'darkorange'.

## Methods
- `.add( color :Color) :Color` — Adds the RGB values of the given color to the RGB values of this color.
- `.addColors( color1 :Color, color2 :Color) :Color` — Adds the RGB values of the given colors and stores the result in this instance.
- `.addScalar( s :number) :Color` — Adds the given scalar value to the RGB values of this color.
- `.applyMatrix3( m :Matrix3) :Color` — Transforms this color with the given 3x3 matrix.
- `.clone() :Color` — Returns a new color with copied values from this instance.
- `.convertLinearToSRGB() :Color` — Converts this color from LinearSRGBColorSpace to SRGBColorSpace .
- `.convertSRGBToLinear() :Color` — Converts this color from SRGBColorSpace to LinearSRGBColorSpace .
- `.copy( color :Color) :Color` — Copies the values of the given color to this instance.
- `.copyLinearToSRGB( color :Color) :Color` — Copies the given color into this color, and then converts this color from LinearSRGBColorSpace to SRGBColorSpace .
- `.copySRGBToLinear( color :Color) :Color` — Copies the given color into this color, and then converts this color from SRGBColorSpace to LinearSRGBColorSpace .
- `.equals( c :Color) : boolean` — Returns true if this color is equal with the given one.
- `.fromArray( array :Array.<number>, offset :number) :Color` — Sets this color's RGB components from the given array.
- `.fromBufferAttribute( attribute :BufferAttribute, index :number) :Color` — Sets the components of this color from the given buffer attribute.
- `.getHSL( target :Object, colorSpace :string) : Object` — Converts the colors RGB values into the HSL format and stores them into the
given target object.
- `.getHex( colorSpace :string) : number` — Returns the hexadecimal value of this color.
- `.getHexString( colorSpace :string) : string` — Returns the hexadecimal value of this color as a string (for example, 'FFFFFF').
- `.getRGB( target :Color, colorSpace :string) :Color` — Returns the RGB values of this color and stores them into the given target object.
- `.getStyle( colorSpace :string) : string` — Returns the value of this color as a CSS style string. Example: rgb(255,0,0) .
- `.lerp( color :Color, alpha :number) :Color` — Linearly interpolates this color's RGB values toward the RGB values of the
given color. The alpha argument can be thought of as the ratio between
the two colors, where 0.0 is this color and 1.0 is ...
- `.lerpColors( color1 :Color, color2 :Color, alpha :number) :Color` — Linearly interpolates between the given colors and stores the result in this instance.
The alpha argument can be thought of as the ratio between the two colors, where 0.0 is the first and 1.0 is th...
- `.lerpHSL( color :Color, alpha :number) :Color` — Linearly interpolates this color's HSL values toward the HSL values of the
given color. It differs from Color#lerp by not interpolating straight
from one color to the other, but instead going throu...
- `.multiply( color :Color) :Color` — Multiplies the RGB values of the given color with the RGB values of this color.
- `.multiplyScalar( s :number) :Color` — Multiplies the given scalar value with the RGB values of this color.
- `.offsetHSL( h :number, s :number, l :number) :Color` — Adds the given HSL values to this color's values.
Internally, this converts the color's RGB values to HSL, adds HSL
and then converts the color back to RGB.
- `.set( r :number | string |Color, g :number, b :number) :Color` — Sets the colors's components from the given values.
- `.setColorName( style :string, colorSpace :string) :Color` — Sets this color from a color name. Faster than Color#setStyle if
you don't need the other CSS-style formats. For convenience, the list of names is exposed in Color.NAMES as a hash. Color.NAMES.alic...
- `.setFromVector3( v :Vector3) :Color` — Sets the color's RGB components from the given 3D vector.
- `.setHSL( h :number, s :number, l :number, colorSpace :string) :Color` — Sets this color from RGB values.
- `.setHex( hex :number, colorSpace :string) :Color` — Sets this color from a hexadecimal value.
- `.setRGB( r :number, g :number, b :number, colorSpace :string) :Color` — Sets this color from RGB values.
- `.setScalar( scalar :number) :Color` — Sets the colors's components to the given scalar value.
- `.setStyle( style :string, colorSpace :string) :Color` — Sets this color from a CSS-style string. For example, rgb(250, 0,0) , rgb(100%, 0%, 0%) , hsl(0, 100%, 50%) , #ff0000 , #f00 , or red ( or
any X11 color name -
all 140 color names are supported).
- `.sub( color :Color) :Color` — Subtracts the RGB values of the given color from the RGB values of this color.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the RGB components of this color to the given array. If no array is provided,
the method returns a new instance.
- `.toJSON() : number` — This methods defines the serialization result of this class. Returns the color
as a hexadecimal value.

## Source