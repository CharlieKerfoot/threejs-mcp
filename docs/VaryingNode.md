# VaryingNode
Extends: EventDispatcher→Node→

Class for representing shader varyings as nodes. Varyings are create from
existing nodes like the following:

## Constructor
`newVaryingNode( node :Node, name :string)`
Constructs a new varying node.

## Properties
- `.global : boolean` — This flag is used for global cache. Default is true .
- `.interpolationSampling : string` — The interpolation sampling type of varying data. Default is null .
- `.interpolationType : string` — The interpolation type of the varying data. Default is null .
- `.isVaryingNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name of the varying in the shader. If no name is defined,
the node system auto-generates one. Default is null .
- `.node :Node` — The node for which a varying should be created.

## Methods
- `.setInterpolation( type :string, sampling :string) :VaryingNode` — Defines the interpolation type of the varying.
- `.setupVarying( builder :NodeBuilder) :NodeVarying` — This method performs the setup of a varying node with the current node builder.

## Source