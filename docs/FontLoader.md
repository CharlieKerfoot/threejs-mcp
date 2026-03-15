# FontLoader
Extends: Loader→

A loader for loading fonts. You can convert fonts online using facetype.js .

## Constructor
`newFontLoader( manager :LoadingManager)`
Constructs a new font loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded font
to the onLoad() callback.
- `.parse( json :Object) :Font` — Parses the given font data and returns the resulting font.

## Source