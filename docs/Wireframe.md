# Wireframe
Extends: EventDispatcher→Object3D→Mesh→

A class for creating wireframes based on wide lines. This module can only be used with WebGLRenderer . When using WebGPURenderer ,
import the class from lines/webgpu/Wireframe.js .

## Constructor
`newWireframe( geometry :LineSegmentsGeometry, material :LineMaterial)`
Constructs a new wireframe.

## Import

## Properties
- `.isWireframe : boolean` — This flag can be used for type testing. Default is true .

## Methods
- `.computeLineDistances() :Wireframe` — Computes an array of distance values which are necessary for rendering dashed lines.
For each vertex in the geometry, the method calculates the cumulative length from the
current point to the very ...

## Source