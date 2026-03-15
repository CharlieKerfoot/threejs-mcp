# CSS2DRenderer

This renderer is a simplified version of CSS3DRenderer . The only transformation that is
supported is translation. The renderer is very useful if you want to combine HTML based labels with 3D objects. Here too,
the respective DOM elements are wrapped into an instance of CSS2DObject and added to the
scene graph. All other types of renderable 3D objects (like meshes or point clouds) are ignored. CSS2DRenderer only supports 100% browser and display zoom.

## Constructor
`newCSS2DRenderer( parameters :CSS2DRenderer~Parameters)`
Constructs a new CSS2D renderer.

## Import

## Properties
- `.domElement : HTMLElement` — The DOM where the renderer appends its child-elements.
- `.sortObjects : boolean` — Controls whether the renderer assigns z-index values to CSS2DObject DOM elements.
If set to true , z-index values are assigned first based on the renderOrder and secondly - the distance to the came...

## Methods
- `.getSize() : Object` — Returns an object containing the width and height of the renderer.
- `.render( scene :Object3D, camera :Camera)` — Renders the given scene using the given camera.
- `.setSize( width :number, height :number)` — Resizes the renderer to the given width and height.

## Type Definitions
- `.Parameters` — Constructor parameters of CSS2DRenderer .

## Source