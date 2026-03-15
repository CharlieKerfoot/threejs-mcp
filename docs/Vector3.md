# Vector3

Class representing a 3D vector. A 3D vector is an ordered triplet of numbers
(labeled x, y and z), which can be used to represent a number of things, such as: A point in 3D space. A direction and length in 3D space. In three.js the length will
always be the Euclidean distance(straight-line distance) from (0, 0, 0) to (x, y, z) and the direction is also measured from (0, 0, 0) towards (x, y, z) . Any arbitrary ordered triplet of numbers. There are other things a 3D vector can be used to represent, such as
momentum vectors and so on, however these are the most
common uses in three.js. Iterating through a vector instance will yield its components (x, y, z) in
the corresponding order.

## Constructor
`newVector3( x :number, y :number, z :number)`
Constructs a new 3D vector.

## Properties
- `.isVector3 : boolean` — This flag can be used for type testing. Default is true .
- `.x : number` — The x value of this vector.
- `.y : number` — The y value of this vector.
- `.z : number` — The z value of this vector.

## Methods
- `.add( v :Vector3) :Vector3` — Adds the given vector to this instance.
- `.addScalar( s :number) :Vector3` — Adds the given scalar value to all components of this instance.
- `.addScaledVector( v :Vector3|Vector4, s :number) :Vector3` — Adds the given vector scaled by the given factor to this instance.
- `.addVectors( a :Vector3, b :Vector3) :Vector3` — Adds the given vectors and stores the result in this instance.
- `.angleTo( v :Vector3) : number` — Returns the angle between the given vector and this instance in radians.
- `.applyAxisAngle( axis :Vector3, angle :number) :Vector3` — Applies a rotation specified by an axis and an angle to this vector.
- `.applyEuler( euler :Euler) :Vector3` — Applies the given Euler rotation to this vector.
- `.applyMatrix3( m :Matrix3) :Vector3` — Multiplies this vector with the given 3x3 matrix.
- `.applyMatrix4( m :Matrix4) :Vector3` — Multiplies this vector (with an implicit 1 in the 4th dimension) by m, and
divides by perspective.
- `.applyNormalMatrix( m :Matrix3) :Vector3` — Multiplies this vector by the given normal matrix and normalizes
the result.
- `.applyQuaternion( q :Quaternion) :Vector3` — Applies the given Quaternion to this vector.
- `.ceil() :Vector3` — The components of this vector are rounded up to the nearest integer value.
- `.clamp( min :Vector3, max :Vector3) :Vector3` — If this vector's x, y or z value is greater than the max vector's x, y or z
value, it is replaced by the corresponding value.
If this vector's x, y or z value is less than the min vector's x, y or ...
- `.clampLength( min :number, max :number) :Vector3` — If this vector's length is greater than the max value, it is replaced by
the max value.
If this vector's length is less than the min value, it is replaced by the
min value.
- `.clampScalar( minVal :number, maxVal :number) :Vector3` — If this vector's x, y or z values are greater than the max value, they are
replaced by the max value.
If this vector's x, y or z values are less than the min value, they are
replaced by the min value.
- `.clone() :Vector3` — Returns a new vector with copied values from this instance.
- `.copy( v :Vector3) :Vector3` — Copies the values of the given vector to this instance.
- `.cross( v :Vector3) :Vector3` — Calculates the cross product of the given vector with this instance.
- `.crossVectors( a :Vector3, b :Vector3) :Vector3` — Calculates the cross product of the given vectors and stores the result
in this instance.
- `.distanceTo( v :Vector3) : number` — Computes the distance from the given vector to this instance.
- `.distanceToSquared( v :Vector3) : number` — Computes the squared distance from the given vector to this instance.
If you are just comparing the distance with another distance, you should compare
the distance squared instead as it is slightly...
- `.divide( v :Vector3) :Vector3` — Divides this instance by the given vector.
- `.divideScalar( scalar :number) :Vector3` — Divides this vector by the given scalar.
- `.dot( v :Vector3) : number` — Calculates the dot product of the given vector with this instance.
- `.equals( v :Vector3) : boolean` — Returns true if this vector is equal with the given one.
- `.floor() :Vector3` — The components of this vector are rounded down to the nearest integer value.
- `.fromArray( array :Array.<number>, offset :number) :Vector3` — Sets this vector's x value to be array[ offset ] , y value to be array[ offset + 1 ] and z value to be array[ offset + 2 ] .
- `.fromBufferAttribute( attribute :BufferAttribute, index :number) :Vector3` — Sets the components of this vector from the given buffer attribute.
- `.getComponent( index :number) : number` — Returns the value of the vector component which matches the given index.
- `.length() : number` — Computes the  Euclidean length (straight-line length) from (0, 0, 0) to (x, y, z).
- `.lengthSq() : number` — Computes the square of the Euclidean length (straight-line length) from
(0, 0, 0) to (x, y, z). If you are comparing the lengths of vectors, you should
compare the length squared instead as it is s...
- `.lerp( v :Vector3, alpha :number) :Vector3` — Linearly interpolates between the given vector and this instance, where
alpha is the percent distance along the line - alpha = 0 will be this
vector, and alpha = 1 will be the given one.
- `.lerpVectors( v1 :Vector3, v2 :Vector3, alpha :number) :Vector3` — Linearly interpolates between the given vectors, where alpha is the percent
distance along the line - alpha = 0 will be first vector, and alpha = 1 will
be the second one. The result is stored in t...
- `.manhattanDistanceTo( v :Vector3) : number` — Computes the Manhattan distance from the given vector to this instance.
- `.manhattanLength() : number` — Computes the Manhattan length of this vector.
- `.max( v :Vector3) :Vector3` — If this vector's x, y or z value is less than the given vector's x, y or z
value, replace that value with the corresponding max value.
- `.min( v :Vector3) :Vector3` — If this vector's x, y or z value is greater than the given vector's x, y or z
value, replace that value with the corresponding min value.
- `.multiply( v :Vector3) :Vector3` — Multiplies the given vector with this instance.
- `.multiplyScalar( scalar :number) :Vector3` — Multiplies the given scalar value with all components of this instance.
- `.multiplyVectors( a :Vector3, b :Vector3) :Vector3` — Multiplies the given vectors and stores the result in this instance.
- `.negate() :Vector3` — Inverts this vector - i.e. sets x = -x, y = -y and z = -z.
- `.normalize() :Vector3` — Converts this vector to a unit vector - that is, sets it equal to a vector
with the same direction as this one, but with a vector length of 1 .
- `.project( camera :Camera) :Vector3` — Projects this vector from world space into the camera's normalized
device coordinate (NDC) space.
- `.projectOnPlane( planeNormal :Vector3) :Vector3` — Projects this vector onto a plane by subtracting this
vector projected onto the plane's normal from this vector.
- `.projectOnVector( v :Vector3) :Vector3` — Projects this vector onto the given one.
- `.random() :Vector3` — Sets each component of this vector to a pseudo-random value between 0 and 1 , excluding 1 .
- `.randomDirection() :Vector3` — Sets this vector to a uniformly random point on a unit sphere.
- `.reflect( normal :Vector3) :Vector3` — Reflects this vector off a plane orthogonal to the given normal vector.
- `.round() :Vector3` — The components of this vector are rounded to the nearest integer value
- `.roundToZero() :Vector3` — The components of this vector are rounded towards zero (up if negative,
down if positive) to an integer value.
- `.set( x :number, y :number, z :number) :Vector3` — Sets the vector components.
- `.setComponent( index :number, value :number) :Vector3` — Allows to set a vector component with an index.
- `.setFromColor( c :Color) :Vector3` — Sets the vector components from the RGB components of the
given color.
- `.setFromCylindrical( c :Cylindrical) :Vector3` — Sets the vector components from the given cylindrical coordinates.
- `.setFromCylindricalCoords( radius :number, theta :number, y :number) :Vector3` — Sets the vector components from the given cylindrical coordinates.
- `.setFromEuler( e :Euler) :Vector3` — Sets the vector components from the given Euler angles.
- `.setFromMatrix3Column( m :Matrix3, index :number) :Vector3` — Sets the vector components from the specified matrix column.
- `.setFromMatrixColumn( m :Matrix4, index :number) :Vector3` — Sets the vector components from the specified matrix column.
- `.setFromMatrixPosition( m :Matrix4) :Vector3` — Sets the vector components to the position elements of the
given transformation matrix.
- `.setFromMatrixScale( m :Matrix4) :Vector3` — Sets the vector components to the scale elements of the
given transformation matrix.
- `.setFromSpherical( s :Spherical) :Vector3` — Sets the vector components from the given spherical coordinates.
- `.setFromSphericalCoords( radius :number, phi :number, theta :number) :Vector3` — Sets the vector components from the given spherical coordinates.
- `.setLength( length :number) :Vector3` — Sets this vector to a vector with the same direction as this one, but
with the specified length.
- `.setScalar( scalar :number) :Vector3` — Sets the vector components to the same value.
- `.setX( x :number) :Vector3` — Sets the vector's x component to the given value.
- `.setY( y :number) :Vector3` — Sets the vector's y component to the given value.
- `.setZ( z :number) :Vector3` — Sets the vector's z component to the given value.
- `.sub( v :Vector3) :Vector3` — Subtracts the given vector from this instance.
- `.subScalar( s :number) :Vector3` — Subtracts the given scalar value from all components of this instance.
- `.subVectors( a :Vector3, b :Vector3) :Vector3` — Subtracts the given vectors and stores the result in this instance.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the components of this vector to the given array. If no array is provided,
the method returns a new instance.
- `.transformDirection( m :Matrix4) :Vector3` — Transforms the direction of this vector by a matrix (the upper left 3 x 3
subset of the given 4x4 matrix and then normalizes the result.
- `.unproject( camera :Camera) :Vector3` — Unprojects this vector from the camera's normalized device coordinate (NDC)
space into world space.

## Source