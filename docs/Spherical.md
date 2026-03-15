# Spherical

This class can be used to represent points in 3D space as Spherical coordinates .

## Constructor
`newSpherical( radius :number, phi :number, theta :number)`
Constructs a new spherical.

## Properties
- `.phi : number` — The polar angle in radians from the y (up) axis. Default is 0 .
- `.radius : number` — The radius, or the Euclidean distance (straight-line distance) from the point to the origin. Default is 1 .
- `.theta : number` — The equator/azimuthal angle in radians around the y (up) axis. Default is 0 .

## Methods
- `.clone() :Spherical` — Returns a new spherical with copied values from this instance.
- `.copy( other :Spherical) :Spherical` — Copies the values of the given spherical to this instance.
- `.makeSafe() :Spherical` — Restricts the polar angle [page:.phi phi] to be between 0.000001 and pi - 0.000001 .
- `.set( radius :number, phi :number, theta :number) :Spherical` — Sets the spherical components by copying the given values.
- `.setFromCartesianCoords( x :number, y :number, z :number) :Spherical` — Sets the spherical components from the given Cartesian coordinates.
- `.setFromVector3( v :Vector3) :Spherical` — Sets the spherical components from the given vector which is assumed to hold
Cartesian coordinates.

## Source