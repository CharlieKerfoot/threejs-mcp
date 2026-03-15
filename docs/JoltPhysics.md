# JoltPhysics

Can be used to include Jolt as a Physics engine into three.js apps. The API can be initialized via: The component automatically imports Jolt from a CDN so make sure
to use the component with an active Internet connection.

## Import

## Methods
- `.addMesh( mesh :Mesh, mass :number, restitution :number)` — Adds the given mesh to this physics simulation.
- `.addScene( scene :Object3D)` — Adds the given scene to this physics simulation. Only meshes with a physics object in their Object3D#userData field will be honored.
The object can be used to store the mass and restitution of the ...
- `.setMeshPosition( mesh :Mesh, position :Vector3, index :number)` — Set the position of the given mesh which is part of the physics simulation. Calling this
method will reset the current simulated velocity of the mesh.

## Source