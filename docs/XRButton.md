# XRButton

A utility class for creating a button that allows to initiate
immersive XR sessions based on WebXR. The button can be created
with a factory method and then appended ot the website's DOM. Compared to ARButton and VRButton , this class will
try to offer an immersive AR session first. If the device does not
support this type of session, it uses an immersive VR session.

## Import

## Static Methods
- `.createButton( renderer :WebGLRenderer|WebGPURenderer, sessionInit :XRSessionInit) : HTMLElement` — Constructs a new XR button.

## Source