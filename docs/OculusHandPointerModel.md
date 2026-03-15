# OculusHandPointerModel
Extends: EventDispatcher→Object3D→

Represents an Oculus hand pointer model.

## Constructor
`newOculusHandPointerModel( hand :Group, controller :Group)`
Constructs a new Oculus hand model.

## Import

## Properties
- `.attached : boolean` — Whether the model is attached or not. Default is false .
- `.controller :Group` — The WebXR controller in target ray space.
- `.cursorObject :Mesh` — The cursor object. Default is null .
- `.hand :Group` — The hand controller.
- `.pinched : boolean` — Whether the model is pinched or not. Default is false .
- `.pointerGeometry :BufferGeometry` — The pointer geometry. Default is null .
- `.pointerMesh :Mesh` — The pointer mesh. Default is null .
- `.pointerObject :Object3D` — The pointer object that holds the pointer mesh. Default is null .
- `.raycaster :Raycaster` — The internal raycaster used for detecting
intersections. Default is null .

## Methods
- `.checkIntersections( objects :Array.<Object3D>, recursive :boolean)` — Checks for intersections between the model's raycaster and the given objects. The method
updates the cursor object to the intersection point.
- `.createPointer()` — Creates a pointer mesh and adds it to this model.
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.intersectObject( object :Object3D, recursive :boolean) : Array.<Raycaster~Intersection>` — Performs an intersection test with the model's raycaster and the given object.
- `.intersectObjects( objects :Array.<Object3D>, recursive :boolean) : Array.<Raycaster~Intersection>` — Performs an intersection test with the model's raycaster and the given objects.
- `.isAttached() : boolean` — Returns true is the model is attached.
- `.isPinched() : boolean` — Returns true is the model is pinched.
- `.setAttached( attached :boolean)` — Sets the attached state.
- `.setCursor( distance :number)` — Sets the cursor to the given distance.
- `.updateMatrixWorld( force :boolean)` — Overwritten with a custom implementation. Makes sure the internal pointer and raycaster are updated.

## Source