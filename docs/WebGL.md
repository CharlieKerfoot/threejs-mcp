# WebGL

A utility module with basic WebGL 2 capability testing.

## Import

## Static Methods
- `.getWebGL2ErrorMessage() : HTMLDivElement` — Returns a div element representing a formatted error message that can be appended in
web sites if WebGL 2 isn't supported.
- `.isColorSpaceAvailable( colorSpace :string) : boolean` — Returns true if the given color space is available. This method can only be used
if WebGL 2 is supported.
- `.isWebGL2Available() : boolean` — Returns true if WebGL 2 is available.

## Source