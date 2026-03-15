# SceneUtils

## Import

## Methods
- `.createMeshesFromInstancedMesh( instancedMesh :InstancedMesh) :Group` — This function creates a mesh for each instance of the given instanced mesh and
adds it to a group. Each mesh will honor the current 3D transformation of its
corresponding instance.
- `.createMeshesFromMultiMaterialMesh( mesh :Mesh) :Group` — This function creates a mesh for each geometry-group of the given multi-material mesh and
adds it to a group.
- `.createMultiMaterialObject( geometry :BufferGeometry, materials :Array.<Material>) :Group` — This function represents an alternative way to create 3D objects with multiple materials.
Normally, BufferGeometry#groups are used which might introduce issues e.g. when
exporting the object to a 3...
- `.reduceVertices( object :Object3D, func :function, initialValue :any) :any` — Executes a reducer function for each vertex of the given 3D object. reduceVertices() returns a single value: the function's accumulated result.
- `.sortInstancedMesh( mesh :InstancedMesh, compareFn :function) (inner)` — Sorts the instances of the given instanced mesh.
- `.traverseAncestorsGenerator( object :Object3D) :Object3D` — Generator based alternative to Object3D#traverseAncestors .
- `.traverseGenerator( object :Object3D) :Object3D` — Generator based alternative to Object3D#traverse .
- `.traverseVisibleGenerator( object :Object3D) :Object3D` — Generator based alternative to Object3D#traverseVisible .

## Source