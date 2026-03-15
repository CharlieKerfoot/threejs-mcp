# CSMFrustum

Represents the frustum of a CSM instance.

## Constructor
`newCSMFrustum( data :CSMFrustum~Data)`
Constructs a new CSM frustum.

## Import

## Properties
- `.vertices : Object` — An object representing the vertices of the near and
far plane in view space.
- `.zNear : number` — The zNear value. This value depends on whether the CSM
is used with WebGL or WebGPU. Both API use different
conventions for their projection matrices.

## Methods
- `.setFromProjectionMatrix( projectionMatrix :Matrix4, maxFar :number) : Object` — Setups this CSM frustum from the given projection matrix and max far value.
- `.split( breaks :Array.<number>, target :Array.<CSMFrustum>)` — Splits the CSM frustum by the given array. The new CSM frustum are pushed into the given
target array.
- `.toSpace( cameraMatrix :Matrix4, target :CSMFrustum)` — Transforms the given target CSM frustum into the different coordinate system defined by the
given camera matrix.

## Type Definitions
- `.Data` — Constructor data of CSMFrustum .

## Source