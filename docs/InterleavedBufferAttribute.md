# InterleavedBufferAttribute

An alternative version of a buffer attribute with interleaved data. Interleaved
attributes share a common interleaved data storage ( InterleavedBuffer ) and refer with
different offsets into the buffer.

## Constructor
`newInterleavedBufferAttribute( interleavedBuffer :InterleavedBuffer, itemSize :number, offset :number, normalized :boolean)`
Constructs a new interleaved buffer attribute.

## Properties
- `.array : TypedArray` — The array holding the interleaved buffer attribute data.
- `.count : number` — The item count of this buffer attribute.
- `.data :InterleavedBuffer` — The buffer holding the interleaved data.
- `.isInterleavedBufferAttribute : boolean` — This flag can be used for type testing. Default is true .
- `.itemSize : number` — The item size, see BufferAttribute#itemSize .
- `.name : string` — The name of the buffer attribute.
- `.needsUpdate : number` — Flag to indicate that this attribute has changed and should be re-sent to
the GPU. Set this to true when you modify the value of the array. Default is false .
- `.normalized :InterleavedBuffer` — Whether the data are normalized or not, see BufferAttribute#normalized
- `.offset : number` — The attribute offset into the buffer.

## Methods
- `.applyMatrix4( m :Matrix4) :InterleavedBufferAttribute` — Applies the given 4x4 matrix to the given attribute. Only works with
item size 3 .
- `.applyNormalMatrix( m :Matrix3) :InterleavedBufferAttribute` — Applies the given 3x3 normal matrix to the given attribute. Only works with
item size 3 .
- `.clone( data :Object) :BufferAttribute|InterleavedBufferAttribute` — Returns a new buffer attribute with copied values from this instance. If no parameter is provided, cloning an interleaved buffer attribute will de-interleave buffer data.
- `.getComponent( index :number, component :number) : number` — Returns the given component of the vector at the given index.
- `.getW( index :number) : number` — Returns the w component of the vector at the given index.
- `.getX( index :number) : number` — Returns the x component of the vector at the given index.
- `.getY( index :number) : number` — Returns the y component of the vector at the given index.
- `.getZ( index :number) : number` — Returns the z component of the vector at the given index.
- `.setComponent( index :number, component :number, value :number) :InterleavedBufferAttribute` — Sets the given value to the given component of the vector at the given index.
- `.setW( index :number, w :number) :InterleavedBufferAttribute` — Sets the w component of the vector at the given index.
- `.setX( index :number, x :number) :InterleavedBufferAttribute` — Sets the x component of the vector at the given index.
- `.setXY( index :number, x :number, y :number) :InterleavedBufferAttribute` — Sets the x and y component of the vector at the given index.
- `.setXYZ( index :number, x :number, y :number, z :number) :InterleavedBufferAttribute` — Sets the x, y and z component of the vector at the given index.
- `.setXYZW( index :number, x :number, y :number, z :number, w :number) :InterleavedBufferAttribute` — Sets the x, y, z and w component of the vector at the given index.
- `.setY( index :number, y :number) :InterleavedBufferAttribute` — Sets the y component of the vector at the given index.
- `.setZ( index :number, z :number) :InterleavedBufferAttribute` — Sets the z component of the vector at the given index.
- `.toJSON( data :Object) : Object` — Serializes the buffer attribute into JSON. If no parameter is provided, cloning an interleaved buffer attribute will de-interleave buffer data.
- `.transformDirection( m :Matrix4) :InterleavedBufferAttribute` — Applies the given 4x4 matrix to the given attribute. Only works with
item size 3 and with direction vectors.

## Source