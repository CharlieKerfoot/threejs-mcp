# Matrix4

Represents a 4x4 matrix. The most common use of a 4x4 matrix in 3D computer graphics is as a transformation matrix.
For an introduction to transformation matrices as used in WebGL, check out this tutorial This allows a 3D vector representing a point in 3D space to undergo
transformations such as translation, rotation, shear, scale, reflection,
orthogonal or perspective projection and so on, by being multiplied by the
matrix. This is known as applying the matrix to the vector. A Note on Row-Major and Column-Major Ordering: The constructor and Matrix3#set method take arguments in row-major order, while internally they are stored in the Matrix3#elements array in column-major order.
This means that calling: will result in the elements array containing: m.elements = [ 11, 21, 31, 41,
               12, 22, 32, 42,
               13, 23, 33, 43,
               14, 24, 34, 44 ]; and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and
most people are used to thinking about matrices in row-major order, the
three.js documentation shows matrices in row-major order. Just bear in
mind that if you are reading the source code, you'll have to take the
transpose of any matrices outlined here to make sense of the calculations.

## Constructor
`newMatrix4( n11 :number, n12 :number, n13 :number, n14 :number, n21 :number, n22 :number, n23 :number, n24 :number, n31 :number, n32 :number, n33 :number, n34 :number, n41 :number, n42 :number, n43 :number, n44 :number)`
Constructs a new 4x4 matrix. The arguments are supposed to be
in row-major order. If no arguments are provided, the constructor
initializes the matrix as an identity matrix.

## Properties
- `.elements : Array.<number>` — A column-major list of matrix values.
- `.isMatrix4 : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.clone() :Matrix4` — Returns a matrix with copied values from this instance.
- `.compose( position :Vector3, quaternion :Quaternion, scale :Vector3) :Matrix4` — Sets this matrix to the transformation composed of the given position,
rotation (Quaternion) and scale.
- `.copy( m :Matrix4) :Matrix4` — Copies the values of the given matrix to this instance.
- `.copyPosition( m :Matrix4) :Matrix4` — Copies the translation component of the given matrix
into this matrix's translation component.
- `.decompose( position :Vector3, quaternion :Quaternion, scale :Vector3) :Matrix4` — Decomposes this matrix into its position, rotation and scale components
and provides the result in the given objects. Note: Not all matrices are decomposable in this way. For example, if an
object ...
- `.determinant() : number` — Computes and returns the determinant of this matrix. Based on the method outlined here .
- `.equals( matrix :Matrix4) : boolean` — Returns true if this matrix is equal with the given one.
- `.extractBasis( xAxis :Vector3, yAxis :Vector3, zAxis :Vector3) :Matrix4` — Extracts the basis of this matrix into the three axis vectors provided.
- `.extractRotation( m :Matrix4) :Matrix4` — Extracts the rotation component of the given matrix
into this matrix's rotation component. Note: This method does not support reflection matrices.
- `.fromArray( array :Array.<number>, offset :number) :Matrix4` — Sets the elements of the matrix from the given array.
- `.getMaxScaleOnAxis() : number` — Gets the maximum scale value of the three axes.
- `.identity() :Matrix4` — Sets this matrix to the 4x4 identity matrix.
- `.invert() :Matrix4` — Inverts this matrix, using the analytic method .
You can not invert with a determinant of zero. If you attempt this, the method produces
a zero matrix instead.
- `.lookAt( eye :Vector3, target :Vector3, up :Vector3) :Matrix4` — Sets the rotation component of the transformation matrix, looking from eye towards target , and oriented by the up-direction.
- `.makeBasis( xAxis :Vector3, yAxis :Vector3, zAxis :Vector3) :Matrix4` — Sets the given basis vectors to this matrix.
- `.makeOrthographic( left :number, right :number, top :number, bottom :number, near :number, far :number, coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem, reversedDepth :boolean) :Matrix4` — Creates a orthographic projection matrix. This is used internally by OrthographicCamera#updateProjectionMatrix .
- `.makePerspective( left :number, right :number, top :number, bottom :number, near :number, far :number, coordinateSystem :WebGLCoordinateSystem|WebGPUCoordinateSystem, reversedDepth :boolean) :Matrix4` — Creates a perspective projection matrix. This is used internally by PerspectiveCamera#updateProjectionMatrix .
- `.makeRotationAxis( axis :Vector3, angle :number) :Matrix4` — Sets this matrix as a rotational transformation around the given axis by
the given angle. This is a somewhat controversial but mathematically sound alternative to
rotating via Quaternions. See the ...
- `.makeRotationFromEuler( euler :Euler) :Matrix4` — Sets the rotation component (the upper left 3x3 matrix) of this matrix to
the rotation specified by the given Euler angles. The rest of
the matrix is set to the identity. Depending on the Euler#ord...
- `.makeRotationFromQuaternion( q :Quaternion) :Matrix4` — Sets the rotation component of this matrix to the rotation specified by
the given Quaternion as outlined here The rest of the matrix is set to the identity.
- `.makeRotationX( theta :number) :Matrix4` — Sets this matrix as a rotational transformation around the X axis by
the given angle.
- `.makeRotationY( theta :number) :Matrix4` — Sets this matrix as a rotational transformation around the Y axis by
the given angle.
- `.makeRotationZ( theta :number) :Matrix4` — Sets this matrix as a rotational transformation around the Z axis by
the given angle.
- `.makeScale( x :number, y :number, z :number) :Matrix4` — Sets this matrix as a scale transformation.
- `.makeShear( xy :number, xz :number, yx :number, yz :number, zx :number, zy :number) :Matrix4` — Sets this matrix as a shear transformation.
- `.makeTranslation( x :number |Vector3, y :number, z :number) :Matrix4` — Sets this matrix as a translation transform from the given vector.
- `.multiply( m :Matrix4) :Matrix4` — Post-multiplies this matrix by the given 4x4 matrix.
- `.multiplyMatrices( a :Matrix4, b :Matrix4) :Matrix4` — Multiples the given 4x4 matrices and stores the result
in this matrix.
- `.multiplyScalar( s :number) :Matrix4` — Multiplies every component of the matrix by the given scalar.
- `.premultiply( m :Matrix4) :Matrix4` — Pre-multiplies this matrix by the given 4x4 matrix.
- `.scale( v :Vector3) :Matrix4` — Multiplies the columns of this matrix by the given vector.
- `.set( n11 :number, n12 :number, n13 :number, n14 :number, n21 :number, n22 :number, n23 :number, n24 :number, n31 :number, n32 :number, n33 :number, n34 :number, n41 :number, n42 :number, n43 :number, n44 :number) :Matrix4` — Sets the elements of the matrix.The arguments are supposed to be
in row-major order.
- `.setFromMatrix3( m :Matrix3) :Matrix4` — Set the upper 3x3 elements of this matrix to the values of given 3x3 matrix.
- `.setPosition( x :number |Vector3, y :number, z :number) :Matrix4` — Sets the position component for this matrix from the given vector,
without affecting the rest of the matrix.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the elements of this matrix to the given array. If no array is provided,
the method returns a new instance.
- `.transpose() :Matrix4` — Transposes this matrix in place.

## Source