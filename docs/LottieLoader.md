# LottieLoader
Extends: Loader→

A loader for the Lottie texture animation format. The loader returns an instance of CanvasTexture to represent
the animated texture. Two additional properties are added to each texture: animation : The return value of lottie.loadAnimation() which is an object
with an API for controlling the animation's playback. image : The image container.

## Constructor
`newLottieLoader( manager :LoadingManager)`
Constructs a new Lottie loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback) :CanvasTexture` — Starts loading from the given URL and passes the loaded Lottie asset
to the onLoad() callback.
- `.setQuality( value :number)` — Sets the texture quality.

## Source