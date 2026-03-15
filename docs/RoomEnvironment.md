# RoomEnvironment
Extends: EventDispatcher→Object3D→Scene→

This class represents a scene with a basic room setup that can be used as
input for PMREMGenerator#fromScene . The resulting PMREM represents the room's
lighting and can be used for Image Based Lighting by assigning it to Scene#environment or directly as an environment map to PBR materials. The implementation is based on the EnvironmentScene component from the model-viewer project.

## Constructor
`newRoomEnvironment()`

## Import

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the environment is no longer required.

## Source