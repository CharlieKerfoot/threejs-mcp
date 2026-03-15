# InterleavedBuffer

"Interleaved" means that multiple attributes, possibly of different types,
(e.g., position, normal, uv, color) are packed into a single array buffer. An introduction into interleaved arrays can be found here: Interleaved array basics

## Constructor
`newInterleavedBuffer( array :TypedArray, stride :number)`
Constructs a new interleaved buffer.

## Properties
- `.array : TypedArray` — A typed array with a shared buffer storing attribute data.
- `.count : number` — The total number of elements in the array
- `.isInterleavedBuffer : boolean` — This flag can be used for type testing. Default is true .
- `.needsUpdate : number` — Flag to indicate that this attribute has changed and should be re-sent to
the GPU. Set this to true when you modify the value of the array. Default is false .
- `.stride : number` — The number of typed-array elements per vertex.
- `.updateRanges : Array.<Object>` — This can be used to only update some components of stored vectors (for example, just the
component related to color). Use the addUpdateRange() function to add ranges to this array.
- `.usage :StaticDrawUsage|DynamicDrawUsage|StreamDrawUsage|StaticReadUsage|DynamicReadUsage|StreamReadUsage|StaticCopyUsage|DynamicCopyUsage|StreamCopyUsage` — Defines the intended usage pattern of the data store for optimization purposes. Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desi...
- `.uuid : string` — The UUID of the interleaved buffer.
- `.version : number` — A version number, incremented every time the needsUpdate is set to true .

## Methods
- `.addUpdateRange( start :number, count :number)` — Adds a range of data in the data array to be updated on the GPU.
- `.clearUpdateRanges()` — Clears the update ranges.
- `.clone( data :Object) :InterleavedBuffer` — Returns a new interleaved buffer with copied values from this instance.
- `.copy( source :InterleavedBuffer) :InterleavedBuffer` — Copies the values of the given interleaved buffer to this instance.
- `.copyAt( index1 :number, interleavedBuffer :InterleavedBuffer, index2 :number) :InterleavedBuffer` — Copies a vector from the given interleaved buffer to this one. The start
and destination position in the attribute buffers are represented by the
given indices.
- `.onUpload( callback :function) :InterleavedBuffer` — Sets the given callback function that is executed after the Renderer has transferred
the array data to the GPU. Can be used to perform clean-up operations after
the upload when data are not needed ...
- `.onUploadCallback()` — A callback function that is executed after the renderer has transferred the attribute array
data to the GPU.
- `.set( value :TypedArray | Array, offset :number) :InterleavedBuffer` — Sets the given array data in the interleaved buffer.
- `.setUsage( value :StaticDrawUsage|DynamicDrawUsage|StreamDrawUsage|StaticReadUsage|DynamicReadUsage|StreamReadUsage|StaticCopyUsage|DynamicCopyUsage|StreamCopyUsage) :InterleavedBuffer` — Sets the usage of this interleaved buffer.
- `.toJSON( data :Object) : Object` — Serializes the interleaved buffer into JSON.

## Source