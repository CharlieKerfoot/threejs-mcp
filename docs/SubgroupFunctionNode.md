# SubgroupFunctionNode
Extends: EventDispatcher→Node→TempNode→

This class represents a set of built in WGSL shader functions that sync
synchronously execute an operation across a subgroup, or 'warp', of compute
or fragment shader invocations within a workgroup. Typically, these functions
will synchronously execute an operation using data from all active invocations
within the subgroup, then broadcast that result to all active invocations. In
other graphics APIs, subgroup functions are also referred to as wave intrinsics
(DirectX/HLSL) or warp intrinsics (CUDA).

## Constructor
`newSubgroupFunctionNode( method :string, aNode :Node, bNode :Node)`
Constructs a new function node.

## Properties
- `.aNode :Node` — The method's first argument.
- `.bNode :Node` — The method's second argument.
- `.method : string` — The subgroup/wave intrinsic method to construct.

## Source