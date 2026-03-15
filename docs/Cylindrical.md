# Cylindrical

This class can be used to represent points in 3D space as Cylindrical coordinates .

## Constructor
`newCylindrical( radius :number, theta :number, y :number)`
Constructs a new cylindrical.

## Properties
- `.radius : number` — The distance from the origin to a point in the x-z plane. Default is 1 .
- `.theta : number` — A counterclockwise angle in the x-z plane measured in radians from the positive z-axis. Default is 0 .
- `.y : number` — The height above the x-z plane. Default is 0 .

## Methods
- `.clone() :Cylindrical` — Returns a new cylindrical with copied values from this instance.
- `.copy( other :Cylindrical) :Cylindrical` — Copies the values of the given cylindrical to this instance.
- `.set( radius :number, theta :number, y :number) :Cylindrical` — Sets the cylindrical components by copying the given values.
- `.setFromCartesianCoords( x :number, y :number, z :number) :Cylindrical` — Sets the cylindrical components from the given Cartesian coordinates.
- `.setFromVector3( v :Vector3) :Cylindrical` — Sets the cylindrical components from the given vector which is assumed to hold
Cartesian coordinates.

## Source