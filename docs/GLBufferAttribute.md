# GLBufferAttribute

An alternative version of a buffer attribute with more control over the VBO. The renderer does not construct a VBO for this kind of attribute. Instead, it uses
whatever VBO is passed in constructor and can later be altered via the buffer property. The most common use case for this class is when some kind of GPGPU calculation interferes
or even produces the VBOs in question. Notice that this class can only be used with WebGLRenderer .

## Constructor
`newGLBufferAttribute( buffer :WebGLBuffer, type :number, itemSize :number, elementSize :number, count :number, normalized :boolean)`
Constructs a new GL buffer attribute.

## Properties
- `.buffer : WebGLBuffer` — The native WebGL buffer.
- `.count : number` — The expected number of vertices in VBO.
- `.elementSize : number` — The corresponding size (in bytes) for the given type parameter.
- `.isGLBufferAttribute : boolean` — This flag can be used for type testing. Default is true .
- `.itemSize : number` — The item size, see BufferAttribute#itemSize .
- `.name : string` — The name of the buffer attribute.
- `.needsUpdate : number` — Flag to indicate that this attribute has changed and should be re-sent to
the GPU. Set this to true when you modify the value of the array. Default is false .
- `.normalized : boolean` — Applies to integer data only. Indicates how the underlying data in the buffer maps to
the values in the GLSL code. For instance, if buffer contains data of gl.UNSIGNED_SHORT ,
and normalized is tru...
- `.type : number` — The native data type.
- `.version : number` — A version number, incremented every time the needsUpdate is set to true .

## Methods
- `.setBuffer( buffer :WebGLBuffer) :BufferAttribute` — Sets the given native WebGL buffer.
- `.setCount( count :number) :BufferAttribute` — Sets the count (the expected number of vertices in VBO).
- `.setItemSize( itemSize :number) :BufferAttribute` — Sets the item size.
- `.setType( type :number, elementSize :number) :BufferAttribute` — Sets the given native data type and element size.

## Source