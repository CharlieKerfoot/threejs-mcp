# LightProbeGenerator

Utility class for creating instances of LightProbe .

## Import

## Static Methods
- `.fromCubeRenderTarget( renderer :WebGPURenderer|WebGLRenderer, cubeRenderTarget :CubeRenderTarget|WebGLCubeRenderTarget) : Promise.<LightProbe>` — Creates a light probe from the given (radiance) environment map.
The method expects that the environment map is represented as a cube render target. The cube render target must be in RGBA so cubeRe...
- `.fromCubeTexture( cubeTexture :CubeTexture) :LightProbe` — Creates a light probe from the given (radiance) environment map.
The method expects that the environment map is represented as a cube texture.

## Source