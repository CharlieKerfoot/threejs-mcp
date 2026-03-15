# BufferAttributeNode
Extends: EventDispatcher→Node→InputNode→

In earlier three.js versions it was only possible to define attribute data
on geometry level. With BufferAttributeNode , it is also possible to do this
on the node level. This new approach is especially interesting when geometry data are generated via
compute shaders. The below line converts a storage buffer into an attribute node. material.positionNode = positionBuffer.toAttribute();

## Constructor
`newBufferAttributeNode( value :BufferAttribute|InterleavedBuffer| TypedArray, bufferType :string, bufferStride :number, bufferOffset :number)`
Constructs a new buffer attribute node.

## Properties
- `.attribute :BufferAttribute` — A reference to the buffer attribute. Default is null .
- `.bufferOffset : number` — The buffer offset. Default is 0 .
- `.bufferStride : number` — The buffer stride. Default is 0 .
- `.bufferType : string` — The buffer type (e.g. 'vec3' ). Default is null .
- `.global : boolean` — BufferAttributeNode sets this property to true by default. Default is true .
- `.instanced : boolean` — Whether the attribute is instanced or not. Default is false .
- `.isBufferNode : boolean` — This flag can be used for type testing. Default is true .
- `.usage : number` — The usage property. Set this to THREE.DynamicDrawUsage via .setUsage() ,
if you are planning to update the attribute data per frame. Default is StaticDrawUsage .

## Methods
- `.generate( builder :NodeBuilder) : string` — Generates the code snippet of the buffer attribute node.
- `.getHash( builder :NodeBuilder) : string` — This method is overwritten since the attribute data might be shared
and thus the hash should be shared as well.
- `.getInputType( builder :NodeBuilder) : string` — Overwrites the default implementation to return a fixed value 'bufferAttribute' .
- `.getNodeType( builder :NodeBuilder) : string` — This method is overwritten since the node type is inferred from
the buffer attribute.
- `.setInstanced( value :boolean) :BufferAttributeNode` — Sets the instanced property to the given value.
- `.setUsage( value :number) :BufferAttributeNode` — Sets the usage property to the given value.
- `.setup( builder :NodeBuilder)` — Depending on which value was passed to the node, setup() behaves
differently. If no instance of BufferAttribute was passed, the method
creates an internal attribute and configures it respectively.

## Source