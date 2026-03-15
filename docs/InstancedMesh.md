# InstancedMesh
Extends: EventDispatcher→Object3D→Mesh→

A special version of a mesh with instanced rendering support. Use
this class if you have to render a large number of objects with the same
geometry and material(s) but with different world transformations. The usage
of 'InstancedMesh' will help you to reduce the number of draw calls and thus
improve the overall rendering performance in your application.

## Constructor
`newInstancedMesh( geometry :BufferGeometry, material :Material| Array.<Material>, count :number)`
Constructs a new instanced mesh.

## Properties
- `.boundingBox :Box3` — The bounding box of the instanced mesh. Can be computed via InstancedMesh#computeBoundingBox . Default is null .
- `.boundingSphere :Sphere` — The bounding sphere of the instanced mesh. Can be computed via InstancedMesh#computeBoundingSphere . Default is null .
- `.count : number` — The number of instances.
- `.instanceColor :InstancedBufferAttribute` — Represents the color of all instances. You have to set its BufferAttribute#needsUpdate flag to true if you modify instanced data
via InstancedMesh#setColorAt . Default is null .
- `.instanceMatrix :InstancedBufferAttribute` — Represents the local transformation of all instances. You have to set its BufferAttribute#needsUpdate flag to true if you modify instanced data
via InstancedMesh#setMatrixAt .
- `.isInstancedMesh : boolean` — This flag can be used for type testing. Default is true .
- `.morphTexture :DataTexture` — Represents the morph target weights of all instances. You have to set its Texture#needsUpdate flag to true if you modify instanced data
via InstancedMesh#setMorphAt . Default is null .
- `.previousInstanceMatrix :InstancedBufferAttribute` — Represents the local transformation of all instances of the previous frame.
Required for computing velocity. Maintained in InstanceNode . Default is null .

## Methods
- `.computeBoundingBox()` — Computes the bounding box of the instanced mesh, and updates InstancedMesh#boundingBox .
The bounding box is not automatically computed by the engine; this method must be called by your app.
You ma...
- `.computeBoundingSphere()` — Computes the bounding sphere of the instanced mesh, and updates InstancedMesh#boundingSphere The engine automatically computes the bounding sphere when it is needed, e.g., for ray casting or view f...
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getColorAt( index :number, color :Color)` — Gets the color of the defined instance.
- `.getMatrixAt( index :number, matrix :Matrix4)` — Gets the local transformation matrix of the defined instance.
- `.getMorphAt( index :number, object :Mesh)` — Gets the morph target weights of the defined instance.
- `.setColorAt( index :number, color :Color)` — Sets the given color to the defined instance. Make sure you set the needsUpdate flag of InstancedMesh#instanceColor to true after updating all the colors.
- `.setMatrixAt( index :number, matrix :Matrix4)` — Sets the given local transformation matrix to the defined instance. Make sure you set the needsUpdate flag of InstancedMesh#instanceMatrix to true after updating all the colors.
- `.setMorphAt( index :number, object :Mesh)` — Sets the morph target weights to the defined instance. Make sure you set the needsUpdate flag of InstancedMesh#morphTexture to true after updating all the influences.

## Source