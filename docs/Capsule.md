# Capsule

A capsule is essentially a cylinder with hemispherical caps at both ends.
It can be thought of as a swept sphere, where a sphere is moved along a line segment. Capsules are often used as bounding volumes (next to AABBs and bounding spheres).

## Constructor
`newCapsule( start :Vector3, end :Vector3, radius :number)`
Constructs a new capsule.

## Import

## Properties
- `.end :Vector3` — The end vector.
- `.radius : number` — The capsule's radius. Default is 1 .
- `.start :Vector3` — The start vector.

## Methods
- `.clone() :Capsule` — Returns a new capsule with copied values from this instance.
- `.copy( capsule :Capsule) :Capsule` — Copies the values of the given capsule to this instance.
- `.getCenter( target :Vector3) :Vector3` — Returns the center point of this capsule.
- `.intersectsBox( box :Box3) : boolean` — Returns true if the given bounding box intersects with this capsule.
- `.set( start :Vector3, end :Vector3, radius :number) :Capsule` — Sets the capsule components to the given values.
Please note that this method only copies the values from the given objects.
- `.translate( v :Vector3) :Capsule` — Adds the given offset to this capsule, effectively moving it in 3D space.

## Source