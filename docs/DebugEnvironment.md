# DebugEnvironment
Extends: EventDispatcher→Object3D→Scene→

This class represents a scene with a very basic room setup that can be used as
input for PMREMGenerator#fromScene . The resulting PMREM represents the room's
lighting and can be used for Image Based Lighting by assigning it to Scene#environment or directly as an environment map to PBR materials. This class uses a simple room setup and should only be used for development purposes.
A more appropriate setup for production is RoomEnvironment .

## Constructor
`newDebugEnvironment()`
Constructs a new debug environment.

## Import

## Methods
- `.dispose()` — Frees internal resources. This method should be called
when the environment is no longer required.

## Source