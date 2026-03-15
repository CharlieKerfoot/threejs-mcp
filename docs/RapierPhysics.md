# RapierPhysics

Can be used to include Rapier as a Physics engine into three.js apps. The API can be initialized via: The component automatically imports Rapier from a CDN so make sure
to use the component with an active Internet connection.

## Import

## Methods
- `.addHeightfield( mesh :Mesh, width :number, depth :number, heights :Float32Array, scale :Object) : RigidBody` — Adds a heightfield terrain to the physics simulation.
- `.addMesh( mesh :Mesh, mass :number, restitution :number)` — Adds the given mesh to this physics simulation.
- `.addScene( scene :Object3D)` — Adds the given scene to this physics simulation. Only meshes with a physics object in their Object3D#userData field will be honored.
The object can be used to store the mass and restitution of the ...
- `.removeMesh( mesh :Mesh)` — Removes the given mesh from this physics simulation.
- `.setMeshPosition( mesh :Mesh, position :Vector3, index :number)` — Set the position of the given mesh which is part of the physics simulation. Calling this
method will reset the current simulated velocity of the mesh.
- `.setMeshVelocity( mesh :Mesh, velocity :Vector3, index :number)` — Set the velocity of the given mesh which is part of the physics simulation.

## Source