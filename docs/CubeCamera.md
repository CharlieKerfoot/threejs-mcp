# CubeCamera
Extends: EventDispatcher→Object3D→

A special type of camera that is positioned in 3D space to render its surroundings into a
cube render target. The render target can then be used as an environment map for rendering
realtime reflections in your scene.

## Constructor
`newCubeCamera( near :number, far :number, renderTarget :WebGLCubeRenderTarget)`
Constructs a new cube camera.

## Properties
- `.activeMipmapLevel : number` — The current active mipmap level Default is 0 .
- `.coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem` — The current active coordinate system. Default is null .
- `.renderTarget :WebGLCubeRenderTarget` — A reference to the cube render target.

## Methods
- `.update( renderer :Renderer|WebGLRenderer, scene :Scene)` — Calling this method will render the given scene with the given renderer
into the cube render target of the camera.
- `.updateCoordinateSystem()` — Must be called when the coordinate system of the cube camera is changed.

## Source