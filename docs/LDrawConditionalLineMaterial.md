# LDrawConditionalLineMaterial
Extends: EventDispatcher→Material→ShaderMaterial→

A special line material for meshes loaded via LDrawLoader . This module can only be used with WebGLRenderer . When using WebGPURenderer ,
import the class from LDrawConditionalLineNodeMaterial.js .

## Constructor
`newLDrawConditionalLineMaterial( parameters :Object)`
Constructs a new conditional line material.

## Import

## Properties
- `.color :Color` — The material's color. Default is (1,1,1) .
- `.isLDrawConditionalLineMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.opacity : number` — The material's opacity. Default is 1 .

## Source