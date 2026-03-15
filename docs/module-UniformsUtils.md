# UniformsUtils

## Static Methods
- `.cloneUniforms( src :Object) : Object` — Clones the given uniform definitions by performing a deep-copy. That means
if the value of a uniform refers to an object like a Vector3 or Texture,
the cloned uniform will refer to a new object ref...
- `.mergeUniforms( uniforms :Array) : Object` — Merges the given uniform definitions into a single object. Since the
method internally uses cloneUniforms(), it performs a deep-copy when
producing the merged uniform definitions.

## Source