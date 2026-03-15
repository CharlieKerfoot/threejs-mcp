# InstancedFlow
Extends: Flow→

An instanced version of Flow for making meshes bend around curves, where the instances are placed on the curve. This module can only be used with WebGLRenderer .

## Constructor
`newInstancedFlow( count :number, curveCount :number, geometry :Geometry, material :Material)`
Constructs a new InstancedFlow instance.

## Import

## Classes

## Methods
- `.moveIndividualAlongCurve( index :number, offset :number)` — Move an individual element along the curve by a specific amount.
- `.setCurve( index :number, curveNo :number)` — Select which curve to use for an element.
- `.writeChanges( index :number)` — The extra information about which curve and curve position is stored in the translation components of the matrix for the instanced objects
This writes that information to the matrix and marks it as...

## Source