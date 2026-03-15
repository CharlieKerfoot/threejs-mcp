# UniformsGroup
Extends: EventDispatcher→

A class for managing multiple uniforms in a single group. The renderer will process
such a definition as a single UBO. Since this class can only be used in context of ShaderMaterial , it is only supported
in WebGLRenderer .

## Constructor
`newUniformsGroup()`
Constructs a new uniforms group.

## Properties
- `.buffer : Float32Array` — A Float32 array buffer with the uniform values.
- `.byteLength : number` — The byte length of the buffer with correct buffer alignment.
- `.id : number` — The ID of the 3D object.
- `.isUniformsGroup : boolean` — This flag can be used for type testing. Default is true .
- `.isUniformsGroup : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the uniforms group.
- `.uniforms : Array.<Uniform>` — An array holding the uniforms.
- `.uniforms : Array.<Uniform>` — An array of uniform objects. The order of uniforms in this array must match the order of uniforms in the shader.
- `.usage :StaticDrawUsage|DynamicDrawUsage|StreamDrawUsage|StaticReadUsage|DynamicReadUsage|StreamReadUsage|StaticCopyUsage|DynamicCopyUsage|StreamCopyUsage` — The buffer usage. Default is StaticDrawUsage .
- `.values : Array.<number>` — An array with the raw uniform values.

## Methods
- `.add( uniform :Uniform) :UniformsGroup` — Adds the given uniform to this uniforms group.
- `.addUniform( uniform :Uniform) :UniformsGroup` — Adds a uniform to this group.
- `.addUniformUpdateRange( uniform :Uniform)` — Adds a uniform's update range to this buffer.
- `.clearUpdateRanges()` — Clears all update ranges of this buffer.
- `.clone() :UniformsGroup` — Returns a new uniforms group with copied values from this instance.
- `.copy( source :UniformsGroup) :UniformsGroup` — Copies the values of the given uniforms group to this instance.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.remove( uniform :Uniform) :UniformsGroup` — Removes the given uniform from this uniforms group.
- `.removeUniform( uniform :Uniform) :UniformsGroup` — Removes a uniform from this group.
- `.setName( name :string) :UniformsGroup` — Sets the name of this uniforms group.
- `.setUsage( value :StaticDrawUsage|DynamicDrawUsage|StreamDrawUsage|StaticReadUsage|DynamicReadUsage|StreamReadUsage|StaticCopyUsage|DynamicCopyUsage|StreamCopyUsage) :UniformsGroup` — Sets the usage of this uniforms group.
- `.update() : boolean` — Updates this group by updating each uniform object of
the internal uniform list. The uniform objects check if their
values has actually changed so this method only returns true if there is a real v...
- `.updateByType( uniform :Uniform) : boolean` — Updates a given uniform by calling an update method matching
the uniforms type.
- `.updateColor( uniform :ColorUniform) : boolean` — Updates a given Color uniform.
- `.updateMatrix3( uniform :Matrix3Uniform) : boolean` — Updates a given Matrix3 uniform.
- `.updateMatrix4( uniform :Matrix4Uniform) : boolean` — Updates a given Matrix4 uniform.
- `.updateNumber( uniform :NumberUniform) : boolean` — Updates a given Number uniform.
- `.updateVector2( uniform :Vector2Uniform) : boolean` — Updates a given Vector2 uniform.
- `.updateVector3( uniform :Vector3Uniform) : boolean` — Updates a given Vector3 uniform.
- `.updateVector4( uniform :Vector4Uniform) : boolean` — Updates a given Vector4 uniform.

## Source