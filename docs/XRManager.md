# XRManager
Extends: EventDispatcher→

The XR manager is built on top of the WebXR Device API to
manage XR sessions with WebGPURenderer . XR is currently only supported with a WebGL 2 backend.

## Constructor
`newXRManager( renderer :Renderer, multiview :boolean)`
Constructs a new XR manager.

## Properties
- `.cameraAutoUpdate : boolean` — Whether the XR camera should automatically be updated or not. Default is true .
- `.enabled : boolean` — This flag globally enables XR rendering. Default is false .
- `.isPresenting : boolean` — Whether the XR device is currently presenting or not. Default is false .

## Methods
- `.createCylinderLayer( radius :number, centralAngle :number, aspectratio :number, translation :Vector3, quaternion :Quaternion, pixelwidth :number, pixelheight :number, rendercall :function, attributes :Object) :Mesh` — This method can be used in XR applications to create a cylindrical layer that presents a separate
rendered scene.
- `.createQuadLayer( width :number, height :number, translation :Vector3, quaternion :Quaternion, pixelwidth :number, pixelheight :number, rendercall :function, attributes :Object) :Mesh` — This method can be used in XR applications to create a quadratic layer that presents a separate
rendered scene.
- `.getBinding() : XRWebGLBinding` — Returns the current XR binding. Creates a new binding if needed and the browser is
capable of doing so.
- `.getCamera() :ArrayCamera` — Returns the XR camera.
- `.getController( index :number) :Group` — Returns an instance of THREE.Group that represents the transformation
of a XR controller in target ray space. The requested controller is defined
by the given index.
- `.getControllerGrip( index :number) :Group` — Returns an instance of THREE.Group that represents the transformation
of a XR controller in grip space. The requested controller is defined
by the given index.
- `.getEnvironmentBlendMode() : 'opaque' | 'additive' | 'alpha-blend' | undefined` — Returns the environment blend mode from the current XR session.
- `.getFoveation() : number | undefined` — Returns the foveation value.
- `.getFrame() : XRFrame` — Returns the current XR frame.
- `.getFramebufferScaleFactor() : number` — Returns the framebuffer scale factor.
- `.getHand( index :number) :Group` — Returns an instance of THREE.Group that represents the transformation
of a XR controller in hand space. The requested controller is defined
by the given index.
- `.getReferenceSpace() : XRReferenceSpace` — Returns the XR reference space.
- `.getReferenceSpaceType() : XRReferenceSpaceType` — Returns the reference space type.
- `.getSession() : XRSession` — Returns the current XR session.
- `.renderLayers()` — Renders the XR layers that have been previously added to the scene. This method is usually called in your animation loop before rendering
the actual scene via renderer.render( scene, camera ); .
- `.setFoveation( foveation :number)` — Sets the foveation value.
- `.setFramebufferScaleFactor( factor :number)` — Sets the framebuffer scale factor. This method can not be used during a XR session.
- `.setReferenceSpace( space :XRReferenceSpace)` — Sets a custom XR reference space.
- `.setReferenceSpaceType( type :XRReferenceSpaceType)` — Sets the reference space type. This method can not be used during a XR session.
- `.setSession( session :XRSession) : Promise` — After a XR session has been requested usually with one of the *Button modules, it
is injected into the renderer with this method. This method triggers the start of
the actual XR rendering.
- `.updateCamera( camera :PerspectiveCamera)` — This method is called by the renderer per frame and updates the XR camera
and it sub cameras based on the given camera. The given camera is the "user"
camera created on application level and used f...
- `.useMultiview() : boolean` — Returns true if the engine renders to a multiview target.

## Source