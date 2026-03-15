# ImageBitmapLoader
Extends: Loader→

A loader for loading images as an ImageBitmap .
An ImageBitmap provides an asynchronous and resource efficient pathway to prepare
textures for rendering. Note that Texture#flipY and Texture#premultiplyAlpha are ignored with image bitmaps.
These options need to be configured via ImageBitmapLoader#setOptions prior to loading,
unlike regular images which can be configured on the Texture to set these options on GPU upload instead. To match the default behaviour of Texture , the following options are needed: Also note that unlike FileLoader , this loader will only avoid multiple concurrent requests to the same URL if Cache is enabled. const loader = new THREE.ImageBitmapLoader();
loader.setOptions( { imageOrientation: 'flipY' } ); // set options if needed
const imageBitmap = await loader.loadAsync( 'image.png' );
const texture = new THREE.Texture( imageBitmap );
texture.needsUpdate = true;

## Constructor
`newImageBitmapLoader( manager :LoadingManager)`
Constructs a new image bitmap loader.

## Properties
- `.isImageBitmapLoader : boolean` — This flag can be used for type testing. Default is true .
- `.options : Object` — Represents the loader options. Default is {premultiplyAlpha:'none'} .

## Methods
- `.abort() :ImageBitmapLoader` — Aborts ongoing fetch requests.
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) : ImageBitmap | undefined` — Starts loading from the given URL and pass the loaded image bitmap to the onLoad() callback.
- `.setOptions( options :Object) :ImageBitmapLoader` — Sets the given loader options. The structure of the object must match the options parameter of createImageBitmap .

## Source