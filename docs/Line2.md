# Line2
Extends: EventDispatcher→Object3D→Mesh→LineSegments2→

A polyline drawn between vertices. This adds functionality beyond Line , like arbitrary line width and changing width to
be in world units.It extends LineSegments2 , simplifying constructing segments from a
chain of points. This module can only be used with WebGLRenderer . When using WebGPURenderer ,
import the class from lines/webgpu/Line2.js .

## Constructor
`newLine2( geometry :LineGeometry, material :LineMaterial)`
Constructs a new wide line.

## Import

## Properties
- `.isLine2 : boolean` — This flag can be used for type testing. Default is true .

## Source