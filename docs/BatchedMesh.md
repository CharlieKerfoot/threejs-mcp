# BatchedMesh
Extends: EventDispatcher→Object3D→Mesh→

A special version of a mesh with multi draw batch rendering support. Use
this class if you have to render a large number of objects with the same
material but with different geometries or world transformations. The usage of BatchedMesh will help you to reduce the number of draw calls and thus improve the overall
rendering performance in your application.

## Constructor
`newBatchedMesh( maxInstanceCount :number, maxVertexCount :number, maxIndexCount :number, material :Material| Array.<Material>)`
Constructs a new batched mesh.

## Properties
- `.boundingBox :Box3` — The bounding box of the batched mesh. Can be computed via BatchedMesh#computeBoundingBox . Default is null .
- `.boundingSphere :Sphere` — The bounding sphere of the batched mesh. Can be computed via BatchedMesh#computeBoundingSphere . Default is null .
- `.customSort : function` — Takes a sort a function that is run before render. The function takes a list of instances to
sort and a camera. The objects in the list include a "z" field to perform a depth-ordered
sort with. Def...
- `.instanceCount : number` — The instance count.
- `.isBatchedMesh : boolean` — This flag can be used for type testing. Default is true .
- `.maxInstanceCount : number` — The maximum number of individual instances that can be stored in the batch.
- `.perObjectFrustumCulled : boolean` — When set ot true , the individual objects of a batch are frustum culled. Default is true .
- `.sortObjects : boolean` — When set to true , the individual objects of a batch are sorted to improve overdraw-related artifacts.
If the material is marked as "transparent" objects are rendered back to front and if not then ...
- `.unusedIndexCount : number` — The number of unused indices.
- `.unusedVertexCount : number` — The number of unused vertices.

## Methods
- `.addGeometry( geometry :BufferGeometry, reservedVertexCount :number, reservedIndexCount :number) : number` — Adds the given geometry to the batch and returns the associated
geometry id referring to it to be used in other functions.
- `.addInstance( geometryId :number) : number` — Adds a new instance to the batch using the geometry of the given ID and returns
a new id referring to the new instance to be used by other functions.
- `.computeBoundingBox()` — Computes the bounding box, updating BatchedMesh#boundingBox .
Bounding boxes aren't computed by default. They need to be explicitly computed,
otherwise they are null .
- `.computeBoundingSphere()` — Computes the bounding sphere, updating BatchedMesh#boundingSphere .
Bounding spheres aren't computed by default. They need to be explicitly computed,
otherwise they are null .
- `.deleteGeometry( geometryId :number) :BatchedMesh` — Deletes the geometry defined by the given ID from this batch. Any instances referencing
this geometry will also be removed as a side effect.
- `.deleteInstance( instanceId :number) :BatchedMesh` — Deletes an existing instance from the batch using the given ID.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getBoundingBoxAt( geometryId :number, target :Box3) :Box3` — Returns the bounding box for the given geometry.
- `.getBoundingSphereAt( geometryId :number, target :Sphere) :Sphere` — Returns the bounding sphere for the given geometry.
- `.getColorAt( instanceId :number, color :Color|Vector4) :Color|Vector4` — Returns the color of the defined instance.
- `.getGeometryIdAt( instanceId :number) : number` — Returns the geometry ID of the defined instance.
- `.getGeometryRangeAt( geometryId :number, target :Object) : Object` — Get the range representing the subset of triangles related to the attached geometry,
indicating the starting offset and count, or null if invalid.
- `.getMatrixAt( instanceId :number, matrix :Matrix4) :Matrix4` — Returns the local transformation matrix of the defined instance.
- `.getVisibleAt( instanceId :number) : boolean` — Returns the visibility state of the defined instance.
- `.optimize() :BatchedMesh` — Repacks the sub geometries in BatchedMesh to remove any unused space remaining from
previously deleted geometry, freeing up space to add new geometry.
- `.setColorAt( instanceId :number, color :Color|Vector4) :BatchedMesh` — Sets the given color to the defined instance.
- `.setCustomSort( func :function) :BatchedMesh` — Takes a sort a function that is run before render. The function takes a list of instances to
sort and a camera. The objects in the list include a "z" field to perform a depth-ordered sort with.
- `.setGeometryAt( geometryId :number, geometry :BufferGeometry) : number` — Replaces the geometry at the given ID with the provided geometry. Throws an error if there
is not enough space reserved for geometry. Calling this will change all instances that are
rendering that ...
- `.setGeometryIdAt( instanceId :number, geometryId :number) :BatchedMesh` — Sets the geometry ID of the instance at the given index.
- `.setGeometrySize( maxVertexCount :number, maxIndexCount :number)` — Resizes the available space in the batch's vertex and index buffer attributes to the provided sizes.
If the provided arguments shrink the geometry buffers but there is not enough unused space at th...
- `.setInstanceCount( maxInstanceCount :number)` — Resizes the necessary buffers to support the provided number of instances.
If the provided arguments shrink the number of instances but there are not enough
unused Ids at the end of the list then a...
- `.setMatrixAt( instanceId :number, matrix :Matrix4) :BatchedMesh` — Sets the given local transformation matrix to the defined instance.
Negatively scaled matrices are not supported.
- `.setVisibleAt( instanceId :number, visible :boolean) :BatchedMesh` — Sets the visibility of the instance.
- `.validateGeometryId( geometryId :number)` — Validates the geometry defined by the given ID.
- `.validateInstanceId( instanceId :number)` — Validates the instance defined by the given ID.

## Source