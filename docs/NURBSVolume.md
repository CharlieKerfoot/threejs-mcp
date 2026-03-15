# NURBSVolume

This class represents a NURBS volume. Implementation is based on (x, y [, z=0 [, w=1]]) control points with w=weight .

## Constructor
`newNURBSVolume( degree1 :number, degree2 :number, degree3 :number, knots1 :Array.<number>, knots2 :Array.<number>, knots3 :Array.<number>, controlPoints :Array.<Array.<Array.<(Vector2|Vector3|Vector4)>>>)`
Constructs a new NURBS surface.

## Import

## Methods
- `.getPoint( t1 :number, t2 :number, t3 :number, target :Vector3)` — This method returns a vector in 3D space for the given interpolation factor. This vector lies within the NURBS volume.

## Source