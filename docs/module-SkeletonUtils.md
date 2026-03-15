# SkeletonUtils

## Import

## Methods
- `.clone( source :Object3D) :Object3D` — Clones the given 3D object and its descendants, ensuring that any SkinnedMesh instances are
correctly associated with their bones. Bones are also cloned, and must be descendants of the
object passe...
- `.retarget( target :Object3D, source :Object3D, options :module:SkeletonUtils~RetargetOptions) (inner)` — Retargets the skeleton from the given source 3D object to the
target 3D object.
- `.retargetClip( target :Object3D, source :Object3D, clip :AnimationClip, options :module:SkeletonUtils~RetargetOptions) :AnimationClip` — Retargets the animation clip of the source object to the
target 3D object.

## Type Definitions
- `.RetargetOptions` — Retarget options of SkeletonUtils .

## Source