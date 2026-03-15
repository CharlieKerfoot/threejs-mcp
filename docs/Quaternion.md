# Quaternion

Class for representing a Quaternion. Quaternions are used in three.js to represent rotations. Iterating through a vector instance will yield its components (x, y, z, w) in
the corresponding order. Note that three.js expects Quaternions to be normalized.

## Constructor
`newQuaternion( x :number, y :number, z :number, w :number)`
Constructs a new quaternion.

## Properties
- `.isQuaternion : boolean` — This flag can be used for type testing. Default is true .
- `.w : number` — The w value of this quaternion. Default is 1 .
- `.x : number` — The x value of this quaternion. Default is 0 .
- `.y : number` — The y value of this quaternion. Default is 0 .
- `.z : number` — The z value of this quaternion. Default is 0 .

## Methods
- `.angleTo( q :Quaternion) : number` — Returns the angle between this quaternion and the given one in radians.
- `.clone() :Quaternion` — Returns a new quaternion with copied values from this instance.
- `.conjugate() :Quaternion` — Returns the rotational conjugate of this quaternion. The conjugate of a
quaternion represents the same rotation in the opposite direction about
the rotational axis.
- `.copy( quaternion :Quaternion) :Quaternion` — Copies the values of the given quaternion to this instance.
- `.dot( v :Quaternion) : number` — Calculates the dot product of this quaternion and the given one.
- `.equals( quaternion :Quaternion) : boolean` — Returns true if this quaternion is equal with the given one.
- `.fromArray( array :Array.<number>, offset :number) :Quaternion` — Sets this quaternion's components from the given array.
- `.fromBufferAttribute( attribute :BufferAttribute, index :number) :Quaternion` — Sets the components of this quaternion from the given buffer attribute.
- `.identity() :Quaternion` — Sets this quaternion to the identity quaternion; that is, to the
quaternion that represents "no rotation".
- `.invert() :Quaternion` — Inverts this quaternion via Quaternion#conjugate . The
quaternion is assumed to have unit length.
- `.length() : number` — Computes the Euclidean length (straight-line length) of this quaternion,
considered as a 4 dimensional vector.
- `.lengthSq() : number` — Computes the squared Euclidean length (straight-line length) of this quaternion,
considered as a 4 dimensional vector. This can be useful if you are comparing the
lengths of two quaternions, as thi...
- `.multiply( q :Quaternion) :Quaternion` — Multiplies this quaternion by the given one.
- `.multiplyQuaternions( a :Quaternion, b :Quaternion) :Quaternion` — Multiplies the given quaternions and stores the result in this instance.
- `.normalize() :Quaternion` — Normalizes this quaternion - that is, calculated the quaternion that performs
the same rotation as this one, but has a length equal to 1 .
- `.premultiply( q :Quaternion) :Quaternion` — Pre-multiplies this quaternion by the given one.
- `.random() :Quaternion` — Sets this quaternion to a uniformly random, normalized quaternion.
- `.rotateTowards( q :Quaternion, step :number) :Quaternion` — Rotates this quaternion by a given angular step to the given quaternion.
The method ensures that the final quaternion will not overshoot q .
- `.set( x :number, y :number, z :number, w :number) :Quaternion` — Sets the quaternion components.
- `.setFromAxisAngle( axis :Vector3, angle :number) :Quaternion` — Sets this quaternion from the given axis and angle.
- `.setFromEuler( euler :Euler, update :boolean) :Quaternion` — Sets this quaternion from the rotation specified by the given
Euler angles.
- `.setFromRotationMatrix( m :Matrix4) :Quaternion` — Sets this quaternion from the given rotation matrix.
- `.setFromUnitVectors( vFrom :Vector3, vTo :Vector3) :Quaternion` — Sets this quaternion to the rotation required to rotate the direction vector vFrom to the direction vector vTo .
- `.slerp( qb :Quaternion, t :number) :Quaternion` — Performs a spherical linear interpolation between this quaternion and the target quaternion.
- `.slerpQuaternions( qa :Quaternion, qb :Quaternion, t :number) :Quaternion` — Performs a spherical linear interpolation between the given quaternions
and stores the result in this quaternion.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the components of this quaternion to the given array. If no array is provided,
the method returns a new instance.
- `.toJSON() : Array.<number>` — This methods defines the serialization result of this class. Returns the
numerical elements of this quaternion in an array of format [x, y, z, w] .

## Static Methods
- `.multiplyQuaternionsFlat( dst :Array.<number>, dstOffset :number, src0 :Array.<number>, srcOffset0 :number, src1 :Array.<number>, srcOffset1 :number) : Array.<number>` — Multiplies two quaternions. This implementation assumes the quaternion data are managed
in flat arrays.
- `.slerpFlat( dst :Array.<number>, dstOffset :number, src0 :Array.<number>, srcOffset0 :number, src1 :Array.<number>, srcOffset1 :number, t :number)` — Interpolates between two quaternions via SLERP. This implementation assumes the
quaternion data are managed in flat arrays.

## Source