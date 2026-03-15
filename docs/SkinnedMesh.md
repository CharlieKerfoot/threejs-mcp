# SkinnedMesh
Extends: EventDispatcher→Object3D→Mesh→

A mesh that has a Skeleton that can then be used to animate the
vertices of the geometry with skinning/skeleton animation. Next to a valid skeleton, the skinned mesh requires skin indices and weights
as buffer attributes in its geometry. These attribute define which bones affect a single
vertex to a certain extend. Typically skinned meshes are not created manually but loaders like GLTFLoader or FBXLoader import respective models.

## Constructor
`newSkinnedMesh( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new skinned mesh.

## Properties
- `.bindMatrix :Matrix4` — The base matrix that is used for the bound bone transforms.
- `.bindMatrixInverse :Matrix4` — The base matrix that is used for resetting the bound bone transforms.
- `.bindMode :AttachedBindMode|DetachedBindMode` — AttachedBindMode means the skinned mesh shares the same world space as the skeleton.
This is not true when using DetachedBindMode which is useful when sharing a skeleton
across multiple skinned mes...
- `.boundingBox :Box3` — The bounding box of the skinned mesh. Can be computed via SkinnedMesh#computeBoundingBox . Default is null .
- `.boundingSphere :Sphere` — The bounding sphere of the skinned mesh. Can be computed via SkinnedMesh#computeBoundingSphere . Default is null .
- `.isSkinnedMesh : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.applyBoneTransform( index :number, target :Vector3) :Vector3` — Applies the bone transform associated with the given index to the given
vertex position. Returns the updated vector.
- `.bind( skeleton :Skeleton, bindMatrix :Matrix4)` — Binds the given skeleton to the skinned mesh.
- `.computeBoundingBox()` — Computes the bounding box of the skinned mesh, and updates SkinnedMesh#boundingBox .
The bounding box is not automatically computed by the engine; this method must be called by your app.
If the ski...
- `.computeBoundingSphere()` — Computes the bounding sphere of the skinned mesh, and updates SkinnedMesh#boundingSphere .
The bounding sphere is automatically computed by the engine once when it is needed, e.g., for ray casting
...
- `.normalizeSkinWeights()` — Normalizes the skin weights which are defined as a buffer attribute
in the skinned mesh's geometry.
- `.pose()` — This method sets the skinned mesh in the rest pose).

## Source