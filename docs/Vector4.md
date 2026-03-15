# Vector4

Class representing a 4D vector. A 4D vector is an ordered quadruplet of numbers
(labeled x, y, z and w), which can be used to represent a number of things, such as: A point in 4D space. A direction and length in 4D space. In three.js the length will
always be the Euclidean distance(straight-line distance) from (0, 0, 0, 0) to (x, y, z, w) and the direction is also measured from (0, 0, 0, 0) towards (x, y, z, w) . Any arbitrary ordered quadruplet of numbers. There are other things a 4D vector can be used to represent, however these
are the most common uses in three.js . Iterating through a vector instance will yield its components (x, y, z, w) in
the corresponding order.

## Constructor
`newVector4( x :number, y :number, z :number, w :number)`
Constructs a new 4D vector.

## Properties
- `.height : number` — Alias for Vector4#w .
- `.isVector4 : boolean` — This flag can be used for type testing. Default is true .
- `.w : number` — The w value of this vector.
- `.width : number` — Alias for Vector4#z .
- `.x : number` — The x value of this vector.
- `.y : number` — The y value of this vector.
- `.z : number` — The z value of this vector.

## Methods
- `.add( v :Vector4) :Vector4` — Adds the given vector to this instance.
- `.addScalar( s :number) :Vector4` — Adds the given scalar value to all components of this instance.
- `.addScaledVector( v :Vector4, s :number) :Vector4` — Adds the given vector scaled by the given factor to this instance.
- `.addVectors( a :Vector4, b :Vector4) :Vector4` — Adds the given vectors and stores the result in this instance.
- `.applyMatrix4( m :Matrix4) :Vector4` — Multiplies this vector with the given 4x4 matrix.
- `.ceil() :Vector4` — The components of this vector are rounded up to the nearest integer value.
- `.clamp( min :Vector4, max :Vector4) :Vector4` — If this vector's x, y, z or w value is greater than the max vector's x, y, z or w
value, it is replaced by the corresponding value.
If this vector's x, y, z or w value is less than the min vector's...
- `.clampLength( min :number, max :number) :Vector4` — If this vector's length is greater than the max value, it is replaced by
the max value.
If this vector's length is less than the min value, it is replaced by the
min value.
- `.clampScalar( minVal :number, maxVal :number) :Vector4` — If this vector's x, y, z or w values are greater than the max value, they are
replaced by the max value.
If this vector's x, y, z or w values are less than the min value, they are
replaced by the m...
- `.clone() :Vector4` — Returns a new vector with copied values from this instance.
- `.copy( v :Vector3|Vector4) :Vector4` — Copies the values of the given vector to this instance.
- `.divide( v :Vector4) :Vector4` — Divides this instance by the given vector.
- `.divideScalar( scalar :number) :Vector4` — Divides this vector by the given scalar.
- `.dot( v :Vector4) : number` — Calculates the dot product of the given vector with this instance.
- `.equals( v :Vector4) : boolean` — Returns true if this vector is equal with the given one.
- `.floor() :Vector4` — The components of this vector are rounded down to the nearest integer value.
- `.fromArray( array :Array.<number>, offset :number) :Vector4` — Sets this vector's x value to be array[ offset ] , y value to be array[ offset + 1 ] ,
z value to be array[ offset + 2 ] , w value to be array[ offset + 3 ] .
- `.fromBufferAttribute( attribute :BufferAttribute, index :number) :Vector4` — Sets the components of this vector from the given buffer attribute.
- `.getComponent( index :number) : number` — Returns the value of the vector component which matches the given index.
- `.length() : number` — Computes the  Euclidean length (straight-line length) from (0, 0, 0, 0) to (x, y, z, w).
- `.lengthSq() : number` — Computes the square of the Euclidean length (straight-line length) from
(0, 0, 0, 0) to (x, y, z, w). If you are comparing the lengths of vectors, you should
compare the length squared instead as i...
- `.lerp( v :Vector4, alpha :number) :Vector4` — Linearly interpolates between the given vector and this instance, where
alpha is the percent distance along the line - alpha = 0 will be this
vector, and alpha = 1 will be the given one.
- `.lerpVectors( v1 :Vector4, v2 :Vector4, alpha :number) :Vector4` — Linearly interpolates between the given vectors, where alpha is the percent
distance along the line - alpha = 0 will be first vector, and alpha = 1 will
be the second one. The result is stored in t...
- `.manhattanLength() : number` — Computes the Manhattan length of this vector.
- `.max( v :Vector4) :Vector4` — If this vector's x, y, z or w value is less than the given vector's x, y, z or w
value, replace that value with the corresponding max value.
- `.min( v :Vector4) :Vector4` — If this vector's x, y, z or w value is greater than the given vector's x, y, z or w
value, replace that value with the corresponding min value.
- `.multiply( v :Vector4) :Vector4` — Multiplies the given vector with this instance.
- `.multiplyScalar( scalar :number) :Vector4` — Multiplies the given scalar value with all components of this instance.
- `.negate() :Vector4` — Inverts this vector - i.e. sets x = -x, y = -y, z = -z, w = -w.
- `.normalize() :Vector4` — Converts this vector to a unit vector - that is, sets it equal to a vector
with the same direction as this one, but with a vector length of 1 .
- `.random() :Vector4` — Sets each component of this vector to a pseudo-random value between 0 and 1 , excluding 1 .
- `.round() :Vector4` — The components of this vector are rounded to the nearest integer value
- `.roundToZero() :Vector4` — The components of this vector are rounded towards zero (up if negative,
down if positive) to an integer value.
- `.set( x :number, y :number, z :number, w :number) :Vector4` — Sets the vector components.
- `.setAxisAngleFromQuaternion( q :Quaternion) :Vector4` — Sets the x, y and z components of this
vector to the quaternion's axis and w to the angle.
- `.setAxisAngleFromRotationMatrix( m :Matrix4) :Vector4` — Sets the x, y and z components of this
vector to the axis of rotation and w to the angle.
- `.setComponent( index :number, value :number) :Vector4` — Allows to set a vector component with an index.
- `.setFromMatrixPosition( m :Matrix4) :Vector4` — Sets the vector components to the position elements of the
given transformation matrix.
- `.setLength( length :number) :Vector4` — Sets this vector to a vector with the same direction as this one, but
with the specified length.
- `.setScalar( scalar :number) :Vector4` — Sets the vector components to the same value.
- `.setW( w :number) :Vector4` — Sets the vector's w component to the given value
- `.setX( x :number) :Vector4` — Sets the vector's x component to the given value
- `.setY( y :number) :Vector4` — Sets the vector's y component to the given value
- `.setZ( z :number) :Vector4` — Sets the vector's z component to the given value
- `.sub( v :Vector4) :Vector4` — Subtracts the given vector from this instance.
- `.subScalar( s :number) :Vector4` — Subtracts the given scalar value from all components of this instance.
- `.subVectors( a :Vector4, b :Vector4) :Vector4` — Subtracts the given vectors and stores the result in this instance.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the components of this vector to the given array. If no array is provided,
the method returns a new instance.

## Source