# VideoFrameTexture
Extends: EventDispatcher→Texture→VideoTexture→

This class can be used as an alternative way to define video data. Instead of using
an instance of HTMLVideoElement like with VideoTexture , VideoFrameTexture expects each frame is
defined manually via VideoFrameTexture#setFrame . A typical use case for this module is when
video frames are decoded with the WebCodecs API.

## Constructor
`newVideoFrameTexture( mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, format :number, type :number, anisotropy :number)`
Constructs a new video frame texture.

## Properties
- `.isVideoFrameTexture : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.setFrame( frame :VideoFrame)` — Sets the current frame of the video. This will automatically update the texture
so the data can be used for rendering.
- `.update()` — This method overwritten with an empty implementation since
this type of texture is updated via setFrame() .

## Source