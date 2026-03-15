# VelocityNode
Extends: EventDispatcher→Node→TempNode→

A node for representing motion or velocity vectors. Foundation
for advanced post processing effects like motion blur or TRAA. The node keeps track of the model, view and projection matrices
of the previous frame and uses them to compute offsets in NDC space.
These offsets represent the final velocity.

## Constructor
`newVelocityNode()`
Constructs a new vertex color node.

## Properties
- `.previousCameraViewMatrix :UniformNode.<mat4>` — Uniform node representing the previous view matrix. Default is null .
- `.previousModelWorldMatrix :UniformNode.<mat4>` — Uniform node representing the previous model matrix in world space. Default is null .
- `.previousProjectionMatrix :UniformNode.<mat4>` — Uniform node representing the previous projection matrix. Default is null .
- `.projectionMatrix :Matrix4` — The current projection matrix. Default is null .
- `.updateAfterType : string` — Overwritten since velocity nodes save data after the update. Default is 'object' .
- `.updateType : string` — Overwritten since velocity nodes are updated per object. Default is 'object' .

## Methods
- `.setProjectionMatrix( projectionMatrix :Matrix4)` — Sets the given projection matrix.
- `.setup( builder :NodeBuilder) :Node.<vec2>` — Implements the velocity computation based on the previous and current vertex data.
- `.update( frame :NodeFrame)` — Updates velocity specific uniforms.
- `.updateAfter( frame :NodeFrame)` — Overwritten to updated velocity specific uniforms.

## Source