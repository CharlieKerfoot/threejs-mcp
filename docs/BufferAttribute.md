# BufferAttribute

This class stores data for an attribute (such as vertex positions, face
indices, normals, colors, UVs, and any custom attributes ) associated with
a geometry, which allows for more efficient passing of data to the GPU. When working with vector-like data, the fromBufferAttribute( attribute, index ) helper methods on vector and color class might be helpful. E.g. Vector3#fromBufferAttribute .

## Constructor
`newBufferAttribute( array :TypedArray, itemSize :number, normalized :boolean)`
Constructs a new buffer attribute.

## Properties
- `.array : TypedArray` — The array holding the attribute data. It should have itemSize * numVertices elements, where numVertices is the number of vertices in the associated geometry.
- `.count : number` — Represents the number of items this buffer attribute stores. It is internally computed
by dividing the array length by the itemSize .
- `.gpuType :FloatType|IntType` — Configures the bound GPU type for use in shaders. Note: this only has an effect for integer arrays and is not configurable for float arrays.
For lower precision float types, use Float16BufferAttrib...
- `.id : number` — The ID of the buffer attribute.
- `.isBufferAttribute : boolean` — This flag can be used for type testing. Default is true .
- `.itemSize : number` — The number of values of the array that should be associated with a particular vertex.
For instance, if this attribute is storing a 3-component vector (such as a position,
normal, or color), then th...
- `.name : string` — The name of the buffer attribute.
- `.needsUpdate : number` — Flag to indicate that this attribute has changed and should be re-sent to
the GPU. Set this to true when you modify the value of the array. Default is false .
- `.normalized : boolean` — Applies to integer data only. Indicates how the underlying data in the buffer maps to
the values in the GLSL code. For instance, if array is an instance of UInt16Array ,
and normalized is true , th...
- `.updateRanges : Array.<Object>` — This can be used to only update some components of stored vectors (for example, just the
component related to color). Use the addUpdateRange() function to add ranges to this array.
- `.usage :StaticDrawUsage|DynamicDrawUsage|StreamDrawUsage|StaticReadUsage|DynamicReadUsage|StreamReadUsage|StaticCopyUsage|DynamicCopyUsage|StreamCopyUsage` — Defines the intended usage pattern of the data store for optimization purposes. Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desi...
- `.version : number` — A version number, incremented every time the needsUpdate is set to true .

## Methods
- `.addUpdateRange( start :number, count :number)` — Adds a range of data in the data array to be updated on the GPU.
- `.applyMatrix3( m :Matrix3) :BufferAttribute` — Applies the given 3x3 matrix to the given attribute. Works with
item size 2 and 3 .
- `.applyMatrix4( m :Matrix4) :BufferAttribute` — Applies the given 4x4 matrix to the given attribute. Only works with
item size 3 .
- `.applyNormalMatrix( m :Matrix3) :BufferAttribute` — Applies the given 3x3 normal matrix to the given attribute. Only works with
item size 3 .
- `.clearUpdateRanges()` — Clears the update ranges.
- `.clone() :BufferAttribute` — Returns a new buffer attribute with copied values from this instance.
- `.copy( source :BufferAttribute) :BufferAttribute` — Copies the values of the given buffer attribute to this instance.
- `.copyArray( array :TypedArray | Array) :BufferAttribute` — Copies the given array data into this buffer attribute.
- `.copyAt( index1 :number, attribute :BufferAttribute, index2 :number) :BufferAttribute` — Copies a vector from the given buffer attribute to this one. The start
and destination position in the attribute buffers are represented by the
given indices.
- `.getComponent( index :number, component :number) : number` — Returns the given component of the vector at the given index.
- `.getW( index :number) : number` — Returns the w component of the vector at the given index.
- `.getX( index :number) : number` — Returns the x component of the vector at the given index.
- `.getY( index :number) : number` — Returns the y component of the vector at the given index.
- `.getZ( index :number) : number` — Returns the z component of the vector at the given index.
- `.onUpload( callback :function) :BufferAttribute` — Sets the given callback function that is executed after the Renderer has transferred
the attribute array data to the GPU. Can be used to perform clean-up operations after
the upload when attribute ...
- `.onUploadCallback()` — A callback function that is executed after the renderer has transferred the attribute
array data to the GPU.
- `.set( value :TypedArray | Array, offset :number) :BufferAttribute` — Sets the given array data in the buffer attribute.
- `.setComponent( index :number, component :number, value :number) :BufferAttribute` — Sets the given value to the given component of the vector at the given index.
- `.setUsage( value :StaticDrawUsage|DynamicDrawUsage|StreamDrawUsage|StaticReadUsage|DynamicReadUsage|StreamReadUsage|StaticCopyUsage|DynamicCopyUsage|StreamCopyUsage) :BufferAttribute` — Sets the usage of this buffer attribute.
- `.setW( index :number, w :number) :BufferAttribute` — Sets the w component of the vector at the given index.
- `.setX( index :number, x :number) :BufferAttribute` — Sets the x component of the vector at the given index.
- `.setXY( index :number, x :number, y :number) :BufferAttribute` — Sets the x and y component of the vector at the given index.
- `.setXYZ( index :number, x :number, y :number, z :number) :BufferAttribute` — Sets the x, y and z component of the vector at the given index.
- `.setXYZW( index :number, x :number, y :number, z :number, w :number) :BufferAttribute` — Sets the x, y, z and w component of the vector at the given index.
- `.setY( index :number, y :number) :BufferAttribute` — Sets the y component of the vector at the given index.
- `.setZ( index :number, z :number) :BufferAttribute` — Sets the z component of the vector at the given index.
- `.toJSON() : Object` — Serializes the buffer attribute into JSON.
- `.transformDirection( m :Matrix4) :BufferAttribute` — Applies the given 4x4 matrix to the given attribute. Only works with
item size 3 and with direction vectors.

## Source