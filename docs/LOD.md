# LOD
Extends: EventDispatcher→Object3D→

A component for providing a basic Level of Detail (LOD) mechanism. Every LOD level is associated with an object, and rendering can be switched
between them at the distances specified. Typically you would create, say,
three meshes, one for far away (low detail), one for mid range (medium
detail) and one for close up (high detail).

## Constructor
`newLOD()`
Constructs a new LOD.

## Properties
- `.autoUpdate : boolean` — Whether the LOD object is updated automatically by the renderer per frame
or not. If set to false , you have to call LOD#update in the
render loop by yourself. Default is true .
- `.isLOD : boolean` — This flag can be used for type testing. Default is true .
- `.levels : Array.<{object:Object3D, distance:number, hysteresis:number}>` — This array holds the LOD levels.

## Methods
- `.addLevel( object :Object3D, distance :number, hysteresis :number) :LOD` — Adds a mesh that will display at a certain distance and greater. Typically
the further away the distance, the lower the detail on the mesh.
- `.getCurrentLevel() : number` — Returns the currently active LOD level index.
- `.getObjectForDistance( distance :number) :Object3D` — Returns a reference to the first 3D object that is greater than
the given distance.
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>)` — Computes intersection points between a casted ray and this LOD.
- `.removeLevel( distance :number) : boolean` — Removes an existing level, based on the distance from the camera.
Returns true when the level has been removed. Otherwise false .
- `.update( camera :Camera)` — Updates the LOD by computing which LOD level should be visible according
to the current distance of the given camera.

## Source