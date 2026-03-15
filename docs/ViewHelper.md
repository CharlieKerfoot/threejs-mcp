# ViewHelper
Extends: EventDispatcher→Object3D→

A special type of helper that visualizes the camera's transformation
in a small viewport area as an axes helper. Such a helper is often wanted
in 3D modeling tools or scene editors like the three.js editor . The helper allows to click on the X, Y and Z axes which animates the camera
so it looks along the selected axis.

## Constructor
`newViewHelper( camera :Camera, domElement :HTMLElement)`
Constructs a new view helper.

## Import

## Properties
- `.animating : boolean` — Whether the helper is currently animating or not. Default is false .
- `.center :Vector3` — The helper's center point.
- `.isViewHelper : boolean` — This flag can be used for type testing. Default is true .
- `.location : Object` — Controls the position of the helper in the viewport.
Use top / bottom for vertical positioning and left / right for horizontal.
If left is null , right is used. If top is null , bottom is used.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.
- `.handleClick( event :PointerEvent) : boolean` — This method should be called when a click or pointer event
has happened in the app.
- `.render( renderer :WebGLRenderer|WebGPURenderer)` — Renders the helper in a separate view in the viewport.
Position is controlled by the location property.
- `.setLabelStyle( font :string, color :string, radius :number)` — Sets the label style. Has no effect when the axes are unlabeled.
- `.setLabels( labelX :string | undefined, labelY :string | undefined, labelZ :string | undefined)` — Sets labels for each axis. By default, they are unlabeled.
- `.update( delta :number)` — Updates the helper. This method should be called in the app's animation
loop.

## Source