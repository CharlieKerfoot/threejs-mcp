# BufferGeometryUtils

## Import

## Methods
- `.computeMikkTSpaceTangents( geometry :BufferGeometry, MikkTSpace :Object, negateSign :boolean) :BufferGeometry` — Computes vertex tangents using the MikkTSpace algorithm. MikkTSpace generates the same tangents consistently,
and is used in most modelling tools and normal map bakers. Use MikkTSpace for materials...
- `.computeMorphedAttributes( object :Mesh|Line|Points) : Object` — Calculates the morphed attributes of a morphed/skinned BufferGeometry. Helpful for Raytracing or Decals (i.e. a DecalGeometry applied to a morphed Object with a BufferGeometry will use the original...
- `.deepCloneAttribute( attribute :BufferAttribute) :BufferAttribute` — Performs a deep clone of the given buffer attribute.
- `.deinterleaveAttribute( attribute :InterleavedBufferAttribute) :BufferAttribute` — Returns a new, non-interleaved version of the given attribute.
- `.deinterleaveGeometry( geometry :BufferGeometry) (inner)` — Deinterleaves all attributes on the given geometry.
- `.estimateBytesUsed( geometry :BufferGeometry) : number` — Returns the amount of bytes used by all attributes to represent the geometry.
- `.interleaveAttributes( attributes :Array.<BufferAttribute>) : Array.<InterleavedBufferAttribute>` — Interleaves a set of attributes and returns a new array of corresponding attributes that share a
single InterleavedBuffer instance. All attributes must have compatible types.
- `.mergeAttributes( attributes :Array.<BufferAttribute>) :BufferAttribute` — Merges a set of attributes into a single instance. All attributes must have compatible properties and types.
Instances of InterleavedBufferAttribute are not supported.
- `.mergeGeometries( geometries :Array.<BufferGeometry>, useGroups :boolean) :BufferGeometry` — Merges a set of geometries into a single instance. All geometries must have compatible attributes.
- `.mergeGroups( geometry :BufferGeometry) :BufferGeometry` — Merges the BufferGeometry#groups for the given geometry.
- `.mergeVertices( geometry :BufferGeometry, tolerance :number) :BufferGeometry` — Returns a new geometry with vertices for which all similar vertex attributes (within tolerance) are merged.
- `.toCreasedNormals( geometry :BufferGeometry, creaseAngle :number) :BufferGeometry` — Modifies the supplied geometry if it is non-indexed, otherwise creates a new,
non-indexed geometry. Returns the geometry with smooth normals everywhere except
faces that meet at an angle greater th...
- `.toTrianglesDrawMode( geometry :BufferGeometry, drawMode :number) :BufferGeometry` — Returns a new indexed geometry based on TrianglesDrawMode draw mode.
This mode corresponds to the gl.TRIANGLES primitive in WebGL.

## Source