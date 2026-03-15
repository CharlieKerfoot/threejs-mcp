# Object3D
Extends: EventDispatcher→

This is the base class for most objects in three.js and provides a set of
properties and methods for manipulating objects in 3D space.

## Constructor
`newObject3D()`
Constructs a new 3D object.

## Properties
- `.animations : Array.<AnimationClip>` — An array holding the animation clips of the 3D object.
- `.castShadow : boolean` — When set to true , the 3D object gets rendered into shadow maps. Default is false .
- `.children : Array.<Object3D>` — An array holding the child 3D objects of this instance.
- `.customDepthMaterial :Material| undefined` — Custom depth material to be used when rendering to the depth map. Can only be used
in context of meshes. When shadow-casting with a DirectionalLight or SpotLight ,
if you are modifying vertex posit...
- `.customDistanceMaterial :Material| undefined` — Same as Object3D#customDepthMaterial , but used with PointLight . Only relevant in context of WebGLRenderer . Default is undefined .
- `.frustumCulled : boolean` — When set to true , the 3D object is honored by view frustum culling. Default is true .
- `.id : number` — The ID of the 3D object.
- `.isObject3D : boolean` — This flag can be used for type testing. Default is true .
- `.layers :Layers` — The layer membership of the 3D object. The 3D object is only visible if it has
at least one layer in common with the camera in use. This property can also be
used to filter out unwanted objects in ...
- `.matrix :Matrix4` — Represents the object's transformation matrix in local space.
- `.matrixAutoUpdate : boolean` — When set to true , the engine automatically computes the local matrix from position,
rotation and scale every frame. If set to false , the app is responsible for recomputing
the local matrix by cal...
- `.matrixWorld :Matrix4` — Represents the object's transformation matrix in world space.
If the 3D object has no parent, then it's identical to the local transformation matrix
- `.matrixWorldAutoUpdate : boolean` — When set to true , the engine automatically computes the world matrix from the current local
matrix and the object's transformation hierarchy. If set to false , the app is responsible for
recomputi...
- `.matrixWorldNeedsUpdate : boolean` — When set to true , it calculates the world matrix in that frame and resets this property
to false . Default is false .
- `.modelViewMatrix :Matrix4` — Represents the object's model-view matrix.
- `.name : string` — The name of the 3D object.
- `.normalMatrix :Matrix3` — Represents the object's normal matrix.
- `.parent :Object3D` — A reference to the parent object. Default is null .
- `.pivot :Vector3` — The pivot point for rotation and scale transformations.
When set, rotation and scale are applied around this point
instead of the object's origin. Default is null .
- `.position :Vector3` — Represents the object's local position. Default is (0,0,0) .
- `.quaternion :Quaternion` — Represents the object's local rotation as Quaternions.
- `.receiveShadow : boolean` — When set to true , the 3D object is affected by shadows in the scene. Default is false .
- `.renderOrder : number` — This value allows the default rendering order of scene graph objects to be
overridden although opaque and transparent objects remain sorted independently.
When this property is set for an instance ...
- `.rotation :Euler` — Represents the object's local rotation as Euler angles, in radians. Default is (0,0,0) .
- `.scale :Vector3` — Represents the object's local scale. Default is (1,1,1) .
- `.static : boolean` — Whether the 3D object is supposed to be static or not. If set to true , it means
the 3D object is not going to be changed after the initial renderer. This includes
geometry and material settings. A...
- `.type : string` — The type property is used for detecting the object type
in context of serialization/deserialization.
- `.up :Vector3` — Defines the up direction of the 3D object which influences
the orientation via methods like Object3D#lookAt . The default values for all 3D objects is defined by Object3D.DEFAULT_UP .
- `.userData : Object` — An object that can be used to store custom data about the 3D object. It
should not hold references to functions as these will not be cloned.
- `.uuid : string` — The UUID of the 3D object.
- `.visible : boolean` — When set to true , the 3D object gets rendered. Default is true .
- `.DEFAULT_MATRIX_AUTO_UPDATE : boolean` — The default setting for Object3D#matrixAutoUpdate for
newly created 3D objects. Default is true .
- `.DEFAULT_MATRIX_WORLD_AUTO_UPDATE : boolean` — The default setting for Object3D#matrixWorldAutoUpdate for
newly created 3D objects. Default is true .
- `.DEFAULT_UP :Vector3` — The default up direction for objects, also used as the default
position for DirectionalLight and HemisphereLight . Default is (0,1,0) .

