# ImageLoader
Extends: Loader→

A loader for loading images. The class loads images with the HTML Image API. Please note that ImageLoader has dropped support for progress
events in r84 . For an ImageLoader that supports progress events, see this thread .

## Constructor
`newImageLoader( manager :LoadingManager)`
Constructs a new image loader.

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) : Image` — Starts loading from the given URL and passes the loaded image
to the onLoad() callback. The method also returns a new Image object which can
directly be used for texture creation. If you do it this...

## Source