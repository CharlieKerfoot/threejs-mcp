# Mesh
Extends: EventDispatcher→Object3D→

Class representing triangular polygon mesh based objects.

## Constructor
`newMesh( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new mesh.

## Properties
- `.count : number` — The number of instances of this mesh.
Can only be used with WebGPURenderer . Default is 1 .
- `.geometry :BufferGeometry` — The mesh geometry.
- `.isMesh : boolean` — This flag can be used for type testing. Default is true .
- `.material :Material| Array.<Material>` — The mesh material. Default is MeshBasicMaterial .
- `.morphTargetDictionary : Object.<string, number> | undefined` — A dictionary representing the morph targets in the geometry. The key is the
morph targets name, the value its attribute index. This member is undefined by default and only set when morph targets ar...
- `.morphTargetInfluences : Array.<number> | undefined` — An array of weights typically in the range [0,1] that specify how much of the morph
is applied. This member is undefined by default and only set when morph targets are
detected in the geometry. Def...

## Methods
- `.getVertexPosition( index :number, target :Vector3) :Vector3` — Returns the local-space position of the vertex at the given index, taking into
account the current animation state of both morph targets and skinning.
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>)` — Computes intersection points between a casted ray and this line.
- `.updateMorphTargets()` — Sets the values of Mesh#morphTargetDictionary and Mesh#morphTargetInfluences to make sure existing morph targets can influence this 3D object.

## Source