# NodeMaterialObserver

This class is used by WebGPURenderer as management component.
It's primary purpose is to determine whether render objects require a
refresh right before they are going to be rendered or not.

## Constructor
`newNodeMaterialObserver( builder :NodeBuilder)`
Constructs a new node material observer.

## Properties
- `.hasAnimation : boolean` — Whether the node builder's 3D object is animated or not.
- `.hasNode : boolean` — Whether the material uses node objects or not.
- `.refreshUniforms : Array.<string>` — A list of all possible material uniforms
- `.renderId : number` — Holds the current render ID from the node frame. Default is 0 .
- `.renderObjects : WeakMap.<RenderObject, Object>` — A node material can be used by more than one render object so the
monitor must maintain a list of render objects.

## Methods
- `.containsNode( builder :NodeBuilder) : boolean` — Returns true if the node builder's material uses
node properties.
- `.equals( renderObject :RenderObject, lightsData :Array.<Light>) : boolean` — Returns true if the given render object has not changed its state.
- `.firstInitialization( renderObject :RenderObject) : boolean` — Returns true if the given render object is verified for the first time of this observer.
- `.getAttributesData( attributes :Object) : Object` — Returns an attribute data structure holding the attributes versions for
monitoring.
- `.getLights( lightsNode :LightsNode, renderId :number) : Array.<Object>` — Returns the lights for the given lights node and render ID.
- `.getLightsData( materialLights :Array.<Light>) : Array.<Object>` — Returns the lights data for the given material lights.
- `.getMaterialData( material :Material) : Object` — Returns a material data structure holding the material property values for
monitoring.
- `.getRenderObjectData( renderObject :RenderObject) : Object` — Returns monitoring data for the given render object.
- `.needsRefresh( renderObject :RenderObject, nodeFrame :NodeFrame) : boolean` — Checks if the given render object requires a refresh.
- `.needsVelocity( renderer :Renderer) : boolean` — Returns true if the current rendering produces motion vectors.

## Source