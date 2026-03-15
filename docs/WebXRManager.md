# WebXRManager
Extends: EventDispatcher→

This class represents an abstraction of the WebXR Device API and is
internally used by WebGLRenderer . WebXRManager also provides a public
interface that allows users to enable/disable XR and perform XR related
tasks like for instance retrieving controllers.

## Properties
- `.cameraAutoUpdate : boolean` — Whether the manager's XR camera should be automatically updated or not. Default is true .
- `.enabled : boolean` — This flag notifies the renderer to be ready for XR rendering. Set it to true if you are going to use XR in your app. Default is false .
- `.isPresenting : boolean` — Whether XR presentation is active or not. Default is false .

## Methods
- `.getBaseLayer() : XRWebGLLayer | XRProjectionLayer` — Returns the current base layer. This is an XRProjectionLayer when the targeted XR device supports the
WebXR Layers API, or an XRWebGLLayer otherwise.
- `.getBinding() : XRWebGLBinding` — Returns the current XR binding. Creates a new binding if needed and the browser is
capable of doing so.
- `.getCamera() :ArrayCamera` — Returns an instance of ArrayCamera which represents the XR camera
of the active XR session. For each view it holds a separate camera object. The camera's fov is currently not used and does not refl...
- `.getCameraTexture( xrCamera :XRCamera) :Texture` — Retrieves an opaque texture from the view-aligned XRCamera.
Only available during the current animation loop.
- `.getController( index :number) :Group` — Returns a group representing the target ray space of the XR controller.
Use this space for visualizing 3D objects that support the user in pointing
tasks like UI interaction.
- `.getControllerGrip( index :number) :Group` — Returns a group representing the grip space of the XR controller.
Use this space for visualizing 3D objects that support the user in pointing
tasks like UI interaction. Note: If you want to show so...
- `.getDepthSensingMesh() :Mesh` — Returns the depth sensing mesh. See WebXRDepthSensing#getMesh .
- `.getDepthTexture() :Texture` — Returns the current depth texture computed via depth sensing. See WebXRDepthSensing#getDepthTexture .
- `.getEnvironmentBlendMode() : 'opaque' | 'additive' | 'alpha-blend' | undefined` — Returns the environment blend mode from the current XR session.
- `.getFoveation() : number | undefined` — Returns the amount of foveation used by the XR compositor for the projection layer.
- `.getFrame() : XRFrame` — Returns the current XR frame.
- `.getHand( index :number) :Group` — Returns a group representing the hand space of the XR controller.
Use this space for visualizing 3D objects that support the user in pointing
tasks like UI interaction.
- `.getReferenceSpace() : XRReferenceSpace` — Returns the XR reference space.
- `.getSession() : XRSession` — Returns the current XR session.
- `.hasDepthSensing() : boolean` — Returns true if depth sensing is supported.
- `.setFoveation( value :number)` — Sets the foveation value.
- `.setFramebufferScaleFactor( value :number)` — Sets the framebuffer scale factor. This method can not be used during a XR session.
- `.setReferenceSpace( space :XRReferenceSpace)` — Sets a custom XR reference space.
- `.setReferenceSpaceType( value :string)` — Sets the reference space type. Can be used to configure a spatial relationship with the user's physical
environment. Depending on how the user moves in 3D space, setting an appropriate reference sp...
- `.setSession( value :XRSession) : Promise` — After a XR session has been requested usually with one of the *Button modules, it
is injected into the renderer with this method. This method triggers the start of
the actual XR rendering.
- `.updateCamera( camera :Camera)` — Updates the state of the XR camera. Use this method on app level if you
set cameraAutoUpdate to false . The method requires the non-XR
camera of the scene as a parameter. The passed in camera's tra...

## Source