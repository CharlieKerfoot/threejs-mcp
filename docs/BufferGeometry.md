# BufferGeometry
Extends: EventDispatcher→

A representation of mesh, line, or point geometry. Includes vertex
positions, face indices, normals, colors, UVs, and custom attributes
within buffers, reducing the cost of passing all this data to the GPU.

## Constructor
`newBufferGeometry()`
Constructs a new geometry.

## Properties
- `.attributes : Object.<string, (BufferAttribute|InterleavedBufferAttribute)>` — This dictionary has as id the name of the attribute to be set and as value
the buffer attribute to set it to. Rather than accessing this property directly,
use setAttribute() and getAttribute() to ...
- `.boundingBox :Box3` — Bounding box for the geometry which can be calculated with computeBoundingBox() . Default is null .
- `.boundingSphere :Sphere` — Bounding sphere for the geometry which can be calculated with computeBoundingSphere() . Default is null .
- `.drawRange : Object` — Determines the part of the geometry to render. This should not be set directly,
instead use setDrawRange() .
- `.groups : Array.<Object>` — Split the geometry into groups, each of which will be rendered in a
separate draw call. This allows an array of materials to be used with the geometry. Use addGroup() and clearGroups() to edit grou...
- `.id : number` — The ID of the geometry.
- `.index :BufferAttribute` — Allows for vertices to be re-used across multiple triangles; this is
called using "indexed triangles". Each triangle is associated with the
indices of three vertices. This attribute therefore store...
- `.indirect :BufferAttribute` — A (storage) buffer attribute which was generated with a compute shader and
now defines indirect draw calls. Can only be used with WebGPURenderer and a WebGPU backend. Default is null .
- `.indirectOffset : number | Array.<number>` — The offset, in bytes, into the indirect drawing buffer where the value data begins. If an array is provided, multiple indirect draw calls will be made for each offset. Can only be used with WebGPUR...
- `.isBufferGeometry : boolean` — This flag can be used for type testing. Default is true .
- `.morphAttributes : Object` — This dictionary holds the morph targets of the geometry. Note: Once the geometry has been rendered, the morph attribute data cannot
be changed. You will have to call dispose() , and create a new ge...
- `.morphTargetsRelative : boolean` — Used to control the morph target behavior; when set to true , the morph
target data is treated as relative offsets, rather than as absolute
positions/normals. Default is false .
- `.name : string` — The name of the geometry.
- `.userData : Object` — An object that can be used to store custom data about the geometry.
It should not hold references to functions as these will not be cloned.
- `.uuid : string` — The UUID of the geometry.

## Methods
- `.addGroup( start :number, count :number, materialIndex :number)` — Adds a group to this geometry.
- `.applyMatrix4( matrix :Matrix4) :BufferGeometry` — Applies the given 4x4 transformation matrix to the geometry.
- `.applyQuaternion( q :Quaternion) :BufferGeometry` — Applies the rotation represented by the Quaternion to the geometry.
- `.center() :BufferGeometry` — Center the geometry based on its bounding box.
- `.clearGroups()` — Clears all groups.
- `.clone() :BufferGeometry` — Returns a new geometry with copied values from this instance.
- `.computeBoundingBox()` — Computes the bounding box of the geometry, and updates the boundingBox member.
The bounding box is not computed by the engine; it must be computed by your app.
You may need to recompute the boundin...
- `.computeBoundingSphere()` — Computes the bounding sphere of the geometry, and updates the boundingSphere member.
The engine automatically computes the bounding sphere when it is needed, e.g., for ray casting or view frustum c...
- `.computeTangents()` — Calculates and adds a tangent attribute to this geometry. The computation is only supported for indexed geometries and if position, normal, and uv attributes
are defined. When using a tangent space...
- `.computeVertexNormals()` — Computes vertex normals for the given vertex data. For indexed geometries, the method sets
each vertex normal to be the average of the face normals of the faces that share that vertex.
For non-inde...
- `.copy( source :BufferGeometry) :BufferGeometry` — Copies the values of the given geometry to this instance.
- `.deleteAttribute( name :string) :BufferGeometry` — Deletes the attribute for the given name.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.getAttribute( name :string) :BufferAttribute|InterleavedBufferAttribute| undefined` — Returns the buffer attribute for the given name.
- `.getIndex() :BufferAttribute` — Returns the index of this geometry.
- `.getIndirect() :BufferAttribute` — Returns the indirect attribute of this geometry.
- `.hasAttribute( name :string) : boolean` — Returns true if this geometry has an attribute for the given name.
- `.lookAt( vector :Vector3) :BufferGeometry` — Rotates the geometry to face a point in 3D space. This is typically done as a one time
operation, and not during a loop. Use Object3D#lookAt for typical
real-time mesh rotation.
- `.normalizeNormals()` — Ensures every normal vector in a geometry will have a magnitude of 1 . This will
correct lighting on the geometry surfaces.
- `.rotateX( angle :number) :BufferGeometry` — Rotates the geometry about the X axis. This is typically done as a one time
operation, and not during a loop. Use Object3D#rotation for typical
real-time mesh rotation.
- `.rotateY( angle :number) :BufferGeometry` — Rotates the geometry about the Y axis. This is typically done as a one time
operation, and not during a loop. Use Object3D#rotation for typical
real-time mesh rotation.
- `.rotateZ( angle :number) :BufferGeometry` — Rotates the geometry about the Z axis. This is typically done as a one time
operation, and not during a loop. Use Object3D#rotation for typical
real-time mesh rotation.
- `.scale( x :number, y :number, z :number) :BufferGeometry` — Scales the geometry. This is typically done as a one time
operation, and not during a loop. Use Object3D#scale for typical
real-time mesh rotation.
- `.setAttribute( name :string, attribute :BufferAttribute|InterleavedBufferAttribute) :BufferGeometry` — Sets the given attribute for the given name.
- `.setDrawRange( start :number, count :number)` — Sets the draw range for this geometry.
- `.setFromPoints( points :Array.<Vector2> | Array.<Vector3>) :BufferGeometry` — Defines a geometry by creating a position attribute based on the given array of points. The array
can hold 2D or 3D vectors. When using two-dimensional data, the z coordinate for all vertices is
se...
- `.setIndex( index :Array.<number> |BufferAttribute) :BufferGeometry` — Sets the given index to this geometry.
- `.setIndirect( indirect :BufferAttribute, indirectOffset :number | Array.<number>) :BufferGeometry` — Sets the given indirect attribute to this geometry.
- `.toJSON() : Object` — Serializes the geometry into JSON.
- `.toNonIndexed() :BufferGeometry` — Return a new non-index version of this indexed geometry. If the geometry
is already non-indexed, the method is a NOOP.
- `.translate( x :number, y :number, z :number) :BufferGeometry` — Translates the geometry. This is typically done as a one time
operation, and not during a loop. Use Object3D#position for typical
real-time mesh rotation.

## Source