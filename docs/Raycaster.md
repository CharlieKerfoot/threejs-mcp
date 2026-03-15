# Raycaster

This class is designed to assist with raycasting. Raycasting is used for
mouse picking (working out what objects in the 3d space the mouse is over)
amongst other things.

## Constructor
`newRaycaster( origin :Vector3, direction :Vector3, near :number, far :number)`
Constructs a new raycaster.

## Properties
- `.camera :Camera` — The camera to use when raycasting against view-dependent objects such as
billboarded objects like sprites. This field can be set manually or
is set when calling setFromCamera() . Default is null .
- `.far : number` — All results returned are closer than far. Far can't be lower than near. Default is Infinity .
- `.layers :Layers` — Allows to selectively ignore 3D objects when performing intersection tests.
The following code example ensures that only 3D objects on layer 1 will be
honored by raycaster. raycaster.layers.set( 1 ...
- `.near : number` — All results returned are further away than near. Near can't be negative. Default is 0 .
- `.params : Object` — A parameter object that configures the raycasting. It has the structure: {
	Mesh: {},
	Line: { threshold: 1 },
	LOD: {},
	Points: { threshold: 1 },
	Sprite: {}
} Where threshold is the precision of...
- `.ray :Ray` — The ray used for raycasting.

## Methods
- `.intersectObject( object :Object3D, recursive :boolean, intersects :Array.<Raycaster~Intersection>) : Array.<Raycaster~Intersection>` — Checks all intersection between the ray and the object with or without the
descendants. Intersections are returned sorted by distance, closest first. Raycaster delegates to the raycast() method of ...
- `.intersectObjects( objects :Array.<Object3D>, recursive :boolean, intersects :Array.<Raycaster~Intersection>) : Array.<Raycaster~Intersection>` — Checks all intersection between the ray and the objects with or without
the descendants. Intersections are returned sorted by distance, closest first.
- `.set( origin :Vector3, direction :Vector3)` — Updates the ray with a new origin and direction by copying the values from the arguments.
- `.setFromCamera( coords :Vector2, camera :Camera)` — Uses the given coordinates and camera to compute a new origin and direction for the internal ray.
- `.setFromXRController( controller :WebXRController) :Raycaster` — Uses the given WebXR controller to compute a new origin and direction for the internal ray.

## Type Definitions
- `.Intersection` — The intersection point of a raycaster intersection test.

## Source