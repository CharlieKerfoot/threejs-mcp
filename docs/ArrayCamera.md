# ArrayCamera
Extends: EventDispatcher→Object3D→Camera→PerspectiveCamera→

This type of camera can be used in order to efficiently render a scene with a
predefined set of cameras. This is an important performance aspect for
rendering VR scenes. An instance of ArrayCamera always has an array of sub cameras. It's mandatory
to define for each sub camera the viewport property which determines the
part of the viewport that is rendered with this camera.

## Constructor
`newArrayCamera( array :Array.<PerspectiveCamera>)`
Constructs a new array camera.

## Properties
- `.cameras : Array.<PerspectiveCamera>` — An array of perspective sub cameras.
- `.isArrayCamera : boolean` — This flag can be used for type testing. Default is true .
- `.isMultiViewCamera : boolean` — Whether this camera is used with multiview rendering or not. Default is false .

## Source