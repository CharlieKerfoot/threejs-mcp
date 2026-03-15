# MDDLoader
Extends: Loader→

A loader for the MDD format. MDD stores a position for every vertex in a model for every frame in an animation.
Similar to BVH, it can be used to transfer animation data between different 3D applications or engines. MDD stores its data in binary format (big endian) in the following way: number of frames (a single uint32) number of vertices (a single uint32) time values for each frame (sequence of float32) vertex data for each frame (sequence of float32)

## Constructor
`newMDDLoader( manager :LoadingManager)`
Constructs a new MDD loader.

## Import

## Methods
- `.load( url :string, onLoad :function, onProgress :onProgressCallback, onError :onErrorCallback)` — Starts loading from the given URL and passes the loaded MDD asset
to the onLoad() callback.
- `.parse( data :ArrayBuffer) : Object` — Parses the given MDD data and returns an object holding the animation clip and the respective
morph targets.

## Source