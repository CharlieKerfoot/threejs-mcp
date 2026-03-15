# Skeleton

Class for representing the armatures in three.js . The skeleton
is defined by a hierarchy of bones.

## Constructor
`newSkeleton( bones :Array.<Bone>, boneInverses :Array.<Matrix4>)`
Constructs a new skeleton.

## Properties
- `.boneInverses : Array.<Matrix4>` — An array of bone inverse matrices.
- `.boneMatrices : Float32Array` — An array buffer holding the bone data.
Input data for Skeleton#boneTexture . Default is null .
- `.boneTexture :DataTexture` — A texture holding the bone data for use
in the vertex shader. Default is null .
- `.bones : Array.<Bone>` — An array of bones defining the skeleton.
- `.previousBoneMatrices : Float32Array` — An array buffer holding the bone data of the previous frame.
Required for computing velocity. Maintained in SkinningNode . Default is null .

## Methods
- `.calculateInverses()` — Computes the bone inverse matrices. This method resets Skeleton#boneInverses and fills it with new matrices.
- `.clone() :Skeleton` — Returns a new skeleton with copied values from this instance.
- `.computeBoneTexture() :Skeleton` — Computes a data texture for passing bone data to the vertex shader.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.fromJSON( json :Object, bones :Object.<string,Bone>) :Skeleton` — Setups the skeleton by the given JSON and bones.
- `.getBoneByName( name :string) :Bone| undefined` — Searches through the skeleton's bone array and returns the first with a
matching name.
- `.init()` — Initializes the skeleton. This method gets automatically called by the constructor
but depending on how the skeleton is created it might be necessary to call this method
manually.
- `.pose()` — Resets the skeleton to the base pose.
- `.toJSON() : Object` — Serializes the skeleton into JSON.
- `.update()` — Resets the skeleton to the base pose.

## Source