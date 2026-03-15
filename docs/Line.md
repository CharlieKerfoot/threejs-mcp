# Line
Extends: EventDispatcher→Object3D→

A continuous line. The line are rendered by connecting consecutive
vertices with straight lines.

## Constructor
`newLine( geometry :BufferGeometry, material :Material| Array.<Material>)`
Constructs a new line.

## Properties
- `.geometry :BufferGeometry` — The line geometry.
- `.isLine : boolean` — This flag can be used for type testing. Default is true .
- `.material :Material| Array.<Material>` — The line material. Default is LineBasicMaterial .
- `.morphTargetDictionary : Object.<string, number> | undefined` — A dictionary representing the morph targets in the geometry. The key is the
morph targets name, the value its attribute index. This member is undefined by default and only set when morph targets ar...
- `.morphTargetInfluences : Array.<number> | undefined` — An array of weights typically in the range [0,1] that specify how much of the morph
is applied. This member is undefined by default and only set when morph targets are
detected in the geometry. Def...

## Methods
- `.computeLineDistances() :Line` — Computes an array of distance values which are necessary for rendering dashed lines.
For each vertex in the geometry, the method calculates the cumulative length from the
current point to the very ...
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>)` — Computes intersection points between a casted ray and this line.
- `.updateMorphTargets()` — Sets the values of Line#morphTargetDictionary and Line#morphTargetInfluences to make sure existing morph targets can influence this 3D object.

## Source