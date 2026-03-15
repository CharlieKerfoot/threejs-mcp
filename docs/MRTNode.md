# MRTNode
Extends: EventDispatcher→Node→OutputStructNode→

This node can be used setup a MRT context for rendering. A typical MRT setup for
post-processing is shown below: The MRT output is defined as a dictionary.

## Constructor
`newMRTNode( outputNodes :Object.<string,Node>)`
Constructs a new output struct node.

## Properties
- `.blendModes : Object.<string,BlendMode>` — A dictionary storing the blend modes for each output.
- `.isMRTNode : boolean` — This flag can be used for type testing. Default is true .
- `.outputNodes : Object.<string,Node>` — A dictionary representing the MRT outputs. The key
is the name of the output, the value the node which produces
the output result.

## Methods
- `.get( name :string) :Node` — Returns the output node for the given name.
- `.getBlendMode( name :string) :BlendMode` — Returns the blend mode for the given output name.
- `.has( name :string) :NodeBuilder` — Returns true if the MRT node has an output with the given name.
- `.merge( mrtNode :MRTNode) :MRTNode` — Merges the outputs of the given MRT node with the outputs of this node.
- `.setBlendMode( name :string, blend :BlendMode) :MRTNode` — Sets the blend mode for the given output name.

## Source