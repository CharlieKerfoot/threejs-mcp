# GPUComputationRenderer

GPUComputationRenderer, based on SimulationRenderer by @zz85. The GPUComputationRenderer uses the concept of variables. These variables are RGBA float textures that hold 4 floats
for each compute element (texel). Each variable has a fragment shader that defines the computation made to obtain the variable in question.
You can use as many variables you need, and make dependencies so you can use textures of other variables in the shader
(the sampler uniforms are added automatically) Most of the variables will need themselves as dependency. The renderer has actually two render targets per variable, to make ping-pong. Textures from the current frame are used
as inputs to render the textures of the next frame. The render targets of the variables can be used as input textures for your visualization shaders. Variable names should be valid identifiers and should not collide with THREE GLSL used identifiers.
a common approach could be to use 'texture' prefixing the variable name; i.e texturePosition, textureVelocity... The size of the computation (sizeX * sizeY) is defined as 'resolution' automatically in the shader. For example: Basic use: // Initialization...
// Create computation renderer
const gpuCompute = new GPUComputationRenderer( 1024, 1024, renderer );
// Create initial state float textures
const pos0 = gpuCompute.createTexture();
const vel0 = gpuCompute.createTexture();
// and fill in here the texture data...
// Add texture variables
const velVar = gpuCompute.addVariable( "textureVelocity", fragmentShaderVel, vel0 );
const posVar = gpuCompute.addVariable( "texturePosition", fragmentShaderPos, pos0 );
// Add variable dependencies
gpuCompute.setVariableDependencies( velVar, [ velVar, posVar ] );
gpuCompute.setVariableDependencies( posVar, [ velVar, posVar ] );
// Add custom uniforms
velVar.material.uniforms.time = { value: 0.0 };
// Check for completeness
const error = gpuCompute.init();
if ( error !== null ) {
		console.error( error );
}
// In each frame...
// Compute!
gpuCompute.compute();
// Update texture uniforms in your visualization materials with the gpu renderer output
myMaterial.uniforms.myTexture.value = gpuCompute.getCurrentRenderTarget( posVar ).texture;
// Do your rendering
renderer.render( myScene, myCamera ); Also, you can use utility functions to create ShaderMaterial and perform computations (rendering between textures)
Note that the shaders can have multiple input textures. const myFilter1 = gpuCompute.createShaderMaterial( myFilterFragmentShader1, { theTexture: { value: null } } );
const myFilter2 = gpuCompute.createShaderMaterial( myFilterFragmentShader2, { theTexture: { value: null } } );
const inputTexture = gpuCompute.createTexture();
// Fill in here inputTexture...
myFilter1.uniforms.theTexture.value = inputTexture;
const myRenderTarget = gpuCompute.createRenderTarget();
myFilter2.uniforms.theTexture.value = myRenderTarget.texture;
const outputRenderTarget = gpuCompute.createRenderTarget();
// Now use the output texture where you want:
myMaterial.uniforms.map.value = outputRenderTarget.texture;
// And compute each frame, before rendering to screen:
gpuCompute.doRenderTarget( myFilter1, myRenderTarget );
gpuCompute.doRenderTarget( myFilter2, outputRenderTarget );

## Constructor
`newGPUComputationRenderer( sizeX :number, sizeY :number, renderer :WebGLRenderer)`
Constructs a new GPU computation renderer.

## Import

## Properties
- `.addResolutionDefine` — Adds a resolution defined for the given material shader.

## Methods
- `.addVariable( variableName :string, computeFragmentShader :string, initialValueTexture :Texture) : Object` — Adds a compute variable to the renderer.
- `.compute()` — Executes the compute. This method is usually called in the animation loop.
- `.createRenderTarget( sizeXTexture :number, sizeYTexture :number, wrapS :number, wrapT :number, minFilter :number, magFilter :number) :WebGLRenderTarget` — Creates a new render target from the given parameters.
- `.createTexture() :DataTexture` — Creates a new data texture.
- `.dispose()` — Frees all internal resources. Call this method if you don't need the
renderer anymore.
- `.doRenderTarget( material :Material, output :WebGLRenderTarget)` — Renders the given material into the given render target
with a full-screen pass.
- `.getAlternateRenderTarget( variable :Object) :WebGLRenderTarget` — Returns the alternate render target for the given compute variable.
- `.getCurrentRenderTarget( variable :Object) :WebGLRenderTarget` — Returns the current render target for the given compute variable.
- `.init() : string` — Initializes the renderer.
- `.renderTexture( input :Texture, output :WebGLRenderTarget)` — Renders the given texture into the given render target.
- `.setDataType( type :FloatType|HalfFloatType) :GPUComputationRenderer` — Sets the data type of the internal textures.
- `.setVariableDependencies( variable :Object, dependencies :Array.<Object>)` — Sets variable dependencies.

## Source