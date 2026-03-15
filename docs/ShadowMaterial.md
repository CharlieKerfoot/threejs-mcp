# ShadowMaterial
Extends: EventDispatcher→Material→

This material can receive shadows, but otherwise is completely transparent.

## Constructor
`newShadowMaterial( parameters :Object)`
Constructs a new shadow material.

## Properties
- `.color :Color` — Color of the material. Default is (0,0,0) .
- `.fog : boolean` — Whether the material is affected by fog or not. Default is true .
- `.isShadowMaterial : boolean` — This flag can be used for type testing. Default is true .
- `.transparent : boolean` — Overwritten since shadow materials are transparent
by default. Default is true .

## Source