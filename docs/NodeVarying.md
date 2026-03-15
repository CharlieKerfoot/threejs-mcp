# NodeVarying
Extends: NodeVar→

NodeBuilder is going to create instances of this class during the build process
of nodes. They represent the final shader varyings that are going to be generated
by the builder. An array of node varyings is maintained in NodeBuilder#varyings for
this purpose.

## Constructor
`newNodeVarying( name :string, type :string, interpolationType :string, interpolationSampling :string)`
Constructs a new node varying.

## Properties
- `.interpolationSampling : string` — The interpolation sampling type of varying data. Default is null .
- `.interpolationType : string` — The interpolation type of the varying data. Default is null .
- `.isNodeVarying : boolean` — This flag can be used for type testing. Default is true .
- `.needsInterpolation : boolean` — Whether this varying requires interpolation or not. This property can be used
to check if the varying can be optimized for a variable. Default is false .

## Source