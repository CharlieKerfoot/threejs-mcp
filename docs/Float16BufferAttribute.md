# Float16BufferAttribute
Extends: BufferAttribute→

Convenient class that can be used when creating a Float16 buffer attribute with
a plain Array instance. This class automatically converts to and from FP16 via Uint16Array since Float16Array browser support is still problematic.

## Constructor
`newFloat16BufferAttribute( array :Array.<number> | Uint16Array, itemSize :number, normalized :boolean)`
Constructs a new buffer attribute.

## Source