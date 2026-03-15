# Matrix3

Represents a 3x3 matrix. A Note on Row-Major and Column-Major Ordering: The constructor and Matrix3#set method take arguments in row-major order, while internally they are stored in the Matrix3#elements array in column-major order.
This means that calling: will result in the elements array containing: m.elements = [ 11, 21, 31,
               12, 22, 32,
               13, 23, 33 ]; and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and
most people are used to thinking about matrices in row-major order, the
three.js documentation shows matrices in row-major order. Just bear in
mind that if you are reading the source code, you'll have to take the
transpose of any matrices outlined here to make sense of the calculations.

## Constructor
`newMatrix3( n11 :number, n12 :number, n13 :number, n21 :number, n22 :number, n23 :number, n31 :number, n32 :number, n33 :number)`
Constructs a new 3x3 matrix. The arguments are supposed to be
in row-major order. If no arguments are provided, the constructor
initializes the matrix as an identity matrix.

## Properties
- `.elements : Array.<number>` — A column-major list of matrix values.
- `.isMatrix3 : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.clone() :Matrix3` — Returns a matrix with copied values from this instance.
- `.copy( m :Matrix3) :Matrix3` — Copies the values of the given matrix to this instance.
- `.determinant() : number` — Computes and returns the determinant of this matrix.
- `.equals( matrix :Matrix3) : boolean` — Returns true if this matrix is equal with the given one.
- `.extractBasis( xAxis :Vector3, yAxis :Vector3, zAxis :Vector3) :Matrix3` — Extracts the basis of this matrix into the three axis vectors provided.
- `.fromArray( array :Array.<number>, offset :number) :Matrix3` — Sets the elements of the matrix from the given array.
- `.getNormalMatrix( matrix4 :Matrix4) :Matrix3` — Computes the normal matrix which is the inverse transpose of the upper
left 3x3 portion of the given 4x4 matrix.
- `.identity() :Matrix3` — Sets this matrix to the 3x3 identity matrix.
- `.invert() :Matrix3` — Inverts this matrix, using the analytic method .
You can not invert with a determinant of zero. If you attempt this, the method produces
a zero matrix instead.
- `.makeRotation( theta :number) :Matrix3` — Sets this matrix as a 2D rotational transformation.
- `.makeScale( x :number, y :number) :Matrix3` — Sets this matrix as a 2D scale transform.
- `.makeTranslation( x :number |Vector2, y :number) :Matrix3` — Sets this matrix as a 2D translation transform.
- `.multiply( m :Matrix3) :Matrix3` — Post-multiplies this matrix by the given 3x3 matrix.
- `.multiplyMatrices( a :Matrix3, b :Matrix3) :Matrix3` — Multiples the given 3x3 matrices and stores the result
in this matrix.
- `.multiplyScalar( s :number) :Matrix3` — Multiplies every component of the matrix by the given scalar.
- `.premultiply( m :Matrix3) :Matrix3` — Pre-multiplies this matrix by the given 3x3 matrix.
- `.rotate( theta :number) :Matrix3` — Rotates this matrix by the given angle.
- `.scale( sx :number, sy :number) :Matrix3` — Scales this matrix with the given scalar values.
- `.set( n11 :number, n12 :number, n13 :number, n21 :number, n22 :number, n23 :number, n31 :number, n32 :number, n33 :number) :Matrix3` — Sets the elements of the matrix.The arguments are supposed to be
in row-major order.
- `.setFromMatrix4( m :Matrix4) :Matrix3` — Set this matrix to the upper 3x3 matrix of the given 4x4 matrix.
- `.setUvTransform( tx :number, ty :number, sx :number, sy :number, rotation :number, cx :number, cy :number) :Matrix3` — Sets the UV transform matrix from offset, repeat, rotation, and center.
- `.toArray( array :Array.<number>, offset :number) : Array.<number>` — Writes the elements of this matrix to the given array. If no array is provided,
the method returns a new instance.
- `.translate( tx :number, ty :number) :Matrix3` — Translates this matrix by the given scalar values.
- `.transpose() :Matrix3` — Transposes this matrix in place.
- `.transposeIntoArray( r :Array.<number>) :Matrix3` — Transposes this matrix into the supplied array, and returns itself unchanged.

## Source