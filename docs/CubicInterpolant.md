# CubicInterpolant
Extends: Interpolant→

Fast and simple cubic spline interpolant. It was derived from a Hermitian construction setting the first derivative
at each sample position to the linear slope between neighboring positions
over their parameter interval.

## Constructor
`newCubicInterpolant( parameterPositions :TypedArray, sampleValues :TypedArray, sampleSize :number, resultBuffer :TypedArray)`
Constructs a new cubic interpolant.

## Source