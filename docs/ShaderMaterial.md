# ShaderMaterial
Extends: EventDispatcher→Material→

A material rendered with custom shaders. A shader is a small program written in GLSL.
that runs on the GPU. You may want to use a custom shader if you need to implement an
effect not included with any of the built-in materials. There are the following notes to bear in mind when using a ShaderMaterial : ShaderMaterial can only be used with WebGLRenderer . Built in attributes and uniforms are passed to the shaders along with your code. If
you don't want that, use RawShaderMaterial instead. You can use the directive #pragma unroll_loop_start and #pragma unroll_loop_end in order to unroll a for loop in GLSL by the shader preprocessor. The directive has
to be placed right above the loop. The loop formatting has to correspond to a defined standard. The loop has to be normalized . The loop variable has to be i . The value UNROLLED_LOOP_INDEX will be replaced with the explicitly
value of i for the given iteration and can be used in preprocessor
statements.

## Constructor
`newShaderMaterial( parameters :Object)`
Constructs a new shader material.

## Properties
- `.clipping : boolean` — Defines whether this material supports clipping; true to let the renderer
pass the clippingPlanes uniform. Default is false .
- `.defaultAttributeValues : Object` — When the rendered geometry doesn't include these attributes but the
material does, these default values will be passed to the shaders. This
avoids errors when buffer data is missing. color: [ 1, 1,...
- `.defines : Object` — Defines custom constants using #define directives within the GLSL code
for both the vertex shader and the fragment shader; each key/value pair
yields another directive. defines: {
	FOO: 15,
	BAR: t...
- `.extensions : Object` — This object allows to enable certain WebGL 2 extensions. clipCullDistance: set to true to use vertex shader clipping multiDraw: set to true to use vertex shader multi_draw / enable gl_DrawID
- `.fog : boolean` — Defines whether the material color is affected by global fog settings; true to pass fog uniforms to the shader. Setting this property to true requires the definition of fog uniforms. It is
recommen...
- `.forceSinglePass : boolean` — Overwritten and set to true by default. Default is true .
- `.fragmentShader : string` — Fragment shader GLSL code. This is the actual code for the shader.
- `.glslVersion :GLSL1|GLSL3` — Defines the GLSL version of custom shader code. Default is null .
- `.index0AttributeName : string | undefined` — If set, this calls gl.bindAttribLocation to bind a generic vertex index to an attribute variable. Default is undefined .
- `.isShaderMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.lights : boolean` — Defines whether this material uses lighting; true to pass uniform data
related to lighting to this shader. Default is false .
- `.linewidth : number` — Controls line thickness or lines. WebGL and WebGPU ignore this setting and always render line primitives with a
width of one pixel. Default is 1 .
- `.uniforms : Object` — An object of the form: {
	"uniform1": { value: 1.0 },
	"uniform2": { value: 2 }
} specifying the uniforms to be passed to the shader code; keys are uniform
names, values are definitions of the form...
- `.uniformsGroups : Array.<UniformsGroup>` — An array holding uniforms groups for configuring UBOs.
- `.uniformsNeedUpdate : boolean` — Can be used to force a uniform update while changing uniforms in Object3D#onBeforeRender . Default is false .
- `.vertexShader : string` — Vertex shader GLSL code. This is the actual code for the shader.
- `.wireframe : boolean` — Renders the geometry as a wireframe. Default is false .
- `.wireframeLinewidth : number` — Controls the thickness of the wireframe. WebGL and WebGPU ignore this property and always render
1 pixel wide lines. Default is 1 .

## Type Definitions
- `.Shader` — This type represents the fields required to store and run the shader code.

## Source