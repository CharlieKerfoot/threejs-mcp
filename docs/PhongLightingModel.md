# PhongLightingModel
Extends: LightingModel→BasicLightingModel→

Represents the lighting model for a phong material. Used in MeshPhongNodeMaterial .

## Constructor
`newPhongLightingModel( specular :boolean)`
Constructs a new phong lighting model.

## Properties
- `.specular : boolean` — Whether specular is supported or not. Set this to false if you are
looking for a Lambert-like material meaning a material for non-shiny
surfaces, without specular highlights. Default is true .

## Methods
- `.direct( lightData :Object)` — Implements the direct lighting. The specular portion is optional an can be controlled
with the PhongLightingModel#specular flag.
- `.indirect( builder :NodeBuilder)` — Implements the indirect lighting.

## Source