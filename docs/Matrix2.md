# Matrix2

Represents a 2x2 matrix. A Note on Row-Major and Column-Major Ordering: The constructor and Matrix2#set method take arguments in row-major order, while internally they are stored in the Matrix2#elements array in column-major order.
This means that calling: will result in the elements array containing: m.elements = [ 11, 21,
               12, 22 ]; and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and
most people are used to thinking about matrices in row-major order, the
three.js documentation shows matrices in row-major order. Just bear in
mind that if you are reading the source code, you'll have to take the
transpose of any matrices outlined here to make sense of the calculations.

## Constructor
`newMatrix2( n11 :number, n12 :number, n21 :number, n22 :number)`
Constructs a new 2x2 matrix. The arguments are supposed to be
in row-major order. If no arguments are provided, the constructor
initializes the matrix as an identity matrix.

## Classes

## Properties
- `.elements : Array.<number>` — A column-major list of matrix values.
- `.isMatrix2 : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.fromArray( array :Array.<number>, offset :number) :Matrix2` — Sets the elements of the matrix from the given array.
- `.identity() :Matrix2` — Sets this matrix to the 2x2 identity matrix.
- `.set( n11 :number, n12 :number, n21 :number, n22 :number) :Matrix2` — Sets the elements of the matrix.The arguments are supposed to be
in row-major order.

## Source