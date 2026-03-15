# CSS3DRenderer

This renderer can be used to apply hierarchical 3D transformations to DOM elements
via the CSS3 transform property. CSS3DRenderer is particularly interesting if you want to apply 3D effects to a website without
canvas based rendering. It can also be used in order to combine DOM elements with WebGL content. There are, however, some important limitations: It's not possible to use the material system of three.js . It's also not possible to use geometries. The renderer only supports 100% browser and display zoom. So CSS3DRenderer is just focused on ordinary DOM elements. These elements are wrapped into special
3D objects ( CSS3DObject or CSS3DSprite ) and then added to the scene graph.

## Constructor
`newCSS3DRenderer( parameters :CSS3DRenderer~Parameters)`
Constructs a new CSS3D renderer.

## Import

## Properties
- `.domElement : HTMLElement` — The DOM where the renderer appends its child-elements.

## Methods
- `.getSize() : Object` — Returns an object containing the width and height of the renderer.
- `.render( scene :Object3D, camera :Camera)` — Renders the given scene using the given camera.
- `.setSize( width :number, height :number)` — Resizes the renderer to the given width and height.

## Type Definitions
- `.Parameters` — Constructor parameters of CSS3DRenderer .

## Source