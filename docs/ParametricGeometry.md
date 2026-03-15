# ParametricGeometry
Extends: EventDispatcher→BufferGeometry→

This class can be used to generate a geometry based on a parametric surface. Reference: Mesh Generation with Python

## Constructor
`newParametricGeometry( func :ParametricGeometry~Func, slices :number, stacks :number)`
Constructs a new parametric geometry.

## Import

## Properties
- `.parameters : Object` — Holds the constructor parameters that have been
used to generate the geometry. Any modification
after instantiation does not change the geometry.

## Type Definitions
- `.Func( u :number, v :number, target :Vector3)` — Parametric function definition of ParametricGeometry .

## Source