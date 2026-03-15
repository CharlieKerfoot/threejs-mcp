# ComputeNode
Extends: EventDispatcher→Node→

TODO

## Constructor
`newComputeNode( computeNode :Node, workgroupSize :Array.<number>)`
Constructs a new compute node.

## Properties
- `.computeNode :Node` — TODO
- `.count : number | Array.<number>` — TODO
- `.isComputeNode : boolean` — This flag can be used for type testing. Default is true .
- `.name : string` — The name or label of the uniform. Default is '' .
- `.onInitFunction : function` — TODO
- `.updateBeforeType : string` — The updateBeforeType is set to NodeUpdateType.OBJECT since ComputeNode#updateBefore is executed once per object by default. Default is 'object' .
- `.version : number` — TODO
- `.workgroupSize : Array.<number>` — TODO Default is [ 64 ] .

## Methods
- `.dispose()` — Executes the dispose event for this node.
- `.getCount() : number | Array.<number>` — TODO
- `.label( name :string) :ComputeNode` — Sets the ComputeNode#name property.
- `.onInit( callback :function) :ComputeNode` — TODO
- `.setCount( count :number | Array.<number>) :ComputeNode` — TODO
- `.setName( name :string) :ComputeNode` — Sets the ComputeNode#name property.
- `.updateBefore( frame :NodeFrame)` — The method execute the compute for this node.

## Source