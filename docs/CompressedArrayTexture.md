# CompressedArrayTexture
Extends: EventDispatcher→Texture→CompressedTexture→

Creates a texture 2D array based on data in compressed form. These texture are usually loaded with CompressedTextureLoader .

## Constructor
`newCompressedArrayTexture( mipmaps :Array.<Object>, width :number, height :number, depth :number, format :number, type :number)`
Constructs a new compressed array texture.

## Properties
- `.image : Object` — The image property of a compressed texture just defines its dimensions.
- `.isCompressedArrayTexture : boolean` — This flag can be used for type testing. Default is true .
- `.layerUpdates : Set.<number>` — A set of all layers which need to be updated in the texture.
- `.wrapR :RepeatWrapping|ClampToEdgeWrapping|MirroredRepeatWrapping` — This defines how the texture is wrapped in the depth and corresponds to W in UVW mapping. Default is ClampToEdgeWrapping .

## Methods
- `.addLayerUpdate( layerIndex :number)` — Describes that a specific layer of the texture needs to be updated.
Normally when Texture#needsUpdate is set to true , the
entire compressed texture array is sent to the GPU. Marking specific
layer...
- `.clearLayerUpdates()` — Resets the layer updates registry.

## Source