# Layers

A layers object assigns an 3D object to 1 or more of 32
layers numbered 0 to 31 - internally the layers are stored as a
bit mask], and by default all 3D objects are a member of layer 0 . This can be used to control visibility - an object must share a layer with
a camera to be visible when that camera's view is
rendered. All classes that inherit from Object3D have an layers property which
is an instance of this class.

## Constructor
`newLayers()`
Constructs a new layers instance, with membership
initially set to layer 0 .

## Properties
- `.mask : number` — A bit mask storing which of the 32 layers this layers object is currently
a member of.

## Methods
- `.disable( layer :number)` — Removes membership of the given layer.
- `.disableAll()` — Removes the membership from all layers.
- `.enable( layer :number)` — Adds membership of the given layer.
- `.enableAll()` — Adds membership to all layers.
- `.isEnabled( layer :number) : boolean` — Returns true if the given layer is enabled.
- `.set( layer :number)` — Sets membership to the given layer, and remove membership all other layers.
- `.test( layers :Layers) : boolean` — Returns true if this and the given layers object have at least one
layer in common.
- `.toggle( layer :number)` — Toggles the membership of the given layer.

## Source