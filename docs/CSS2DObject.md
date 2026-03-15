# CSS2DObject
Extends: EventDispatcher→Object3D→

The only type of 3D object that is supported by CSS2DRenderer .

## Constructor
`newCSS2DObject( element :HTMLElement)`
Constructs a new CSS2D object.

## Import

## Properties
- `.center :Vector2` — The 3D objects center point. ( 0, 0 ) is the lower left, ( 1, 1 ) is the top right. Default is (0.5,0.5) .
- `.element : HTMLElement` — The DOM element which defines the appearance of this 3D object. Default is true .
- `.isCSS2DObject : boolean` — This flag can be used for type testing. Default is true .

## Source