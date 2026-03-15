# Flow

A modifier for making meshes bend around curves. This module can only be used with WebGLRenderer . When using WebGPURenderer ,
import the class from CurveModifierGPU.js .

## Constructor
`newFlow( mesh :Mesh, numberOfCurves :number)`
Constructs a new Flow instance.

## Import

## Classes

## Methods
- `.moveAlongCurve( amount :number)` — Moves the mesh along the curve.
- `.updateCurve( index :number, curve :Curve)` — Updates the curve for the given curve index.

## Source