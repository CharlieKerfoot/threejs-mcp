# AnimationObjectGroup

A group of objects that receives a shared animation state. Usage: Add objects you would otherwise pass as 'root' to the
constructor or the .clipAction method of AnimationMixer. Instead pass this object as 'root'. You can also add and remove objects later when the mixer is running. Note: Objects of this class appear as one object to the mixer,
so cache control of the individual objects must be done on the group. Limitation: The animated properties must be compatible among the all objects in the group. A single property can either be controlled through a target group or directly, but not both.

## Constructor
`newAnimationObjectGroup( …arguments :Object3D)`
Constructs a new animation group.

## Properties
- `.isAnimationObjectGroup : boolean` — This flag can be used for type testing. Default is true .
- `.uuid : string` — The UUID of the 3D object.

## Methods
- `.add( …arguments :Object3D)` — Adds an arbitrary number of objects to this animation group.
- `.remove( …arguments :Object3D)` — Removes an arbitrary number of objects to this animation group
- `.uncache( …arguments :Object3D)` — Deallocates all memory resources for the passed 3D objects of this animation group.

## Source