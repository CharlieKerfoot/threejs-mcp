# Camera
Extends: EventDispatcher→Object3D→

Abstract base class for cameras. This class should always be inherited
when you build a new camera.

## Constructor
`newCamera()(abstract)`
Constructs a new camera.

## Properties
- `.coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem` — The coordinate system in which the camera is used.
- `.isCamera : boolean` — This flag can be used for type testing. Default is true .
- `.matrixWorldInverse :Matrix4` — The inverse of the camera's world matrix.
- `.projectionMatrix :Matrix4` — The camera's projection matrix.
- `.projectionMatrixInverse :Matrix4` — The inverse of the camera's projection matrix.
- `.reversedDepth : boolean` — The flag that indicates whether the camera uses a reversed depth buffer. Default is false .

## Methods
- `.getWorldDirection( target :Vector3) :Vector3` — Returns a vector representing the ("look") direction of the 3D object in world space. This method is overwritten since cameras have a different forward vector compared to other
3D objects. A camera...

## Source