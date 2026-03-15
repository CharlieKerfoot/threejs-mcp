# ShadowMapViewer

This is a helper for visualising a given light's shadow map.
It works for shadow casting lights: DirectionalLight and SpotLight.
It renders out the shadow map and displays it on a HUD. This module can only be used with WebGLRenderer . When using WebGPURenderer ,
import the class from ShadowMapViewerGPU.js .

## Constructor
`newShadowMapViewer( light :Light)`
Constructs a new shadow map viewer.

## Import

## Properties
- `.enabled : boolean` — Whether to display the shadow map viewer or not. Default is true .
- `.position : Object` — The position of the viewer. When changing this property, make sure
to call ShadowMapViewer#update . Default is true .
- `.size : Object` — The size of the viewer. When changing this property, make sure
to call ShadowMapViewer#update . Default is true .

## Methods
- `.render( renderer :WebGLRenderer)` — Renders the viewer. This method must be called in the app's animation loop.
- `.update()` — Updates the viewer.
- `.updateForWindowResize()` — Resizes the viewer. This method should be called whenever the app's
window is resized.

## Source