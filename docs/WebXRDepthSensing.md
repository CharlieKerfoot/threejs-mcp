# WebXRDepthSensing

A XR module that manages the access to the Depth Sensing API.

## Constructor
`newWebXRDepthSensing()`
Constructs a new depth sensing module.

## Properties
- `.depthFar : number` — The depth near far.
- `.depthNear : number` — The depth near value.
- `.mesh :Mesh` — A plane mesh for visualizing the depth texture.
- `.texture :ExternalTexture` — An opaque texture representing the depth of the user's environment.

## Methods
- `.getDepthTexture() :ExternalTexture` — Returns a texture representing the depth of the user's environment.
- `.getMesh( cameraXR :ArrayCamera) :Mesh` — Returns a plane mesh that visualizes the depth texture.
- `.init( depthData :XRWebGLDepthInformation, renderState :XRRenderState)` — Inits the depth sensing module
- `.reset()` — Resets the module

## Source