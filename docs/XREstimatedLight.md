# XREstimatedLight
Extends: EventDispatcher→Object3D→Group→

This class can be used to represent the environmental light of
a XR session. It relies on the WebXR Lighting Estimation API.

## Constructor
`newXREstimatedLight( renderer :WebGLRenderer, environmentEstimation :boolean)`
Constructs a new light.

## Import

## Classes

## Properties
- `.directionalLight :DirectionalLight` — Represents the primary light from the XR environment.
- `.environment :Texture` — Will be set to a cube map in the SessionLightProbe if environment estimation is
available and requested. Default is null .
- `.lightProbe :LightProbe` — The light probe that represents the estimated light.

## Methods
- `.dispose()` — Frees the GPU-related resources allocated by this instance. Call this
method whenever this instance is no longer used in your app.

## Source