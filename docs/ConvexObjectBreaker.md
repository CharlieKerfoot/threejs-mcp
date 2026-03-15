# ConvexObjectBreaker

This class can be used to subdivide a convex Geometry object into pieces. Use the function prepareBreakableObject to prepare a Mesh object to be broken.
Then, call the various functions to subdivide the object (subdivideByImpact, cutByPlane).
Sub-objects that are product of subdivision don't need prepareBreakableObject to be called on them. Requisites for the object: Mesh object must have a buffer geometry and a material. Vertex normals must be planar (not smoothed). The geometry must be convex (this is not checked in the library). You can create convex
geometries with ConvexGeometry . The BoxGeometry , SphereGeometry and other
convex primitives can also be used. Note: This lib adds member variables to object's userData member (see prepareBreakableObject function)
Use with caution and read the code when using with other libs.

## Constructor
`newConvexObjectBreaker( minSizeForBreak :number, smallDelta :number)`
Constructs a new convex object breaker.

## Import

## Methods
- `.cutByPlane( object :Object3D, plane :Plane, output :Object) : number` — Subdivides the given 3D object into pieces by a plane.
- `.prepareBreakableObject( object :Object3D, mass :number, velocity :Vector3, angularVelocity :Vector3, breakable :boolean)` — Must be called for all 3D objects that should be breakable.
- `.subdivideByImpact( object :Object3D, pointOfImpact :Vector3, normal :Vector3, maxRadialIterations :number, maxRandomIterations :number) : Array.<Object3D>` — Subdivides the given 3D object into pieces by an impact (meaning another object hits
the given 3D object at a certain surface point).

## Source