# Octree

An octree is a hierarchical tree data structure used to partition a three-dimensional
space by recursively subdividing it into eight octants. This particular implementation can have up to sixteen levels and stores up to eight triangles
in leaf nodes. Octree can be used in games to compute collision between the game world and colliders from
the player or other dynamic 3D objects.

## Constructor
`newOctree( box :Box3)`
Constructs a new Octree.

## Import

## Properties
- `.bounds :Box3` — The bounds of the Octree. Compared to Octree#box , no
margin is applied.
- `.box :Box3` — The base box with enclose the entire Octree.
- `.layers :Layers` — Can by used for layers configuration for refine testing.
- `.maxLevel : number` — The maximum level of the Octree. It defines the maximum
hierarchical depth of the data structure. Default is 16 .
- `.trianglesPerLeaf : number` — The number of triangles a leaf can store before it is split. Default is 8 .

## Methods
- `.addTriangle( triangle :Triangle) :Octree` — Adds the given triangle to the Octree. The triangle vertices are clamped if they exceed
the bounds of the Octree.
- `.boxIntersect( box :Box3) : Object | boolean` — Performs a bounding box intersection test with this Octree.
- `.build() :Octree` — Builds the Octree.
- `.calcBox() :Octree` — Prepares Octree#box for the build.
- `.capsuleIntersect( capsule :Capsule) : Object | boolean` — Performs a capsule intersection test with this Octree.
- `.clear() :Octree` — Clears the Octree by making it empty.
- `.fromGraphNode( group :Object3D) :Octree` — Constructs the Octree from the given 3D object.
- `.getBoxTriangles( box :Box3, triangles :Array.<Triangle>)` — Computes the triangles that potentially intersect with the given bounding box.
- `.getCapsuleTriangles( capsule :Capsule, triangles :Array.<Triangle>)` — Computes the triangles that potentially intersect with the given capsule.
- `.getRayTriangles( ray :Ray, triangles :Array.<Triangle>)` — Computes the triangles that potentially intersect with the given ray.
- `.getSphereTriangles( sphere :Sphere, triangles :Array.<Triangle>)` — Computes the triangles that potentially intersect with the given bounding sphere.
- `.rayIntersect( ray :Ray) : Object | boolean` — Performs a ray intersection test with this Octree.
- `.sphereIntersect( sphere :Sphere) : Object | boolean` — Performs a bounding sphere intersection test with this Octree.
- `.split( level :number) :Octree` — Splits the Octree. This method is used recursively when
building the Octree.
- `.triangleBoxIntersect( box :Box3, triangle :Triangle) : Object | false` — Computes the intersection between the given bounding box and triangle.
- `.triangleCapsuleIntersect( capsule :Capsule, triangle :Triangle) : Object | false` — Computes the intersection between the given capsule and triangle.
- `.triangleSphereIntersect( sphere :Sphere, triangle :Triangle) : Object | false` — Computes the intersection between the given sphere and triangle.

## Source