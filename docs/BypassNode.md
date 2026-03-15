# BypassNode
Extends: EventDispatcher→Node→

The class generates the code of a given node but returns another node in the output.
This can be used to call a method or node that does not return a value, i.e.
type void on an input where returning a value is required. Example:

## Constructor
`newBypassNode( outputNode :Node, callNode :Node)`
Constructs a new bypass node.

## Properties
- `.callNode :Node` — The call node.
- `.isBypassNode : boolean` — This flag can be used for type testing. Default is true .
- `.outputNode :Node` — The output node.

## Source