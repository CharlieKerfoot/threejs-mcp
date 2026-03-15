# VRButton

A utility class for creating a button that allows to initiate
immersive VR sessions based on WebXR. The button can be created
with a factory method and then appended ot the website's DOM.

## Import

## Properties
- `.xrSessionIsGranted : boolean` — Whether a XR session has been granted or not. Default is false .

## Static Methods
- `.createButton( renderer :WebGLRenderer|WebGPURenderer, sessionInit :XRSessionInit) : HTMLElement` — Constructs a new VR button.
- `.registerSessionGrantedListener()` — Registers a sessiongranted event listener. When a session is granted, the VRButton#xrSessionIsGranted
flag will evaluate to true . This method is automatically called by the module itself so there
...

## Source