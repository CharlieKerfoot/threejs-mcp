# Texture
Extends: EventDispatcher→

Base class for all textures. Note: After the initial use of a texture, its dimensions, format, and type
cannot be changed. Instead, call Texture#dispose on the texture and instantiate a new one.

## Constructor
`newTexture( image :Object, mapping :number, wrapS :number, wrapT :number, magFilter :number, minFilter :number, format :number, type :number, anisotropy :number, colorSpace :string)`
Constructs a new texture.

## Properties
- `.anisotropy : number` — The number of samples taken along the axis through the pixel that has the
highest density of texels. By default, this value is 1 . A higher value
gives a less blurry result than a basic mipmap, at ...
- `.center :Vector2` — The point around which rotation occurs. A value of (0.5, 0.5) corresponds
to the center of the texture. Default is (0, 0) , the lower left. Default is (0,0) .
- `.channel : number` — Lets you select the uv attribute to map the texture to. 0 for uv , 1 for uv1 , 2 for uv2 and 3 for uv3 . Default is 0 .
- `.colorSpace : string` — Textures containing color data should be annotated with SRGBColorSpace or LinearSRGBColorSpace . Default is NoColorSpace .
- `.depth` — The depth of the texture in pixels.
- `.flipY : boolean` — If set to true , the texture is flipped along the vertical axis when
uploaded to the GPU. Note that this property has no effect when using ImageBitmap . You need to
configure the flip on bitmap cre...
- `.format : number` — The format of the texture. Default is RGBAFormat .
- `.generateMipmaps : boolean` — Whether to generate mipmaps (if possible) for a texture. Set this to false if you are creating mipmaps manually. Default is true .
- `.height` — The height of the texture in pixels.
- `.id : number` — The ID of the texture.
- `.image : Object` — The image object holding the texture data.
- `.internalFormat : string` — The default internal format is derived from Texture#format and Texture#type and
defines how the texture data is going to be stored on the GPU. This property allows to overwrite the default format. ...
- `.isArrayTexture : boolean` — Indicates if a texture should be handled like a texture array. Default is false .
- `.isRenderTargetTexture : boolean` — Indicates whether a texture belongs to a render target or not. Default is false .
- `.isTexture : boolean` — This flag can be used for type testing. Default is true .
- `.magFilter :NearestFilter|NearestMipmapNearestFilter|NearestMipmapLinearFilter|LinearFilter|LinearMipmapNearestFilter|LinearMipmapLinearFilter` — How the texture is sampled when a texel covers more than one pixel. Default is LinearFilter .
- `.mapping :UVMapping|CubeReflectionMapping|CubeRefractionMapping|EquirectangularReflectionMapping|EquirectangularRefractionMapping|CubeUVReflectionMapping` — How the texture is applied to the object. The value UVMapping is the default, where texture or uv coordinates are used to apply the map. Default is UVMapping .
- `.matrix :Matrix3` — The uv-transformation matrix of the texture.
- `.matrixAutoUpdate : boolean` — Whether to update the texture's uv-transformation Texture#matrix from the properties Texture#offset , Texture#repeat , Texture#rotation , and Texture#center . Set this to false if you are specifyin...
- `.minFilter :NearestFilter|NearestMipmapNearestFilter|NearestMipmapLinearFilter|LinearFilter|LinearMipmapNearestFilter|LinearMipmapLinearFilter` — How the texture is sampled when a texel covers less than one pixel. Default is LinearMipmapLinearFilter .
- `.mipmaps : Array.<Object>` — An array holding user-defined mipmaps.
- `.name : string` — The name of the texture.
- `.needsPMREMUpdate : boolean` — Setting this property to true indicates the engine the PMREM
must be regenerated. Default is false .
- `.needsUpdate : boolean` — Setting this property to true indicates the engine the texture
must be updated in the next render. This triggers a texture upload
to the GPU and ensures correct texture parameter configuration. Def...
- `.offset :Vector2` — How much a single repetition of the texture is offset from the beginning,
in each direction U and V. Typical range is 0.0 to 1.0 . Default is (0,0) .
- `.onUpdate : function` — A callback function, called when the texture is updated (e.g., when Texture#needsUpdate has been set to true and then the texture is used). Default is null .
- `.pmremVersion : number` — Indicates whether this texture should be processed by PMREMGenerator or not
(only relevant for render target textures). Default is 0 .
- `.premultiplyAlpha : boolean` — If set to true , the alpha channel, if present, is multiplied into the
color channels when the texture is uploaded to the GPU. Note that this property has no effect when using ImageBitmap . You nee...
- `.renderTarget :RenderTarget|WebGLRenderTarget` — An optional back reference to the textures render target. Default is null .
- `.repeat :Vector2` — How many times the texture is repeated across the surface, in each
direction U and V. If repeat is set greater than 1 in either direction,
the corresponding wrap parameter should also be set to Rep...
- `.rotation : number` — How much the texture is rotated around the center point, in radians.
Positive values are counter-clockwise. Default is 0 .
- `.source :Source` — The data definition of a texture. A reference to the data source can be
shared across textures. This is often useful in context of spritesheets
where multiple textures render the same data but with...
- `.type : number` — The data type of the texture. Default is UnsignedByteType .
- `.unpackAlignment : number` — Specifies the alignment requirements for the start of each pixel row in memory.
The allowable values are 1 (byte-alignment), 2 (rows aligned to even-numbered bytes), 4 (word-alignment), and 8 (rows...
- `.updateRanges : Array.<Object>` — This can be used to only update a subregion or specific rows of the texture (for example, just the
first 3 rows). Use the addUpdateRange() function to add ranges to this array.
- `.userData : Object` — An object that can be used to store custom data about the texture. It
should not hold references to functions as these will not be cloned.
- `.uuid : string` — The UUID of the texture.
- `.version : number` — This starts at 0 and counts how many times Texture#needsUpdate is set to true . Default is 0 .
- `.width` — The width of the texture in pixels.
- `.wrapS :RepeatWrapping|ClampToEdgeWrapping|MirroredRepeatWrapping` — This defines how the texture is wrapped horizontally and corresponds to U in UV mapping. Default is ClampToEdgeWrapping .
- `.wrapT :RepeatWrapping|ClampToEdgeWrapping|MirroredRepeatWrapping` — This defines how the texture is wrapped horizontally and corresponds to V in UV mapping. Default is ClampToEdgeWrapping .
- `.DEFAULT_ANISOTROPY : number` — The default anisotropy value for all textures. Default is 1 .
- `.DEFAULT_IMAGE : Image` — The default image for all textures. Default is null .
- `.DEFAULT_MAPPING : number` — The default mapping for all textures. Default is UVMapping .

## Methods
- `.addUpdateRange( start :number, count :number)` — Adds a range of data in the data texture to be updated on the GPU.
- `.clearUpdateRanges()` — Clears the update ranges.
- `.clone() :Texture` — Returns a new texture with copied values from this instance.
- `.copy( source :Texture) :Texture` — Copies the values of the given texture to this instance.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.setValues( values :Object)` — Sets this texture's properties based on values .
- `.toJSON( meta :Object | string) : Object` — Serializes the texture into JSON.
- `.transformUv( uv :Vector2) :Vector2` — Transforms the given uv vector with the textures uv transformation matrix.
- `.updateMatrix()` — Updates the texture transformation matrix from the from the properties Texture#offset , Texture#repeat , Texture#rotation , and Texture#center .

## Events
- `.dispose` — Fires when the texture has been disposed of.

## Source