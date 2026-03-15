# RemapNode
Extends: EventDispatcher→Node→

This node allows to remap a node value from one range into another. E.g a value of 0.4 in the range [ 0.3, 0.5 ] should be remapped into the normalized range [ 0, 1 ] . RemapNode takes care of that and converts the original value of 0.4 to 0.5 .

## Constructor
`newRemapNode( node :Node, inLowNode :Node, inHighNode :Node, outLowNode :Node, outHighNode :Node)`
Constructs a new remap node.

## Properties
- `.doClamp : boolean` — Whether the node value should be clamped before
remapping it to the target range. Default is true .
- `.inHighNode :Node` — The source or current upper bound of the range.
- `.inLowNode :Node` — The source or current lower bound of the range.
- `.node :Node` — The node that should be remapped.
- `.outHighNode :Node` — The target upper bound of the range. Default is float(1) .
- `.outLowNode :Node` — The target lower bound of the range. Default is float(0) .

## Source