# Points
Extends: EventDispatcher→Object3D→

A class for displaying points or point clouds.

## Constructor
`newPoints( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new point cloud.

## Properties
- `.geometry :BufferGeometry` — The points geometry.
- `.isPoints : boolean` — This flag can be used for type testing. Default is true .
- `.material :Material| Array.<Material>` — The line material. Default is PointsMaterial .
- `.morphTargetDictionary : Object.<string, number> | undefined` — A dictionary representing the morph targets in the geometry. The key is the
morph targets name, the value its attribute index. This member is undefined by default and only set when morph targets ar...
- `.morphTargetInfluences : Array.<number> | undefined` — An array of weights typically in the range [0,1] that specify how much of the morph
is applied. This member is undefined by default and only set when morph targets are
detected in the geometry. Def...

## Methods
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>)` — Computes intersection points between a casted ray and this point cloud.
- `.updateMorphTargets()` — Sets the values of Points#morphTargetDictionary and Points#morphTargetInfluences to make sure existing morph targets can influence this 3D object.

## Source