## Methods
- `.add( object :Object3D) :Object3D` — Adds the given 3D object as a child to this 3D object. An arbitrary number of
objects may be added. Any current parent on an object passed in here will be
removed, since an object can have at most ...
- `.applyMatrix4( matrix :Matrix4)` — Applies the given transformation matrix to the object and updates the object's position,
rotation and scale.
- `.applyQuaternion( q :Quaternion) :Object3D` — Applies a rotation represented by given the quaternion to the 3D object.
- `.attach( object :Object3D) :Object3D` — Adds the given 3D object as a child of this 3D object, while maintaining the object's world
transform. This method does not support scene graphs having non-uniformly-scaled nodes(s).
- `.clear() :Object3D` — Removes all child objects.
- `.clone( recursive :boolean) :Object3D` — Returns a new 3D object with copied values from this instance.
- `.copy( source :Object3D, recursive :boolean) :Object3D` — Copies the values of the given 3D object to this instance.
- `.getObjectById( id :number) :Object3D| undefined` — Searches through the 3D object and its children, starting with the 3D object
itself, and returns the first with a matching ID.
- `.getObjectByName( name :string) :Object3D| undefined` — Searches through the 3D object and its children, starting with the 3D object
itself, and returns the first with a matching name.
- `.getObjectByProperty( name :string, value :any) :Object3D| undefined` — Searches through the 3D object and its children, starting with the 3D object
itself, and returns the first with a matching property value.
- `.getObjectsByProperty( name :string, value :any, result :Array.<Object3D>) : Array.<Object3D>` — Searches through the 3D object and its children, starting with the 3D object
itself, and returns all 3D objects with a matching property value.
- `.getWorldDirection( target :Vector3) :Vector3` — Returns a vector representing the ("look") direction of the 3D object in world space.
- `.getWorldPosition( target :Vector3) :Vector3` — Returns a vector representing the position of the 3D object in world space.
- `.getWorldQuaternion( target :Quaternion) :Quaternion` — Returns a Quaternion representing the position of the 3D object in world space.
- `.getWorldScale( target :Vector3) :Vector3` — Returns a vector representing the scale of the 3D object in world space.
- `.localToWorld( vector :Vector3) :Vector3` — Converts the given vector from this 3D object's local space to world space.
- `.lookAt( x :number |Vector3, y :number, z :number)` — Rotates the object to face a point in world space. This method does not support objects having non-uniformly-scaled parent(s).
- `.onAfterRender( renderer :Renderer|WebGLRenderer, object :Object3D, camera :Camera, geometry :BufferGeometry, material :Material, group :Object)` — A callback that is executed immediately after a 3D object is rendered.
- `.onAfterShadow( renderer :Renderer|WebGLRenderer, object :Object3D, camera :Camera, shadowCamera :Camera, geometry :BufferGeometry, depthMaterial :Material, group :Object)` — A callback that is executed immediately after a 3D object is rendered to a shadow map.
- `.onBeforeRender( renderer :Renderer|WebGLRenderer, object :Object3D, camera :Camera, geometry :BufferGeometry, material :Material, group :Object)` — A callback that is executed immediately before a 3D object is rendered.
- `.onBeforeShadow( renderer :Renderer|WebGLRenderer, object :Object3D, camera :Camera, shadowCamera :Camera, geometry :BufferGeometry, depthMaterial :Material, group :Object)` — A callback that is executed immediately before a 3D object is rendered to a shadow map.
- `.raycast( raycaster :Raycaster, intersects :Array.<Object>) (abstract)` — Abstract method to get intersections between a casted ray and this
3D object. Renderable 3D objects such as Mesh , Line or Points implement this method in order to use raycasting.
- `.remove( object :Object3D) :Object3D` — Removes the given 3D object as child from this 3D object.
An arbitrary number of objects may be removed.
- `.removeFromParent() :Object3D` — Removes this 3D object from its current parent.
- `.rotateOnAxis( axis :Vector3, angle :number) :Object3D` — Rotates the 3D object along an axis in local space.
- `.rotateOnWorldAxis( axis :Vector3, angle :number) :Object3D` — Rotates the 3D object along an axis in world space.
- `.rotateX( angle :number) :Object3D` — Rotates the 3D object around its X axis in local space.
- `.rotateY( angle :number) :Object3D` — Rotates the 3D object around its Y axis in local space.
- `.rotateZ( angle :number) :Object3D` — Rotates the 3D object around its Z axis in local space.
- `.setRotationFromAxisAngle( axis :Vector3, angle :number)` — Sets the given rotation represented as an axis/angle couple to the 3D object.
- `.setRotationFromEuler( euler :Euler)` — Sets the given rotation represented as Euler angles to the 3D object.
- `.setRotationFromMatrix( m :Matrix4)` — Sets the given rotation represented as rotation matrix to the 3D object.
- `.setRotationFromQuaternion( q :Quaternion)` — Sets the given rotation represented as a Quaternion to the 3D object.
- `.toJSON( meta :Object | string) : Object` — Serializes the 3D object into JSON.
- `.translateOnAxis( axis :Vector3, distance :number) :Object3D` — Translate the 3D object by a distance along the given axis in local space.
- `.translateX( distance :number) :Object3D` — Translate the 3D object by a distance along its X-axis in local space.
- `.translateY( distance :number) :Object3D` — Translate the 3D object by a distance along its Y-axis in local space.
- `.translateZ( distance :number) :Object3D` — Translate the 3D object by a distance along its Z-axis in local space.
- `.traverse( callback :function)` — Executes the callback on this 3D object and all descendants. Note: Modifying the scene graph inside the callback is discouraged.
- `.traverseAncestors( callback :function)` — Like Object3D#traverse , but the callback will only be executed for all ancestors. Note: Modifying the scene graph inside the callback is discouraged.
- `.traverseVisible( callback :function)` — Like Object3D#traverse , but the callback will only be executed for visible 3D objects.
Descendants of invisible 3D objects are not traversed. Note: Modifying the scene graph inside the callback is...
- `.updateMatrix()` — Updates the transformation matrix in local space by computing it from the current
position, rotation and scale values.
- `.updateMatrixWorld( force :boolean)` — Updates the transformation matrix in world space of this 3D objects and its descendants. To ensure correct results, this method also recomputes the 3D object's transformation matrix in
local space....
- `.updateWorldMatrix( updateParents :boolean, updateChildren :boolean)` — An alternative version of Object3D#updateMatrixWorld with more control over the
update of ancestor and descendant nodes.
- `.worldToLocal( vector :Vector3) :Vector3` — Converts the given vector from this 3D object's world space to local space.

## Events
- `.added` — Fires when the object has been added to its parent object.
- `.childadded` — Fires when a new child object has been added.
- `.childremoved` — Fires when a child object has been removed.
- `.removed` — Fires when the object has been removed from its parent object.

## Source