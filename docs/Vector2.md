# Vector2

Class representing a 2D vector. A 2D vector is an ordered pair of numbers
(labeled x and y), which can be used to represent a number of things, such as: A point in 2D space (i.e. a position on a plane). A direction and length across a plane. In three.js the length will
always be the Euclidean distance(straight-line distance) from (0, 0) to (x, y) and the direction is also measured from (0, 0) towards (x, y) . Any arbitrary ordered pair of numbers. There are other things a 2D vector can be used to represent, such as
momentum vectors, complex numbers and so on, however these are the most
common uses in three.js. Iterating through a vector instance will yield its components (x, y) in
the corresponding order.

## Constructor
`newVector2( x :number, y :number)`
Constructs a new 2D vector.

## Properties
- `.height : number` — Alias for Vector2#y .
- `.isVector2 : boolean` — This flag can be used for type testing. Default is true .
- `.width : number` — Alias for Vector2#x .
- `.x : number` — The x value of this vector.
- `.y : number` — The y value of this vector.

## Methods
- `.add( v :Vector2) :Vector2` — Adds the given vector to this instance.
- `.addScalar( s :number) :Vector2` — Adds the given scalar value to all components of this instance.
- `.addScaledVector( v :Vector2, s :number) :Vector2` — Adds the given vector scaled by the given factor to this instance.
- `.addVectors( a :Vector2, b :Vector2) :Vector2` — Adds the given vectors and stores the result in this instance.
- `.angle() : number` — Computes the angle in radians of this vector with respect to the positive x-axis.
- `.angleTo( v :Vector2) : number` — Returns the angle between the given vector and this instance in radians.
- `.applyMatrix3( m :Matrix3) :Vector2` — Multiplies this vector (with an implicit 1 as the 3rd component) by
the given 3x3 matrix.
- `.ceil() :Vector2` — The components of this vector are rounded up to the nearest integer value.
- `.clamp( min :Vector2, max :Vector2) :Vector2` — If this vector's x or y value is greater than the max vector's x or y
value, it is replaced by the corresponding value.
If this vector's x or y value is less than the min vector's x or y value,
it ...
- `.clampLength( min :number, max :number) :Vector2` — If this vector's length is greater than the max value, it is replaced by
the max value.
If this vector's length is less than the min value, it is replaced by the
min value.
- `.clampScalar( minVal :number, maxVal :number) :Vector2` — If this vector's x or y values are greater than the max value, they are
replaced by the max value.
If this vector's x or y values are less than the min value, they are
replaced by the min value.
- `.clone() :Vector2` — Returns a new vector with copied values from this instance.
- `.copy( v :Vector2) :Vector2` — Copies the values of the given vector to this instance.
- `.cross( v :Vector2) : number` — Calculates the cross product of the given vector with this instance.
- `.distanceTo( v :Vector2) : number` — Computes the distance from the given vector to this instance.
- `.distanceToSquared( v :Vector2) : number` — Computes the squared distance from the given vector to this instance.
If you are just comparing the distance with another distance, you should compare
the distance squared instead as it is slightly...
- `.divide( v :Vector2) :Vector2` — Divides this instance by the given vector.
- `.divideScalar( scalar :number) :Vector2` — Divides this vector by the given scalar.
- `.dot( v :Vector2) : number` — Calculates the dot product of the given vector with this instance.
- `.equals( v :Vector2) : boolean` — Returns true if this vector is equal with the given one.
- `.floor() :Vector2` — The components of this vector are rounded down to the nearest integer value.
- `.fromArray( array :Array.<number>, offset :number) :Vector2` — Sets this vector's x value to be array[ offset ] and y
value to be array[ offset + 1 ] .
- `.fromBufferAttribute( attribute :BufferAttribute, index :number) :Vector2` — Sets the components of this vector from the given buffer attribute.
- `.getComponent( index :number) : number` — Returns the value of the vector component which matches the given index.
- `.length() : number` — Computes the  Euclidean length (straight-line length) from (0, 0) to (x, y).
- `.lengthSq() : number` — Computes the square of the Euclidean length (straight-line length) from
(0, 0) to (x, y). If you are comparing the lengths of vectors, you should
compare the length squared instead as it is slightl...
- `.lerp( v :Vector2, alpha :number) :Vector2` — Linearly interpolates between the given vector and this instance, where
alpha is the percent distance along the line - alpha = 0 will be this
vector, and alpha = 1 will be the given one.
- `.lerpVectors( v1 :Vector2, v2 :Vector2, alpha :number) :Vector2` — Linearly interpolates between the given vectors, where alpha is the percent
distance along the line - alpha = 0 will be first vector, and alpha = 1 will
be the second one. The result is stored in t...
- `.manhattanDistanceTo( v :Vector2) : number` — Computes the Manhattan distance from the given vector to this instance.
- `.manhattanLength() : number` — Computes the Manhattan length of this vector.
- `.max( v :Vector2) :Vector2` — If this vector's x or y value is less than the given vector's x or y
value, replace that value with the corresponding max value.
- `.min( v :Vector2) :Vector2` — If this vector's x or y value is greater than the given vector's x or y
value, replace that value with the corresponding min value.
- `.multiply( v :Vector2) :Vector2` — Multiplies the given vector with this instance.
- `.multiplyScalar( scalar :number) :Vector2` — Multiplies the given scalar value with all components of this instance.
- `.negate() :Vector2` — Inverts this vector - i.e. sets x = -x and y = -y.
- `.normalize() :Vector2` — Converts this vector to a unit vector - that is, sets it equal to a vector
with the same direction as this one, but with a vector length of 1 .
- `.random() :Vector2` — Sets each component of this vector to a pseudo-random value between 0 and 1 , excluding 1 .
- `.rotateAround( center :Vector2, angle :number) :Vector2` — Rotates this vector around the given center by the given angle.
- `.round() :Vector2` — The components of this vector are rounded to the nearest integer value
- `.roundToZero() :Vector2` — The components of this vector are rounded towards zero (up if negative,
down if positive) to an integer value.
- `.set( x :number, y :number) :Vector2` — Sets the vector components.
- `.setComponent( index :number, value :number) :Vector2` — Allows to set a vector component with an index.
- `.setLength( length :number) :Vector2` — Sets this vector to a vector with the same direction as this one, but
with the specified length.
- `.setScalar( scalar :number) :Vector2` — Sets the vector components to the same value.
- `.setX( x :number) :Vector2` — Sets the vector's x component to the given value
- `.setY( y :number) :Vector2` — Sets the vector's y component to the given value
- `.sub( v :Vector2) :Vector2` — Subtracts the given vector from this instance.
- `.subScalar( s :number) :Vector2` — Subtracts the given scalar value from all components of this instance.
- `.subVectors( a :Vector2, b :Vector2) :Vector2` — Subtracts the given vectors and stores the result in this instance.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the components of this vector to the given array. If no array is provided,
the method returns a new instance.

## Source