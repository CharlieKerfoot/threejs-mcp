# Uniform

Represents a uniform which is a global shader variable. They are passed to shader programs. When declaring a uniform of a ShaderMaterial , it is declared by value or by object. Since this class can only be used in context of ShaderMaterial , it is only supported
in WebGLRenderer .

## Constructor
`newUniform( value :any)`
Constructs a new uniform.

## Properties
- `.boundary : number` — Used to build the uniform buffer according to the STD140 layout.
Derived uniforms will set this property to a data type specific
value.
- `.index : number` — This property is set by UniformsGroup and marks
the index position in the uniform array.
- `.itemSize : number` — The item size. Derived uniforms will set this property to a data
type specific value.
- `.name : string` — The uniform's name.
- `.offset : number` — This property is set by UniformsGroup and marks
the start position in the uniform buffer.
- `.value :any` — The uniform value.
- `.value :any` — The uniform's value.

## Methods
- `.clone() :Uniform` — Returns a new uniform with copied values from this instance.
If the value has a clone() method, the value is cloned as well.
- `.getValue() :any` — Returns the uniform's value.
- `.setValue( value :any)` — Sets the uniform's value.

## Source